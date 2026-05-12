from enum import Enum

class AngleType(str, Enum):
    NotApplicable = "NotApplicable",
    SingleType = "SingleType",
    ShortShort = "ShortShort",
    LongLong = "LongLong",
    Starred = "Starred",

