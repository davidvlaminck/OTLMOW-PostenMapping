from pathlib import Path

import pytest

from otlmow_postenmapping.PostAssetFactory import PostAssetFactory


def set_up_factory():
    this_file = Path(__file__)
    f = PostAssetFactory(this_file.parent / 'Postenmapping v1.0.0 RC3 Verkeersborden-gemapt.db',
                         directory=this_file.parent)
    return f


def test_load_vkb_postenmapping():
    factory = set_up_factory()
    mapping = factory.posten_mapping
    assert '1001.30704' in mapping
    assert '1001.20111' in mapping

    assert 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun' in mapping['1001.30704']
    assert 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord' \
           in mapping['1001.20111']

    assert mapping['1001.30704'] == {
        'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun': {
            'attributen':
                {'diameter': {
                    'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter',
                    'dotnotation': 'diameter',
                    'type': 'http://www.w3.org/2001/XMLSchema#decimal',
                    'value': '114',
                    'range': None}}}
    }


def test_create_assets_from_post_1001_20111(subtests):
    factory = set_up_factory()
    created_assets = factory.create_assets_from_post('1001.20111')

    folie_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
    bord_count = sum(1 for a in created_assets if
                     a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
    steun_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

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
    factory = set_up_factory()
    created_assets = factory.create_assets_from_post('1001.20128')

    folie_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
    bord_count = sum(1 for a in created_assets if
                     a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
    steun_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

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
    factory = set_up_factory()
    created_assets = factory.create_assets_from_post('1001.20131')

    folie_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
    bord_count = sum(1 for a in created_assets if
                     a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
    steun_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

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


def test_create_assets_from_post_1001_30704(subtests):
    factory = set_up_factory()
    created_assets = factory.create_assets_from_post('1001.30704')

    folie_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
    bord_count = sum(1 for a in created_assets if
                     a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
    steun_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

    assert folie_count == 0
    assert bord_count == 0
    assert steun_count == 1

    steun = next((a for a in created_assets if a.typeURI ==
                  'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'), None)

    assert steun is not None

    with subtests.test(msg='correct value for float/decimal'):
        assert steun.diameter.waarde == 114.0


def test_create_assets_from_post_1001_10171(subtests):
    factory = set_up_factory()
    created_assets = factory.create_assets_from_post('1001.10171')

    folie_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
    bord_count = sum(1 for a in created_assets if
                     a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
    steun_count = sum(1 for a in created_assets if
                      a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

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
