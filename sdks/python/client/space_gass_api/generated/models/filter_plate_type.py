from enum import Enum

class FilterPlateType(str, Enum):
    All = "All",
    Triangular = "Triangular",
    Quadrilateral = "Quadrilateral",
    KirchoffThin = "KirchoffThin",
    MindlinThick = "MindlinThick",
    Offset = "Offset",
    Duplicated = "Duplicated",
    Horizontal = "Horizontal",
    Vertical = "Vertical",
    FreeVertex = "FreeVertex",
    Invalid = "Invalid",
    InvalidFlat = "InvalidFlat",
    InvalidInternalAngle = "InvalidInternalAngle",
    InvalidAspectRatio = "InvalidAspectRatio",
    InvalidRepeatedNode = "InvalidRepeatedNode",

