from enum import Enum

class TranslationUnit(str, Enum):
    Ft = "ft",
    Inch = "inch",
    M = "m",
    Cm = "cm",
    Mm = "mm",

