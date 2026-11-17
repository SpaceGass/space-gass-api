from enum import Enum

class DesignRunPhase(str, Enum):
    Designing = "Designing",
    Checking = "Checking",
    UpdatingSections = "UpdatingSections",
    StaticAnalysis = "StaticAnalysis",
    BucklingAnalysis = "BucklingAnalysis",

