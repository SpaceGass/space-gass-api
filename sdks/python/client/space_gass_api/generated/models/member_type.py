from enum import Enum

class MemberType(str, Enum):
    Normal = "Normal",
    TensionOnly = "TensionOnly",
    CompressionOnly = "CompressionOnly",
    Cable = "Cable",
    Gap = "Gap",
    BrittleFuse = "BrittleFuse",
    PlasticFuse = "PlasticFuse",
    Pulley = "Pulley",
    Truss = "Truss",

