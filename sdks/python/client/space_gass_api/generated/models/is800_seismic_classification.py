from enum import Enum

class Is800SeismicClassification(str, Enum):
    NonSeismic = "NonSeismic",
    OrdinaryConcentricallyBracedFrame = "OrdinaryConcentricallyBracedFrame",
    SpecialConcentricallyBracedFrame = "SpecialConcentricallyBracedFrame",
    OrdinaryMomentFrame = "OrdinaryMomentFrame",
    SpecialMomentFrame = "SpecialMomentFrame",

