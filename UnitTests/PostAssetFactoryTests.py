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
                      'dotnotation': 'diameter'}]}
        }, mapping['1001.30704'])


    def test_create_assets_from_post_bord_steun_folie(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.20111')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(1, folie_count)
        self.assertEqual(1, bord_count)
        self.assertEqual(1, steun_count)

    def test_create_assets_from_post_steun(self):
        factory = self.set_up_factory()
        created_assets = factory.create_assets_from_post('1001.30704')

        folie_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        bord_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord')
        steun_count = sum(1 for a in created_assets if a.typeURI == 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self.assertEqual(0, folie_count)
        self.assertEqual(0, bord_count)
        self.assertEqual(1, steun_count)
