from enum import Enum

class AccelerationUnit(str, Enum):
    Gravity = "Gravity",
    FeetPerSecondSquared = "FeetPerSecondSquared",
    InchesPerSecondSquared = "InchesPerSecondSquared",
    MetersPerSecondSquared = "MetersPerSecondSquared",
    CentimetersPerSecondSquared = "CentimetersPerSecondSquared",
    MillimetersPerSecondSquared = "MillimetersPerSecondSquared",
    KiloNewtonsPerKilogram = "KiloNewtonsPerKilogram",

