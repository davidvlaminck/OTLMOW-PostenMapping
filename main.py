from pathlib import Path

from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_model.OtlmowModel.Classes.Onderdeel.WVLichtmast import WVLichtmast

from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_file = Path(__file__)
    f = PostAssetFactory(this_file.parent / 'templates-Mapping_Artefact-versie kris 0.1.db', directory=this_file.parent)

    base_assets = []
    for i in range(5):
        base_asset = WVLichtmast()
        base_asset.assetId.identificator = f'000{i}'
        base_asset.bestekPostNummer = ['WVlichtmast_config1', 'random bestekpostnummer']
        base_assets.append(base_asset)

    template_created_assets = []
    for i, asset in enumerate(base_assets):
        template_created_assets.extend(f.create_assets_from_template(
            'WVlichtmast_config1', asset, unique_index=i))

    print(template_created_assets)
    OtlmowConverter().from_objects_to_file(sequence_of_objects=template_created_assets,
                                           file_path=this_file.parent / 'output.xlsx')
