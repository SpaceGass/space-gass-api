from enum import Enum

class LengthUnit(str, Enum):
    Feet = "Feet",
    Inches = "Inches",
    Metres = "Metres",
    Centimetres = "Centimetres",
    Millimetres = "Millimetres",

