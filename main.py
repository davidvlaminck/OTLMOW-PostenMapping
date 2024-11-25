from pathlib import Path
from otlmow_converter.OtlmowConverter import OtlmowConverter
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory
from otlmow_postenmapping.PostenMappingTemplateModifier import PostenMappingTemplateModifier, create_dummy_assets

if __name__ == '__main__':
    this_directory = Path(__file__).parent
    f = PostAssetFactory(this_directory / 'templates-Mapping_Artefact-versie kris 0.1.db', directory=this_directory,
                         mapping_name='templates_mapping_artefact_krisVDS')

    start_assets = OtlmowConverter().from_file_to_objects(file_path=this_directory / 'start_bestand.xlsx')

    template_created_assets = []
    for i, asset in enumerate(start_assets):
        template_created_assets.extend(
            f.create_assets_from_mapping(
                asset
                , unique_index=i, keep_original_attributes=True
            )
        )

    dummy_assets = create_dummy_assets(template_created_assets)
    template_created_assets.extend(dummy_assets)

    OtlmowConverter().from_objects_to_file(sequence_of_objects=template_created_assets,
                                           file_path=this_directory / 'output.xlsx', abbreviate_excel_sheettitles=True)

    PostenMappingTemplateModifier.alter_excel_template(
        path_to_template_file_and_extension=this_directory / 'output.xlsx'
        , instantiated_assets=template_created_assets  # ! a list of OTLAssets and not a list of OTLAttributes
        , delete_dummy_records=True
    )
