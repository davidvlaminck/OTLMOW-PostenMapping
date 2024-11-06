from pathlib import Path

import pytest
from otlmow_model.OtlmowModel.Classes.Onderdeel.Camera import Camera

from UnitTests.PostenMappingDict import PostenMappingDict
from otlmow_postenmapping.Exceptions.InvalidMappingKeyError import InvalidMappingKeyError
from otlmow_postenmapping.Exceptions.MultipleMappingKeysError import MultipleMappingKeysError
from otlmow_postenmapping.Exceptions.MissingMappingKeyError import MissingMappingKeyError
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory


def set_up_factory_from_artefact() -> PostAssetFactory:
    this_file = Path(__file__)
    return PostAssetFactory(
        this_file.parent / 'Postenmapping v1.0.0 RC3 Verkeersborden-gemapt.db',
        directory=this_file.parent,
    )


def set_up_factory_with_unittest_mapping() -> PostAssetFactory:
    factory = PostAssetFactory()
    factory.mapping_dict = PostenMappingDict.mapping_dict
    return factory


def test_load_factory_with_default_mapping():
    factory = PostAssetFactory()
    assert factory.mapping_dict is not None


def test_load_vkb_postenmapping():
    factory = set_up_factory_with_unittest_mapping()
    mapping = factory.mapping_dict
    assert '1001.10714' in mapping
    assert '1001.20111' in mapping

    assert mapping['1001.10714']['None'][
               'typeURI'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
    assert mapping['1001.20111']['2'][
               'typeURI'] == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'

    assert mapping['1001.10714'] == {
        'None':
             {'attributen': {'diameter':
                                 {'dotnotation': 'diameter',
                                  'range': None,
                                  'type': 'http://www.w3.org/2001/XMLSchema#decimal',
                                  'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter',
                                  'value': '114'},
                             'lengte':
                                 {'dotnotation': 'lengte',
                                  'range': None,
                                  'type': 'http://www.w3.org/2001/XMLSchema#decimal',
                                  'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengte',
                                  'value': None}},
              'isHoofdAsset': False,
              'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'}}


def test_create_assets_from_post_1001_20111(subtests):
    factory = set_up_factory_with_unittest_mapping()
    created_assets = factory.create_assets_from_post('1001.20111')

    folie_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
                      for a in created_assets)
    bord_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                     for a in created_assets)
    steun_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                      for a in created_assets)

    assert folie_count == 1
    assert bord_count == 1
    assert steun_count == 1

    bord = next((a for a in created_assets if a.typeURI ==
                 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

    assert bord is not None

    with subtests.test(msg='correct value (x <= 0.5), not raising ValueError'):
        bord.oppervlakte.waarde = 0.5
        assert True

    with subtests.test(msg='incorrect value, raising ValueError'):
        with pytest.raises(ValueError):
            bord.oppervlakte.waarde = 0.6


def test_create_assets_from_post_1001_20128(subtests):
    factory = set_up_factory_with_unittest_mapping()
    created_assets = factory.create_assets_from_post('1001.20128')

    folie_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
                      for a in created_assets)
    bord_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                     for a in created_assets)
    steun_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                      for a in created_assets)

    assert folie_count == 1
    assert bord_count == 1
    assert steun_count == 0

    bord = next((a for a in created_assets if a.typeURI ==
                 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

    assert bord is not None

    with subtests.test(msg='correct value (0.5 < x <= 1), not raising ValueError'):
        bord.oppervlakte.waarde = 0.6
        assert True

    with subtests.test(msg='incorrect value, raising ValueError'):
        with pytest.raises(ValueError):
            bord.oppervlakte.waarde = 0.2
        with pytest.raises(ValueError):
            bord.oppervlakte.waarde = 1.6


def test_create_assets_from_post_1001_20131(subtests):
    factory = set_up_factory_with_unittest_mapping()
    created_assets = factory.create_assets_from_post('1001.20131')

    folie_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
                      for a in created_assets)
    bord_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                     for a in created_assets)
    steun_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                      for a in created_assets)

    assert folie_count == 1
    assert bord_count == 1
    assert steun_count == 1

    folie = next((a for a in created_assets if a.typeURI ==
                  'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'), None)

    assert folie is not None

    with subtests.test(msg='correct value, not raising ValueError'):
        folie.folietype = 'folietype-3a'
        assert True

    with subtests.test(msg='incorrect value, raising ValueError'):
        with pytest.raises(ValueError):
            folie.folietype = 'folietype-1'

