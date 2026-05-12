from enum import Enum

class FrictionNormalDirection(str, Enum):
    Either = "Either",
    PositiveOnly = "PositiveOnly",
    NegativeOnly = "NegativeOnly",

