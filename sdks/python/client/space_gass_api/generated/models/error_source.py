from enum import Enum

class ErrorSource(str, Enum):
    SpaceGass = "SpaceGass",
    Validation = "Validation",
    Api = "Api",
    Infrastructure = "Infrastructure",
    Unknown = "Unknown",

