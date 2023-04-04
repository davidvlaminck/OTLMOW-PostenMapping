import json
import pprint

import os
from pathlib import Path
from typing import List, Dict

from otlmow_converter.DotnotationHelper import DotnotationHelper
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.OTLObject import OTLObject
from otlmow_model.Helpers.AssetCreator import dynamic_create_instance_from_uri

from otlmow_postenmapping.PostenMappingDict import PostenMappingDict
from otlmow_postenmapping.SQLDbReader import SQLDbReader


class PostAssetFactory:
    def __init__(self, posten_mapping_path: Path = None, directory: Path = None) -> None:
        if posten_mapping_path is not None:
            if not os.path.isfile(posten_mapping_path):
                raise FileNotFoundError(f'{posten_mapping_path} is not a valid path. File does not exist.')
            self.posten_mapping = self._write_and_return_posten_mapping(posten_mapping_path, directory=directory)

        if self.posten_mapping is None:
            self.posten_mapping = PostenMappingDict.mapping_dict

    def create_assets_from_type_template(self, template_key: str, base_asset: OTLObject) -> List[OTLObject]:
        mapping = self.posten_mapping[template_key]
        created_assets = [base_asset]

        # TODO
        # edit the base_asset instead of creating a new one

        for asset_to_create in mapping.keys():
            type_uri = mapping[asset_to_create]['typeURI']
            asset = dynamic_create_instance_from_uri(class_uri=type_uri)
            created_assets.append(asset)

            for attr in mapping[asset_to_create]['attributen'].values():
                if attr['value'] is not None:
                    value = attr['value']
                    if attr['type'] == 'http://www.w3.org/2001/XMLSchema#decimal':
                        value = float(attr['value'])

                    DotnotationHelper.set_attribute_by_dotnotation(asset, dotnotation=attr['dotnotation'],
                                                                   waarde_shortcut_applicable=True, value=value)
                elif attr['range'] is not None:
                    asset_atr = DotnotationHelper.get_attributes_by_dotnotation(asset, dotnotation=attr['dotnotation'],
                                                                                waarde_shortcut_applicable=True)
                    field = asset_atr.field
                    if field == FloatOrDecimalField:
                        asset_atr.field = self._create_extended_field_float_or_decimal(field, attr['range'])
                    elif issubclass(field, KeuzelijstField):
                        asset_atr.field = self._create_extended_field_keuzelijst(field, attr['range'])
                    else:
                        raise NotImplementedError(f'Not implemented for {field}')

        return created_assets

    def create_assets_from_post(self, post: str) -> List[OTLObject]:
        mapping = self.posten_mapping[post]
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

                    DotnotationHelper.set_attribute_by_dotnotation(asset, dotnotation=attr['dotnotation'],
                                                                   waarde_shortcut_applicable=True, value=value)
                elif attr['range'] is not None:
                    asset_atr = DotnotationHelper.get_attributes_by_dotnotation(asset, dotnotation=attr['dotnotation'],
                                                                                waarde_shortcut_applicable=True)
                    field = asset_atr.field
                    if field == FloatOrDecimalField:
                        asset_atr.field = self._create_extended_field_float_or_decimal(field, attr['range'])
                    elif issubclass(field, KeuzelijstField):
                        asset_atr.field = self._create_extended_field_keuzelijst(field, attr['range'])
                    else:
                        raise NotImplementedError(f'Not implemented for {field}')

        return created_assets

    def _create_extended_field_float_or_decimal(self, field, range_str: str) -> object:
        extended_field = type('Extended' + field.__name__, (field, object), field.__dict__.copy())
        extended_field.super_class = field

        conditions = self._split_numeric_range_str(range_str)

        def validate(value, attribuut, cls=extended_field):
            s = cls.super_class
            base_validate = s.validate(value, attribuut)
            if not base_validate:
                return base_validate

            if len(conditions) == 1:
                if conditions[0][0] == 'st':
                    if value < conditions[0][1]:
                        return True
                    return False
                elif conditions[0][0] == 'ste':
                    if value <= conditions[0][1]:
                        return True
                    return False
                elif conditions[0][0] == 'gt':
                    if value > conditions[0][1]:
                        return True
                    return False
                elif conditions[0][0] == 'gte':
                    if value >= conditions[0][1]:
                        return True
                    return False
            elif len(conditions) == 2:
                if conditions[0][0] == 'gt' and conditions[1][0] == 'st':
                    if conditions[0][1] < value < conditions[1][1]:
                        return True
                    return False
                elif conditions[0][0] == 'gte' and conditions[1][0] == 'st':
                    if conditions[0][1] <= value < conditions[1][1]:
                        return True
                    return False
                elif conditions[0][0] == 'gt' and conditions[1][0] == 'ste':
                    if conditions[0][1] < value <= conditions[1][1]:
                        return True
                    return False
                elif conditions[0][0] == 'gte' and conditions[1][0] == 'ste':
                    if conditions[0][1] <= value <= conditions[1][1]:
                        return True
                    return False

        extended_field.validate = validate
        return extended_field

    @staticmethod
    def _write_and_return_posten_mapping(posten_mapping_path: Path, directory: Path = None) -> Dict:
        reader = SQLDbReader(posten_mapping_path)
        version = reader.performReadQuery(
            """SELECT waarde
            FROM GeneralInfo
            WHERE parameter = 'Version'""",
            {})[0][0]

        if PostenMappingDict.mapping_dict['version'] == version:
            return PostenMappingDict.mapping_dict

        data = reader.performReadQuery(
            """SELECT standaardpostnummer, typeURI, attribuutURI, dotnotatie, dtAttriURI, defaultWaarde, bereik, 
            usageNote, isMeetstaatAttr, isAltijdInTeVullen, isBasisMapping, mappingStatus, mappingOpmerking, TempID 
            FROM MappingSB250
            WHERE isBasisMapping = '1'""",
            {})

        mapping_dict = {'version': version}
        for row in data:
            mapping_nr = str(row[0])
            temp_id = str(row[13])
            type_uri = str(row[1])
            if mapping_nr not in mapping_dict:
                mapping_dict[mapping_nr] = {}

            if temp_id not in mapping_dict[mapping_nr]:
                mapping_dict[mapping_nr][temp_id] = {'typeURI': type_uri, 'attributen': {}}

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

                mapping_dict[mapping_nr][temp_id]['attributen'][dotnot_str] = {
                    'typeURI': attr_uri,
                    'dotnotation': dotnot_str,
                    'type': type_str,
                    'value': waarde_str,
                    'range': bereik_str
                }

        PostAssetFactory._write_posten_mapping(mapping_dict, directory)

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
    def _write_posten_mapping(posten_mapping: dict, directory: Path = None) -> None:
        posten_mapping_str = json.dumps(posten_mapping, indent=4)
        file_dir = directory
        if file_dir is None:
            file_dir = Path(__file__).parent
        file_path = file_dir / 'PostenMappingDict.py'
        with open(file_path, "w") as file:
            file.write('class PostenMappingDict:\n    mapping_dict = ' + posten_mapping_str.replace('null', 'None'))
