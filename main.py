from pathlib import Path
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_file = Path(__file__)
    f = PostAssetFactory(this_file.parent / 'Postenmapping beschermbuis.db', directory=this_file.parent)
