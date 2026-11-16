from enum import Enum

class ModeStatus(str, Enum):
    Reported = "Reported",
    AboveUpperLimit = "AboveUpperLimit",
    BelowLowerLimit = "BelowLowerLimit",
    Unstable = "Unstable",

