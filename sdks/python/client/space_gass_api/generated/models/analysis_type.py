from enum import Enum

class AnalysisType(str, Enum):
    LinearStaticAnalysis = "LinearStaticAnalysis",
    NonLinearStaticAnalysis = "NonLinearStaticAnalysis",
    DynamicFrequencyAnalysis = "DynamicFrequencyAnalysis",
    SpectralResponseAnalysis = "SpectralResponseAnalysis",
    BucklingAnalysis = "BucklingAnalysis",
    HarmonicAnalysis = "HarmonicAnalysis",
    LinearTransientAnalysis = "LinearTransientAnalysis",
    NonLinearTransientAnalysis = "NonLinearTransientAnalysis",
    None_ = "None",

