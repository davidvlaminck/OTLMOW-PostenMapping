from pathlib import Path
from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_directory = Path(__file__).parent
    f = PostAssetFactory(this_directory / 'templates-Mapping_Artefact-20241127.db',
                         directory=this_directory
                         )

    start_assets = OtlmowConverter().from_file_to_objects(file_path=this_directory / 'demo_bim4infra' / 'basisimport.xlsx')

    f.create_assets_from_mapping_and_write_to_file(start_assets=start_assets,
                                                   output_path=this_directory / 'output.xlsx',
                                                   overwrite_original_attributes_by_template=False,
                                                   append_all_attributes=False
                                                   )