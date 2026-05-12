from enum import Enum

class TensionCompressionOnlyMode(str, Enum):
    Activated = "Activated",
    NoReversal = "NoReversal",
    Deactivated = "Deactivated",
    GradualActivation = "GradualActivation",

