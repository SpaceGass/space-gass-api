from enum import Enum

class AnalysisOptimizationMethod(str, Enum):
    None_ = "None",
    Auto = "Auto",
    General = "General",
    Linear = "Linear",
    Circular = "Circular",

