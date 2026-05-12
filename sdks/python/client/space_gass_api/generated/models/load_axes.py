from enum import Enum

class LoadAxes(str, Enum):
    Local = "Local",
    GlobalInclined = "GlobalInclined",
    GlobalProjected = "GlobalProjected",