def test_get_valid_template_key_from_base_asset_happy_flow():
    # arrange opzetten test scenario 1
    factory = set_up_factory_with_unittest_mapping() # maakt zelf een factory die specifiek gemaakt is voor uw test
    asset = Camera() # maakt een asset aan die specifiek gemaakt is voor uw test
    asset.bestekPostNummer = ['1001.10111']

    # act code uitvoeren binnen scenario
    template_key = factory.get_valid_mapping_key_from_base_asset(asset)

    # assert checken of de code het scenario correct heeft uitgevoerd
    assert template_key == '1001.10111'

    # arrange opzetten test scenario 2
    factory = set_up_factory_with_unittest_mapping() # maakt zelf een factory die specifiek gemaakt is voor uw test
    asset = Camera() # maakt een asset aan die specifiek gemaakt is voor uw test
    asset.bestekPostNummer = ['1001.10111', 'randomBestekPostNummer']

    # act code uitvoeren binnen scenario
    template_key = factory.get_valid_mapping_key_from_base_asset(asset)

    # assert checken of de code het scenario correct heeft uitgevoerd
    assert template_key == '1001.10111'



def test_get_valid_template_key_from_base_asset_invalid_template_key():
    # arrange opzetten test scenario
    factory = set_up_factory_with_unittest_mapping()  # maakt zelf een factory die specifiek gemaakt is voor uw test
    asset = Camera()  # maakt een asset aan die specifiek gemaakt is voor uw test
    asset.bestekPostNummer = ['invalid_template_key']

    # act + assert
    with pytest.raises(InvalidMappingKeyError):
        factory.get_valid_mapping_key_from_base_asset(asset)

def test_get_valid_template_key_from_base_asset_multiple_template_keys():
    # arrange opzetten test scenario
    factory = set_up_factory_with_unittest_mapping()  # maakt zelf een factory die specifiek gemaakt is voor uw test
    asset = Camera()  # maakt een asset aan die specifiek gemaakt is voor uw test
    asset.bestekPostNummer = ['1001.10111', '1001.10112']

    # act + assert
    with pytest.raises(MultipleMappingKeysError):
        factory.get_valid_mapping_key_from_base_asset(asset)

def test_get_valid_template_key_from_base_asset_missing_template_key():
    # arrange opzetten test scenario
    factory = set_up_factory_with_unittest_mapping()  # maakt zelf een factory die specifiek gemaakt is voor uw test
    asset = Camera()  # maakt een asset aan die specifiek gemaakt is voor uw test
    asset.bestekPostNummer = None

    # act + assert
    with pytest.raises(MissingMappingKeyError):
        factory.get_valid_mapping_key_from_base_asset(asset)

def test_create_assets_from_post_1001_30704(subtests):
    factory = set_up_factory_with_unittest_mapping()
    created_assets = factory.create_assets_from_post('1001.30704')

    folie_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
                      for a in created_assets)
    bord_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                     for a in created_assets)
    steun_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                      for a in created_assets)

    assert folie_count == 0
    assert bord_count == 0
    assert steun_count == 1

    steun = next((a for a in created_assets if a.typeURI ==
                  'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'), None)

    assert steun is not None

    with subtests.test(msg='correct value for float/decimal'):
        assert steun.diameter.waarde == 114.0


def test_create_assets_from_post_1001_10171(subtests):
    factory = set_up_factory_with_unittest_mapping()
    created_assets = factory.create_assets_from_post('1001.10171')

    folie_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'
                      for a in created_assets)
    bord_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                     for a in created_assets)
    steun_count = sum(a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                      for a in created_assets)

    assert folie_count == 1
    assert bord_count == 1
    assert steun_count == 0

    bord = next((a for a in created_assets if a.typeURI ==
                 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

    assert bord is not None

    with subtests.test(msg='correct value for uniontype'):
        assert bord.afmeting.achthoekig.zijde.waarde == 400


def test_split_range_str(subtests):
    with subtests.test(msg='x < 0.5'):
        expected_list = [('st', 0.5)]
        assert PostAssetFactory._split_numeric_range_str('x < 0.5') == expected_list

    with subtests.test(msg='x <= 0.5'):
        expected_list = [('ste', 0.5)]
        assert PostAssetFactory._split_numeric_range_str('x <= 0.5') == expected_list

    with subtests.test(msg='0.5 < x'):
        expected_list = [('gt', 0.5)]
        assert PostAssetFactory._split_numeric_range_str('0.5 < x') == expected_list

    with subtests.test(msg='0.5 <= x'):
        expected_list = [('gte', 0.5)]
        assert PostAssetFactory._split_numeric_range_str('0.5 <= x') == expected_list

    with subtests.test(msg='0.5 < x <= 1'):
        expected_list = [('gt', 0.5), ('ste', 1)]
        assert PostAssetFactory._split_numeric_range_str('0.5 < x <= 1') == expected_list
