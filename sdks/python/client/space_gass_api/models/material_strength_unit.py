from enum import Enum

class MaterialStrengthUnit(str, Enum):
    KiloPoundsPerSquareFoot = "KiloPoundsPerSquareFoot",
    PoundsPerSquareFoot = "PoundsPerSquareFoot",
    KiloPoundsPerSquareInch = "KiloPoundsPerSquareInch",
    PoundsPerSquareInch = "PoundsPerSquareInch",
    MegaPascals = "MegaPascals",
    KiloPascals = "KiloPascals",
    Pascals = "Pascals",
    KilogramsPerSquareMetre = "KilogramsPerSquareMetre",
    KilogramsPerSquareCentimetre = "KilogramsPerSquareCentimetre",
    KilogramsPerSquareMillimetre = "KilogramsPerSquareMillimetre",

