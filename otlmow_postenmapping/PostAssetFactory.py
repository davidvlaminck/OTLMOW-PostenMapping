import os
from pathlib import Path
from typing import List

from otlmow_model.BaseClasses.OTLObject import OTLObject
from otlmow_model.Classes.Onderdeel.RetroreflecterendeFolie import RetroreflecterendeFolie
from otlmow_model.Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from otlmow_model.Classes.Onderdeel.Verkeersbordsteun import Verkeersbordsteun
from otlmow_converter.AssetFactory import AssetFactory

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
            created_assets.append(AssetFactory.dynamic_create_instance_from_uri(type_uri))

        return created_assets

    @staticmethod
    def load_postenmapping(posten_mapping_path: Path):
        reader = SQLDbReader(posten_mapping_path)
        data = reader.performReadQuery(
            'SELECT standaardpostnummer, typeURI, attribuutURI, dotnotatie, defaultWaarde, bereik, UsageNote, isMeetstaatAttr, isAltijdInTeVullen, isBasisMapping, mappingStatus, mappingOpmerking FROM "MappingSB250"',
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
                mapping_dict[mapping_nr][type_uri]['attributen'].append({
                    'typeURI': attr_uri,
                    'dotnotation': dotnot_str
                })

        return mapping_dict
