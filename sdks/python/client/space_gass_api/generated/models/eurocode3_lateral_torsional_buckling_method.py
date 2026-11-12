from enum import Enum

class Eurocode3LateralTorsionalBucklingMethod(str, Enum):
    General = "General",
    RolledOrEquivalentWelded = "RolledOrEquivalentWelded",
    Simplified = "Simplified",

