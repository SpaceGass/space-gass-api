from enum import Enum

class SteelMemberType(str, Enum):
    NonSpecific = "NonSpecific",
    Beam = "Beam",
    Column = "Column",
    Brace = "Brace",

