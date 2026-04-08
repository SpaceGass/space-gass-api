from enum import Enum

class MomentUnit(str, Enum):
    KipFeet = "KipFeet",
    KipInches = "KipInches",
    PoundFeet = "PoundFeet",
    PoundInches = "PoundInches",
    KiloNewtonMetres = "KiloNewtonMetres",
    KiloNewtonCentimetres = "KiloNewtonCentimetres",
    KiloNewtonMillimetres = "KiloNewtonMillimetres",
    NewtonMetres = "NewtonMetres",
    NewtonCentimetres = "NewtonCentimetres",
    NewtonMillimetres = "NewtonMillimetres",
    KilogramMetres = "KilogramMetres",
    KilogramCentimetres = "KilogramCentimetres",
    KilogramMillimetres = "KilogramMillimetres",

