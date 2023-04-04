from pathlib import Path

from otlmow_model.Classes.Onderdeel.WVLichtmast import WVLichtmast

from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_file = Path(__file__)
    f = PostAssetFactory(this_file.parent / 'Postenmapping Wegverlichting WV lichtmast.db', directory=this_file.parent)
    base_asset = WVLichtmast()
    base_asset.assetId.identificator = '0000'
    assets = f.create_assets_from_type_template('WVlichtmast_config1', base_asset=base_asset)
    print(assets)
