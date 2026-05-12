from enum import Enum

class DirectionAxis(str, Enum):
    NotApplicable = "NotApplicable",
    XAxis = "XAxis",
    YAxis = "YAxis",
    ZAxis = "ZAxis",
    NegativeXAxis = "NegativeXAxis",
    NegativeYAxis = "NegativeYAxis",
    NegativeZAxis = "NegativeZAxis",

