class PostenMapping_template_202411Dict:
    mapping_dict = {
    "version": "WV-beschermbuis",
    "WVlichtmast_config1": {
        "Lichtmast1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast",
            "attributen": {
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
                },
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
                }
            },
            "isHoofdAsset": True
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
                "modelnaam": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam",
                    "dotnotation": "modelnaam",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelModelnaam",
                    "value": "izylum",
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
        }
    },
    "WVConsole_config1": {
        "VerlichtingstoestelLED2": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED",
            "attributen": {
                "modelnaam": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel.modelnaam",
                    "dotnotation": "modelnaam",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelModelnaam",
                    "value": "izylum",
                    "range": None,
                    "union_type_criterium": None
                },
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
        "Console1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole",
            "attributen": {
                "naam": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam",
                    "dotnotation": "naam",
                    "type": "http://www.w3.org/2001/XMLSchema#string",
                    "value": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": True
        }
    },
    "Beschermbuis1": {
        "Beschermbuis1": {
            "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis",
            "attributen": {
                "indicatieveDiepte": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.indicatieveDiepte",
                    "dotnotation": "indicatieveDiepte",
                    "type": "http://www.w3.org/2001/XMLSchema#decimal",
                    "value": "0.8",
                    "range": None,
                    "union_type_criterium": None
                },
                "buitendiameter": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding.buitendiameter",
                    "dotnotation": "buitendiameter",
                    "type": "http://www.w3.org/2001/XMLSchema#decimal",
                    "value": "50.0",
                    "range": None,
                    "union_type_criterium": None
                },
                "materiaal": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.materiaal",
                    "dotnotation": "materiaal",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisMateriaal",
                    "value": "hdpe",
                    "range": None,
                    "union_type_criterium": None
                },
                "theoretischeLevensduur": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject.theoretischeLevensduur",
                    "dotnotation": "theoretischeLevensduur",
                    "type": "http://www.w3.org/2001/XMLSchema#nonNegativeInteger",
                    "value": "360.0",
                    "range": None,
                    "union_type_criterium": None
                },
                "kleur": {
                    "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis.kleur",
                    "dotnotation": "kleur",
                    "type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisKleur",
                    "value": "blauw",
                    "range": None,
                    "union_type_criterium": None
                }
            },
            "isHoofdAsset": True
        }
    }
}