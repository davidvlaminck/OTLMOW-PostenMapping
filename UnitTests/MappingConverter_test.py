from pathlib import Path

import pytest

from otlmow_postenmapping.MappingConverter import MappingConverter

CURRENT_DIR = Path(__file__).parent


@pytest.skip
def test_create_db_locally():
    db_path = CURRENT_DIR / 'test.db'
    if db_path.exists():
        db_path.unlink()

    converter = MappingConverter(db_path=db_path)

    mapping_dict = {'version': 'test'}
    converter.convert(mapping_dict)
    assert db_path.exists()
    assert converter.get_version() == 'test'

    if db_path.exists():
        db_path.unlink()


def test_in_memory():
    converter = MappingConverter()

    mapping_dict = {'version': 'test'}
    converter.convert(mapping_dict)
    assert converter.get_version() == 'test'


def test_in_memory_simplest_template():
    converter = MappingConverter()

    mapping_dict = {'version': 'test',
                    'template_1': {
                        'asset_1': {
                            'isHoofdAsset': True,
                            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast',
                            'attributen': {
                                'heeftStopcontact': {
                                    'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact',
                                    'dotnotation': 'heeftStopcontact',
                                    'type': 'None',
                                    'value': 'False',
                                    'range': None
                                }}}}}
    converter.convert(mapping_dict)
    template_rows = converter.get_template_rows_by_name('template_1')
    assert len(template_rows) == 1
    assert template_rows[0].standaardpostnummer == 'template_1'
    assert template_rows[0].tempID == 'asset_1'
    assert template_rows[0].isHoofdAsset
    assert template_rows[0].typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    assert template_rows[0].defaultWaarde == 'False'
    assert template_rows[0].dotnotatie == 'heeftStopcontact'
    assert template_rows[
               0].attribuutURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact'
    assert template_rows[0].rijNummer == 1


def test_in_memory_template_two_attributes():
    converter = MappingConverter()

    mapping_dict = {'version': 'test',
                    'template_1': {
                        'asset_1': {
                            'isHoofdAsset': True,
                            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast',
                            'attributen': {
                                'heeftStopcontact': {
                                    'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact',
                                    'dotnotation': 'heeftStopcontact',
                                    'type': 'None',
                                    'value': 'False',
                                    'range': None
                                },
                                "aantalArmen": {
                                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen",
                                    "dotnotation": "aantalArmen",
                                    "type": "None",
                                    "value": "0",
                                    "range": None
                                }}}}}
    converter.convert(mapping_dict)
    template_rows = converter.get_template_rows_by_name('template_1')
    assert len(template_rows) == 2
    assert template_rows[0].standaardpostnummer == 'template_1'
    assert template_rows[0].tempID == 'asset_1'
    assert template_rows[0].isHoofdAsset
    assert template_rows[0].typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    assert template_rows[0].defaultWaarde == 'False'
    assert template_rows[0].dotnotatie == 'heeftStopcontact'
    assert template_rows[
               0].attribuutURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact'
    assert template_rows[0].rijNummer == 1

    assert template_rows[1].standaardpostnummer == 'template_1'
    assert template_rows[1].tempID == 'asset_1'
    assert template_rows[1].isHoofdAsset
    assert template_rows[1].typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    assert template_rows[1].defaultWaarde == '0'
    assert template_rows[1].dotnotatie == 'aantalArmen'
    assert template_rows[
               1].attribuutURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen'
    assert template_rows[1].rijNummer == 2


def test_in_memory_template_two_assets_second_without_attributes():
    converter = MappingConverter()

    mapping_dict = {'version': 'test',
                    'template_1': {
                        'asset_1': {
                            'isHoofdAsset': True,
                            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast',
                            'attributen': {
                                'heeftStopcontact': {
                                    'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact',
                                    'dotnotation': 'heeftStopcontact',
                                    'type': 'None',
                                    'value': 'False',
                                    'range': None
                                }}},
                        "asset_2": {
                            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver",
                            "attributen": {
                                "typeURI": {
                                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI",
                                    "dotnotation": "typeURI",
                                    "type": "None",
                                    "value": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver",
                                    "range": None
                                }
                            },
                            "isHoofdAsset": False
                        }}}
    converter.convert(mapping_dict)
    template_rows = converter.get_template_rows_by_name('template_1')
    assert len(template_rows) == 2
    assert template_rows[0].standaardpostnummer == 'template_1'
    assert template_rows[0].tempID == 'asset_1'
    assert template_rows[0].isHoofdAsset
    assert template_rows[0].typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    assert template_rows[0].defaultWaarde == 'False'
    assert template_rows[0].dotnotatie == 'heeftStopcontact'
    assert template_rows[
               0].attribuutURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact'
    assert template_rows[0].rijNummer == 1

    assert template_rows[1].standaardpostnummer == 'template_1'
    assert template_rows[1].tempID == 'asset_2'
    assert not template_rows[1].isHoofdAsset
    assert template_rows[1].typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver'
    assert template_rows[1].defaultWaarde == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver'
    assert template_rows[1].dotnotatie == 'typeURI'
    assert template_rows[
                1].attribuutURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.typeURI'
    assert template_rows[1].rijNummer == 2



