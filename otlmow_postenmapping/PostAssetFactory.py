import copy
import importlib
import json
import os
from pathlib import Path
from typing import List, Dict

from otlmow_converter.DotnotationHelper import DotnotationHelper
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject, dynamic_create_instance_from_uri

from otlmow_postenmapping.Exceptions.InvalidMappingKeyError import InvalidMappingKeyError
from otlmow_postenmapping.Exceptions.MultipleMappingKeysError import MultipleMappingKeysError
from otlmow_postenmapping.Exceptions.MissingMappingKeyError import MissingMappingKeyError

from otlmow_postenmapping.SQLDbReader import SQLDbReader


class PostAssetFactory:
    mapping_dict = None

    def __init__(self, mapping_artefact_path: Path = None, directory: Path = None, mapping_name: str = 'PostenMapping') -> None:
        self.mapping_dict = None
        if mapping_artefact_path is not None:
            if not os.path.isfile(mapping_artefact_path):
                raise FileNotFoundError(f'{mapping_artefact_path} is not a valid path. File does not exist.')
            self.mapping_dict = self._write_and_return_mapping_dict(mapping_artefact_path, directory=directory,
                                                                    mapping_name=mapping_name)

        if self.mapping_dict is None:
            self.mapping_dict = self.import_mapping_dict(directory=directory, mapping_name=mapping_name)

    @staticmethod
    def import_mapping_dict(directory: Path, mapping_name: str):
        class_name = f'{mapping_name}Dict'
        import_str = class_name
        if directory is not None:
            import_str = f'{directory}.{import_str}'
        py_mod = importlib.import_module(import_str)
        class_ = getattr(py_mod, class_name)
        return class_().mapping_dict

    def get_valid_mapping_key_from_base_asset(self, base_asset: OTLObject) -> str:
        """
        Searches in the "PostenMapping dictionary" for the "PostenMapping key" that matches with the "BestekPost nummer".

        Args:
            base_asset (OTLObject): The base asset, from which a "BestekPost nummer" is derived.

        Returns:
            str: The valid "PostenMapping key"
        """
        bestek_post_nummer = base_asset.bestekPostNummer

        if not bestek_post_nummer:
            raise MissingMappingKeyError("bestekPostNummer is missing or empty in the base asset")

        # Initialize an empty list to store all the valid keys
        valid_keys = []
        # Loop over the numbers and check the number of matches
        for candidate_key in bestek_post_nummer:
            if candidate_key in self.mapping_dict:
                valid_keys.append(candidate_key)

        # Remove duplicate identical values from the list, by converting it to a dictionary and back.
        valid_keys = list(dict.fromkeys(valid_keys))

        # Test the number of valid keys that were found
        nbr_valid_keys = len(valid_keys)
        if nbr_valid_keys == 0:
            raise InvalidMappingKeyError(f"bestekPostNummer(s) not found in posten mapping dictionary")
        elif nbr_valid_keys > 1:
            raise MultipleMappingKeysError("Multiple values found for bestekPostNummer; expected one.")
        else:
            return valid_keys[0]


    def create_assets_from_mapping(self, base_asset: OTLObject, unique_index: int) -> List[OTLObject]:
        mapping_key = self.get_valid_mapping_key_from_base_asset(base_asset)

        mapping = copy.deepcopy(self.mapping_dict[mapping_key])
        copy_base_asset = dynamic_create_instance_from_uri(base_asset.typeURI)
        copy_base_asset.assetId.identificator = base_asset.assetId.identificator
        copy_base_asset.assetId.toegekendDoor = base_asset.assetId.toegekendDoor
        copy_base_asset.bestekPostNummer = base_asset.bestekPostNummer
        copy_base_asset.bestekPostNummer.remove(mapping_key)
        base_asset_toestand = base_asset.toestand
        created_assets = [copy_base_asset]

        # change the local id of the base asset to the real id in the mapping
        # and change relation id's accordingly
        base_local_id = next(local_id for local_id, asset_mapping in mapping.items() if asset_mapping['isHoofdAsset'])
        for local_id, asset_mapping in mapping.items():
            if local_id == base_local_id:
                continue
            if 'bronAssetId.identificator' in asset_mapping['attributen']:
                if asset_mapping['attributen']['bronAssetId.identificator']['value'] == base_local_id:
                    asset_mapping['attributen']['bronAssetId.identificator'][
                        'value'] = base_asset.assetId.identificator
                else:
                    asset_mapping['attributen']['bronAssetId.identificator']['value'] = \
                        f"{asset_mapping['attributen']['bronAssetId.identificator']['value']}_{unique_index}"

            if 'doelAssetId.identificator' in asset_mapping['attributen']:
                if asset_mapping['attributen']['doelAssetId.identificator']['value'] == base_local_id:
                    asset_mapping['attributen']['doelAssetId.identificator'][
                        'value'] = base_asset.assetId.identificator
                else:
                    asset_mapping['attributen']['doelAssetId.identificator']['value'] = \
                        f"{asset_mapping['attributen']['doelAssetId.identificator']['value']}_{unique_index}"

        for asset_to_create in mapping.keys():
            if asset_to_create != base_local_id:
                type_uri = mapping[asset_to_create]['typeURI']
                asset = dynamic_create_instance_from_uri(class_uri=type_uri)
                asset.assetId.identificator = f'{asset_to_create}_{unique_index}'
                created_assets.append(asset)
                if hasattr(asset, 'toestand'):
                    asset.toestand = base_asset_toestand
            else:
                asset = copy_base_asset

            for attr in mapping[asset_to_create]['attributen'].values():
                if attr['dotnotation'] == 'typeURI':
                    continue
                if attr['value'] is not None:
                    value = attr['value']
                    if attr['type'] == 'http://www.w3.org/2001/XMLSchema#decimal':
                        value = float(attr['value'])

                    if asset == copy_base_asset:
                        asset_attr = DotnotationHelper.get_attribute_by_dotnotation(
                            base_asset, dotnotation=attr['dotnotation'], waarde_shortcut=True)
                        if isinstance(asset_attr, list):
                            asset_attr = asset_attr[0]
                        if asset_attr.waarde is not None:
                            continue

                    DotnotationHelper.set_attribute_by_dotnotation(asset, dotnotation=attr['dotnotation'], value=value)

        return created_assets

    def create_assets_from_post(self, post: str) -> List[OTLObject]:
        mapping = self.mapping_dict[post]
        created_assets = []
        for asset_to_create in mapping.keys():
            type_uri = mapping[asset_to_create]['typeURI']
            asset = dynamic_create_instance_from_uri(class_uri=type_uri)
            created_assets.append(asset)

            for attr in mapping[asset_to_create]['attributen'].values():
                if attr['value'] is not None:
                    value = attr['value']
                    if attr['type'] == 'http://www.w3.org/2001/XMLSchema#decimal':
                        value = float(attr['value'])

                    DotnotationHelper.set_attribute_by_dotnotation(asset, dotnotation=attr['dotnotation'], value=value)
                elif attr['range'] is not None:
                    asset_atr = DotnotationHelper.get_attribute_by_dotnotation(asset, dotnotation=attr['dotnotation'],
                                                                               waarde_shortcut=True)
                    field = asset_atr.field
                    if field == FloatOrDecimalField:
                        asset_atr.field = self._create_extended_field_float_or_decimal(field, attr['range'])
                    elif issubclass(field, KeuzelijstField):
                        asset_atr.field = self._create_extended_field_keuzelijst(field, attr['range'])
                    else:
                        raise NotImplementedError(f'Not implemented for {field}')

        return created_assets

    def _create_extended_field_float_or_decimal(self, field, range_str: str) -> object:
        extended_field = type(f'Extended{field.__name__}', (field, object), field.__dict__.copy())
        extended_field.super_class = field

        conditions = self._split_numeric_range_str(range_str)

        def validate(value, attribuut, cls=extended_field):
            s = cls.super_class
            base_validate = s.validate(value, attribuut)
            if not base_validate:
                return base_validate

            if len(conditions) == 1:
                if conditions[0][0] == 'st':
                    return value < conditions[0][1]
                elif conditions[0][0] == 'ste':
                    return value <= conditions[0][1]
                elif conditions[0][0] == 'gt':
                    return value > conditions[0][1]
                elif conditions[0][0] == 'gte':
                    return value >= conditions[0][1]
            elif len(conditions) == 2:
                if conditions[0][0] == 'gt' and conditions[1][0] == 'st':
                    return conditions[0][1] < value < conditions[1][1]
                elif conditions[0][0] == 'gte' and conditions[1][0] == 'st':
                    return conditions[0][1] <= value < conditions[1][1]
                elif conditions[0][0] == 'gt' and conditions[1][0] == 'ste':
                    return conditions[0][1] < value <= conditions[1][1]
                elif conditions[0][0] == 'gte' and conditions[1][0] == 'ste':
                    return conditions[0][1] <= value <= conditions[1][1]

        extended_field.validate = validate
        return extended_field

    @staticmethod
    def _write_and_return_mapping_dict(posten_mapping_path: Path, mapping_name: str, directory: Path = None) -> Dict:
        reader = SQLDbReader(posten_mapping_path)
        version = reader.perform_read_query(
            """SELECT waarde
            FROM GeneralInfo
            WHERE parameter = 'Version'""",
            {})[0][0]

        data = reader.perform_read_query(
            """SELECT code, typeURI, attribuutURI, dotnotatie, dataTypeURI, defaultWaarde, bereik, 
                usageNote, isMeetstaatAttribuut, altijdInTeVullen, isBasisMapping, mappingStatus, mappingOpmerking, tempId, 
                isHoofdAsset, unionTypeCriterium
            FROM Mapping
            WHERE isBasisMapping = '1'""",
            {})

        mapping_dict = {'version': version}
        for row in data:
            mapping_code, type_uri = str(row[0]), str(row[1])
            temp_id = str(row[13])

            if mapping_code not in mapping_dict:
                mapping_dict[mapping_code] = {}

            if temp_id not in mapping_dict[mapping_code]:
                mapping_dict[mapping_code][temp_id] = {'typeURI': type_uri, 'attributen': {}}

            mapping_dict[mapping_code][temp_id]['isHoofdAsset'] = (row[14] == 1)

            attr_uri = str(row[2])
            if attr_uri != 'None':
                dotnot_str = str(row[3])
                type_str = str(row[4])
                waarde_str = str(row[5])
                if waarde_str == 'None':
                    waarde_str = None
                bereik_str = str(row[6])
                if bereik_str == 'None':
                    bereik_str = None
                union_type_criterium_str = str(row[15])
                if union_type_criterium_str == 'None':
                    union_type_criterium_str = None

                mapping_dict[mapping_code][temp_id]['attributen'][dotnot_str] = {
                    'typeURI': attr_uri,
                    'dotnotation': dotnot_str,
                    'type': type_str,
                    'value': waarde_str,
                    'range': bereik_str,
                    'union_type_criterium': union_type_criterium_str
                }

        PostAssetFactory._write_posten_mapping(mapping_dict=mapping_dict, directory=directory,
                                               mapping_name=mapping_name)

        return mapping_dict

    @staticmethod
    def _split_numeric_range_str(range_str: str) -> []:
        if range_str == '' or range_str is None or 'x' not in range_str:
            return []

        splitted = range_str.split(' ')
        conditions = []

        if splitted[2] == 'x':
            if splitted[1] == '<':
                conditions.append(('gt', float(splitted[0])))
            elif splitted[1] == '<=':
                conditions.append(('gte', float(splitted[0])))
            if len(splitted) > 3:
                if splitted[3] == '<':
                    conditions.append(('st', float(splitted[4])))
                elif splitted[3] == '<=':
                    conditions.append(('ste', float(splitted[4])))
        elif splitted[0] == 'x':
            if splitted[1] == '<':
                conditions.append(('st', float(splitted[2])))
            elif splitted[1] == '<=':
                conditions.append(('ste', float(splitted[2])))

        return conditions

    @staticmethod
    def _create_extended_field_keuzelijst(field, range_str) -> object:
        extended_field = type('Extended' + field.__name__, (field, object), field.__dict__.copy())
        extended_field.super_class = field
        extended_field.options = {}

        field_options = field.options

        if '|' in range_str:
            valid_options = range_str.split('|')
        else:
            valid_options = [range_str]

        for option in valid_options:
            extended_field.options[option] = field_options[option]

        return extended_field

    @staticmethod
    def _write_posten_mapping(mapping_dict: dict, mapping_name: str, directory: Path = None) -> None:
        posten_mapping_str = json.dumps(mapping_dict, indent=4)
        file_dir = directory
        if file_dir is None:
            file_dir = Path(__file__).parent
        file_path = file_dir / f'{mapping_name}Dict.py'
        with open(file_path, "w") as file:
            file.write(f'class {mapping_name}Dict:\n    mapping_dict = ' + posten_mapping_str.replace('null', 'None').
                       replace('true', 'True').replace('false', 'False'))
