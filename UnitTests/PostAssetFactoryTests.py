from pathlib import Path
from unittest import TestCase

from otlmow_postenmapping.PostAssetFactory import PostAssetFactory


class PostAssetFactoryTests(TestCase):
    def set_up_factory(self):
        this_file = Path(__file__)
        f = PostAssetFactory(this_file.parent / 'Postenmapping v1.0.0 RC3 Verkeersborden-gemapt.db')
        return f

    def test_load_vkb_postenmapping(self):
        factory = self.set_up_factory()
        mapping = factory.posten_mapping
        self.assertTrue('1001.30704' in mapping)
        self.assertTrue('1001.20111' in mapping)

        self.assertTrue('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
                        in mapping['1001.30704'])
        self.assertTrue('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'
                        in mapping['1001.20111'])

        self.assertDictEqual({
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun': {
                'attributen':
                    [{'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter',
                      'dotnotation': 'diameter',
                      'type': 'http://www.w3.org/2001/XMLSchema#decimal',
                      'value': '114',
                      'range': None}]}
        }, mapping['1001.30704'])

    def test_create_assets_from_post_1001_20111(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.20111')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(1, folie_count)
        self.assertEqual(1, bord_count)
        self.assertEqual(1, steun_count)

        bord = next((a for a in created_assets if a.typeURI ==
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

        self.assertIsNotNone(bord)

        with self.subTest('correct value (x <= 0.5), not raising ValueError'):
            try:
                bord.oppervlakte.waarde = 0.5
                self.assertTrue(True)
            except ValueError:
                self.fail('ValueError raised')

        with self.subTest('incorrect value, raising ValueError'):
            with self.assertRaises(ValueError):
                bord.oppervlakte.waarde = 0.6

    def test_create_assets_from_post_1001_20128(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.20128')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(1, folie_count)
        self.assertEqual(1, bord_count)
        self.assertEqual(0, steun_count)

        bord = next((a for a in created_assets if a.typeURI ==
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

        self.assertIsNotNone(bord)

        with self.subTest('correct value (0.5 < x <= 1), not raising ValueError'):
            try:
                bord.oppervlakte.waarde = 0.6
                self.assertTrue(True)
            except ValueError:
                self.fail('ValueError raised')

        with self.subTest('incorrect value, raising ValueError'):
            with self.assertRaises(ValueError):
                bord.oppervlakte.waarde = 0.2
            with self.assertRaises(ValueError):
                bord.oppervlakte.waarde = 1.6

    def test_create_assets_from_post_1001_20131(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.20131')

        folie_count = sum(1 for a in created_assets if
                          a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if
                         a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if
                          a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(1, folie_count)
        self.assertEqual(1, bord_count)
        self.assertEqual(1, steun_count)

        folie = next((a for a in created_assets if a.typeURI ==
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie'), None)

        self.assertIsNotNone(folie)

        with self.subTest('correct value, not raising ValueError'):
            try:
                folie.folietype = 'folietype-3a'
                self.assertTrue(True)
            except ValueError:
                self.fail('ValueError raised')

        with self.subTest('incorrect value, raising ValueError'):
            with self.assertRaises(ValueError):
                folie.folietype = 'folietype-1'

    def test_create_assets_from_post_1001_30704(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.30704')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(0, folie_count)
        self.assertEqual(0, bord_count)
        self.assertEqual(1, steun_count)

        steun = next((a for a in created_assets if a.typeURI ==
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'), None)

        self.assertIsNotNone(steun)
        with self.subTest('correct value for float/decimal'):
            self.assertEqual(114.0, steun.diameter.waarde)

    def test_create_assets_from_post_1001_10171(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.10171')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(1, folie_count)
        self.assertEqual(1, bord_count)
        self.assertEqual(0, steun_count)

        bord = next((a for a in created_assets if a.typeURI ==
                     'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord'), None)

        self.assertIsNotNone(bord)
        with self.subTest('correct value for uniontype'):
            self.assertEqual(400, bord.afmeting.achthoekig.zijde.waarde)

    def test_split_range_str(self):
        with self.subTest('x < 0.5'):
            expected_list = [('st', 0.5)]
            self.assertListEqual(expected_list, PostAssetFactory.split_numeric_range_str('x < 0.5'))

        with self.subTest('x <= 0.5'):
            expected_list = [('ste', 0.5)]
            self.assertListEqual(expected_list, PostAssetFactory.split_numeric_range_str('x <= 0.5'))

        with self.subTest('0.5 < x'):
            expected_list = [('gt', 0.5)]
            self.assertListEqual(expected_list, PostAssetFactory.split_numeric_range_str('0.5 < x'))

        with self.subTest('0.5 <= x'):
            expected_list = [('gte', 0.5)]
            self.assertListEqual(expected_list, PostAssetFactory.split_numeric_range_str('0.5 <= x'))

        with self.subTest('0.5 < x <= 1'):
            expected_list = [('gt', 0.5), ('ste', 1)]
            self.assertListEqual(expected_list, PostAssetFactory.split_numeric_range_str('0.5 < x <= 1'))
