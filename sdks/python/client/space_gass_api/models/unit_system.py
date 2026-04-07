from enum import Enum

class UnitSystem(str, Enum):
    Metric = "Metric",
    Imperial = "Imperial",
    Custom = "Custom",

