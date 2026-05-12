from enum import Enum

class OptimizationMethod(str, Enum):
    None_ = "None",
    Auto = "Auto",
    General = "General",
    Linear = "Linear",
    Circular = "Circular",

