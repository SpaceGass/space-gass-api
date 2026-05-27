from enum import Enum

class FilterPlateCutType(str, Enum):
    All = "All",
    Offset = "Offset",
    Duplicated = "Duplicated",
    AlongX = "AlongX",
    AlongY = "AlongY",
    AlongZ = "AlongZ",
    Horizontal = "Horizontal",
    Vertical = "Vertical",

