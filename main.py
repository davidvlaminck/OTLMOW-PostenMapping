from pathlib import Path
from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_directory = Path(__file__).parent
    f = PostAssetFactory(this_directory / 'templates-Mapping_Artefact-versie kris 0.1.db',
                         directory=this_directory,
                         mapping_name='templates_mapping_artefact_krisVDS'
                         )

    start_assets = OtlmowConverter().from_file_to_objects(file_path=this_directory / 'start_bestand.xlsx')

    # TODO 2 parameters output_directory en output_file_name samenvoegen naar 1 parameter output_path
    f.create_assets_from_mapping_and_write_to_file(start_assets=start_assets,
                                                   output_path=this_directory / 'output.xlsx',
                                                   keep_original_attributes=True,
                                                   append_all_attributes=True
                                                   )