from enum import Enum

class AngleType(str, Enum):
    NotApplicable = "NotApplicable",
    Single = "Single",
    ShortShort = "ShortShort",
    LongLong = "LongLong",
    Starred = "Starred",

