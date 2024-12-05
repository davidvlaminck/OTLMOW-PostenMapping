class PostenMappingDict:
    mapping_dict = {
    "version": "WV-beschermbuis",
    "tt_wvlichtmast-demo": {
        "Lichtmast1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast",
            "attributen": {
                "beschermlaag": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.beschermlaag",
                    "dotnotation": "beschermlaag",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagConstrBeschermlaag",
                    "value": "gegalvaniseerd",
                    "range": None,
                    "union_type_criterium": None
                },
                "dwarsdoorsnede": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.dwarsdoorsnede",
                    "dotnotation": "dwarsdoorsnede",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagconstructieDwarsdoorsnede",
                    "value": "octagonaal",
                    "range": None,
                    "union_type_criterium": None
                },
                "heeftStopcontact": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact",
                    "dotnotation": "heeftStopcontact",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "masthoogte.standaardHoogte": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte",
                    "dotnotation": "masthoogte.standaardHoogte",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte",
                    "value": "10.00",
                    "range": None,
                    "union_type_criterium": None
                },
                "masttype": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masttype",
                    "dotnotation": "masttype",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasttype",
                    "value": "RM",
                    "range": None,
                    "union_type_criterium": None
                },
                "normeringBotsvriendelijk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.normeringBotsvriendelijk",
                    "dotnotation": "normeringBotsvriendelijk",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastBotsNormering",
                    "value": "niet-botsvriendelijke-mast",
                    "range": None,
                    "union_type_criterium": None
                },
                "aantalArmen": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen",
                    "dotnotation": "aantalArmen",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastAantArmen",
                    "value": "0",
                    "range": None,
                    "union_type_criterium": None
                },
                "armlengte": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.armlengte",
                    "dotnotation": "armlengte",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastArmlengte",
                    "value": "niet-van-toepassing",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": True
        },
        "VerlichtingstoestelLED1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED",
            "attributen": {
                "aantalTeVerlichtenRijstroken": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.aantalTeVerlichtenRijstroken",
                    "dotnotation": "aantalTeVerlichtenRijstroken",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken",
                    "value": "2",
                    "range": None,
                    "union_type_criterium": None
                },
                "kleurArmatuur": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurArmatuur",
                    "dotnotation": "kleurArmatuur",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlArmatuurkleur",
                    "value": "ral-7038",
                    "range": None,
                    "union_type_criterium": None
                },
                "heeftAntiVandalisme": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.heeftAntiVandalisme",
                    "dotnotation": "heeftAntiVandalisme",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "isFaunavriendelijk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isFaunavriendelijk",
                    "dotnotation": "isFaunavriendelijk",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "isLijnvormig": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isLijnvormig",
                    "dotnotation": "isLijnvormig",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "lichtpuntHoogte": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtpuntHoogte",
                    "dotnotation": "lichtpuntHoogte",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtpunthoogte",
                    "value": "10",
                    "range": None,
                    "union_type_criterium": None
                },
                "merk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.merk",
                    "dotnotation": "merk",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelMerk",
                    "value": "Schreder",
                    "range": None,
                    "union_type_criterium": None
                },
                "modelnaam": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam",
                    "dotnotation": "modelnaam",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelModelnaam",
                    "value": "izylum",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "VerlichtingstoestelLED2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED",
            "attributen": {
                "aantalTeVerlichtenRijstroken": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.aantalTeVerlichtenRijstroken",
                    "dotnotation": "aantalTeVerlichtenRijstroken",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken",
                    "value": "2",
                    "range": None,
                    "union_type_criterium": None
                },
                "kleurArmatuur": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurArmatuur",
                    "dotnotation": "kleurArmatuur",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlArmatuurkleur",
                    "value": "ral-7038",
                    "range": None,
                    "union_type_criterium": None
                },
                "heeftAntiVandalisme": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.heeftAntiVandalisme",
                    "dotnotation": "heeftAntiVandalisme",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "isFaunavriendelijk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isFaunavriendelijk",
                    "dotnotation": "isFaunavriendelijk",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "isLijnvormig": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isLijnvormig",
                    "dotnotation": "isLijnvormig",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "lichtpuntHoogte": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtpuntHoogte",
                    "dotnotation": "lichtpuntHoogte",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtpunthoogte",
                    "value": "10",
                    "range": None,
                    "union_type_criterium": None
                },
                "merk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.merk",
                    "dotnotation": "merk",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelMerk",
                    "value": "Schreder",
                    "range": None,
                    "union_type_criterium": None
                },
                "modelnaam": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam",
                    "dotnotation": "modelnaam",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelModelnaam",
                    "value": "izylum",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Armatuurcontroller1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller",
            "attributen": {
                "isDummydot": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.isDummydot",
                    "dotnotation": "isDummydot",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "merk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk",
                    "dotnotation": "merk",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Smartnodes",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Armatuurcontroller2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller",
            "attributen": {
                "isDummydot": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.isDummydot",
                    "dotnotation": "isDummydot",
                    "type": "http://www.w3.org/2001/XMLSchema#boolean",
                    "value": "False",
                    "range": None,
                    "union_type_criterium": None
                },
                "merk": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk",
                    "dotnotation": "merk",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Smartnodes",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "LEDdriver1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver",
            "attributen": {},
            "isHoofdAsset": False
        },
        "LEDdriver2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver",
            "attributen": {},
            "isHoofdAsset": False
        },
        "Bevestiging1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Lichtmast1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED1",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Bevestiging8": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Armatuurcontroller1",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Bevestiging3": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver1",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Sturing1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED1",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "VoedtAangestuurd1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Armatuurcontroller1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver1",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Bevestiging2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Lichtmast1",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED2",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Bevestiging7": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED2",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Armatuurcontroller2",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Bevestiging4": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED2",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver2",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "Sturing2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver2",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "VerlichtingstoestelLED2",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        },
        "VoedtAangestuurd2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd",
            "attributen": {
                "bronAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "bronAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "Armatuurcontroller2",
                    "range": None,
                    "union_type_criterium": None
                },
                "doelAssetId.identificator": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                    "dotnotation": "doelAssetId.identificator",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "LEDdriver2",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": False
        }
    }
}