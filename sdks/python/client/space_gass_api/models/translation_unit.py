from enum import Enum

class TranslationUnit(str, Enum):
    Feet = "Feet",
    Inches = "Inches",
    Metres = "Metres",
    Centimetres = "Centimetres",
    Millimetres = "Millimetres",

