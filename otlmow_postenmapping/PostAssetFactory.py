import os
from pathlib import Path
from typing import List

from otlmow_converter.AssetFactory import AssetFactory
from otlmow_converter.DotnotationHelper import DotnotationHelper
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.OTLObject import OTLObject

from otlmow_postenmapping.SQLDbReader import SQLDbReader


class PostAssetFactory:
    def __init__(self, posten_mapping_path: Path = None):
        if posten_mapping_path is None:
            raise ValueError("can't init PostAssetFactory without a path to the file")

        if not os.path.isfile(posten_mapping_path):
            raise FileNotFoundError(f'{posten_mapping_path} is not a valid path. File does not exist.')

        self.posten_mapping = self.load_postenmapping(posten_mapping_path)

    def create_assets_from_post(self, post: str) -> List[OTLObject]:
        mapping = self.posten_mapping[post]
        created_assets = []
        for type_uri in mapping.keys():
            asset = AssetFactory.dynamic_create_instance_from_uri(type_uri)
            created_assets.append(asset)

            for attr in mapping[type_uri]['attributen']:
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
                        asset_atr.field = self.create_extended_field_floatordecimal(field, attr['range'])
                    else:
                        raise NotImplementedError(f'Not implemented for {field}')



                    pass

        return created_assets

    def create_extended_field_floatordecimal(self, field, range_str: str):
        extended_field = type('Extended' + field.__name__, (field, object), field.__dict__.copy())
        extended_field.super_class = field

        conditions = self.split_numeric_range_str(range_str)

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
    def load_postenmapping(posten_mapping_path: Path):
        reader = SQLDbReader(posten_mapping_path)
        data = reader.performReadQuery(
            """SELECT standaardpostnummer, typeURI, attribuutURI, dotnotatie, dtAttriURI, defaultWaarde, bereik, 
            usageNote, isMeetstaatAttr, isAltijdInTeVullen, isBasisMapping, mappingStatus, mappingOpmerking 
            FROM MappingSB250
            WHERE isBasisMapping = '1'""",
            {})

        mapping_dict = {}
        for row in data:
            mapping_nr = str(row[0])
            type_uri = str(row[1])
            if mapping_nr not in mapping_dict:
                mapping_dict[mapping_nr] = {type_uri: {'attributen': []}}

            if type_uri not in mapping_dict[mapping_nr]:
                mapping_dict[mapping_nr][type_uri] = {'attributen': []}

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

                mapping_dict[mapping_nr][type_uri]['attributen'].append({
                    'typeURI': attr_uri,
                    'dotnotation': dotnot_str,
                    'type': type_str,
                    'value': waarde_str,
                    'range': bereik_str
                })

        return mapping_dict

    @staticmethod
    def split_numeric_range_str(range_str: str) -> []:
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
