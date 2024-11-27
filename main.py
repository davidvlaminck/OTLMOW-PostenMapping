from pathlib import Path
from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_directory = Path(__file__).parent
    f = PostAssetFactory(this_directory / 'templates-Mapping_Artefact-versie kris 0.1.db', directory=this_directory,
                         mapping_name='templates_mapping_artefact_krisVDS')

    start_assets = OtlmowConverter().from_file_to_objects(file_path=this_directory / 'start_bestand.xlsx')

    f.create_assets_from_mapping_and_write_to_file(start_assets=start_assets,
                                                   output_directory=this_directory,
                                                   output_file_name='outputDries',
                                                   keep_original_attributes=True)