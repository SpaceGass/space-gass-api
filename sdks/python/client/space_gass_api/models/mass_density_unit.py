from enum import Enum

class MassDensityUnit(str, Enum):
    KipsPerCubicFoot = "KipsPerCubicFoot",
    KipsPerCubicInch = "KipsPerCubicInch",
    PoundsPerCubicFoot = "PoundsPerCubicFoot",
    PoundsPerCubicInch = "PoundsPerCubicInch",
    TonnesPerCubicMetre = "TonnesPerCubicMetre",
    TonnesPerCubicCentimetre = "TonnesPerCubicCentimetre",
    TonnesPerCubicMillimetre = "TonnesPerCubicMillimetre",
    KilogramsPerCubicMetre = "KilogramsPerCubicMetre",
    KilogramsPerCubicCentimetre = "KilogramsPerCubicCentimetre",
    KilogramsPerCubicMillimetre = "KilogramsPerCubicMillimetre",

