from pathlib import Path

from otlmow_converter.DotnotationDictConverter import DotnotationDictConverter
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory


def find_mappings_by_instanced_asset(full_mapping_dict: dict, instance: OTLObject) -> list:
    mappings = []
    ddict = DotnotationDictConverter.to_dict(instance) # dotnotation dict representation of the instance

    for mapping_key, mapping_value_dict in full_mapping_dict.items():
        if mapping_key == 'version':
            continue
        add_mapping = True
        correct_type_mapping = None
        for _, mapping_dict in mapping_value_dict.items():
            if mapping_dict.get('typeURI') == ddict['typeURI']:
                correct_type_mapping = mapping_dict
                break
        if correct_type_mapping is None:
            continue

        for attribute, value in ddict.items():
            if attribute == 'typeURI':
                continue
            mapping_attribute_dict = correct_type_mapping['attributen'].get(attribute)
            if mapping_attribute_dict is None:
                add_mapping = False
                break
            if mapping_attribute_dict['value'] != value:
                add_mapping = False
                break
        if add_mapping:
            mappings.append((mapping_key, mapping_dict))

    print(f'Found {len(mappings)} mappings for {instance.typeURI}')
    return mappings


if __name__ == '__main__':
    factory = PostAssetFactory(
        mapping_artefact_path=Path(__file__).parent.parent / 'Postenmapping_Artefact.db',
        directory=Path(__file__).parent.parent / 'otlmow_postenmapping')
    mapping_dict = factory.mapping_dict

    instance = OTLObject.from_dict(
        {
            'typeURI': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis',
            'materiaal': 'gresbuizen',
            'sterktereeks': 'gres-240'
        }
    )

    mappings = find_mappings_by_instanced_asset(mapping_dict, instance)
    print(len(mappings))
    for key, m in mappings:
        print(key, m)


