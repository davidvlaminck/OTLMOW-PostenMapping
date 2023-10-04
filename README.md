# OTLMOW-PostenMapping
[![PyPI](https://img.shields.io/pypi/v/otlmow-postenmapping?label=latest%20release)](https://pypi.org/project/otlmow-postenmapping/)
[![otlmow-postenmapping-downloads](https://img.shields.io/pypi/dm/otlmow-postenmapping)](https://pypi.org/project/otlmow-model/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-PostenMapping/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-PostenMapping/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-postenmapping)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-PostenMapping)](https://github.com/davidvlaminck/OTLMOW-PostenMapping/issues)
[![coverage](https://github.com/davidvlaminck/OTLMOW-PostenMapping/blob/master/UnitTests/coverage.svg)](https://htmlpreview.github.io/?https://github.com/davidvlaminck/OTLMOW-PostenMapping/blob/master/UnitTests/htmlcov/index.html)

## Summary
The main use case of otlmow-postenmapping is to translate the postenmapping artefact into Python dictionary for easy access and then using the dictionary to resolve a specific mapping into the corresponding assets

## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- [otlmow_model](https://github.com/davidvlaminck/OTLMOW-Model)
- [otlmow_modelbuilder](https://github.com/davidvlaminck/OTLMOW-ModelBuilder)
- [otlmow_converter](https://github.com/davidvlaminck/OTLMOW-Converter)
- [otlmow_template](https://github.com/davidvlaminck/OTLMOW-Template)
- [otlmow_postenmapping](https://github.com/davidvlaminck/OTLMOW-PostenMapping) (you are currently looking at this package)
- [otlmow_davie](https://github.com/davidvlaminck/OTLMOW-DAVIE)
- [otlmow_visuals](https://github.com/davidvlaminck/OTLMOW-Visuals)
- [otlmow_gui](https://github.com/davidvlaminck/OTLMOW-GUI)



## Installation and requirements
Currently, you need at least Python version 3.7 to use this library.

To install the OTL MOW project into your Python project, use pip to install it:
``` 
pip install otlmow_postenmapping
```
To upgrade an existing installation use:
``` 
pip install otlmow_postenmapping --upgrade
```

## Usage
To create the Python dictionary holding all the mappings, initialize a PostAssetFactory, using the file path of the postenmapping and the directory where the dictionary needs to go.
``` 
from pathlib import Path
from otlmow_postenmapping.PostAssetFactory import PostAssetFactory

if __name__ == '__main__':
    this_file = Path(__file__)
    f = PostAssetFactory(this_file.parent / 'Postenmapping beschermbuis.db', directory=this_file.parent)
``` 
