from enum import Enum

class DesignFailureType(str, Enum):
    LoadFactor = "LoadFactor",
    Seismic = "Seismic",
    Slenderness = "Slenderness",
    DesignError = "DesignError",

