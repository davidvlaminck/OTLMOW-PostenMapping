from pathlib import Path

from otlmow_postenmapping.PostAssetFactory import PostAssetFactory


if __name__ == '__main__':
    factory = PostAssetFactory(
        mapping_artefact_path=Path(__file__).parent.parent / 'Postenmapping_Artefact.db',
        directory=Path(__file__).parent.parent / 'otlmow_postenmapping')

    d = factory.mapping_dict
    print(len(d.keys()))