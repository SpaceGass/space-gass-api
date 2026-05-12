from enum import Enum

class RegistrationStatus(str, Enum):
    TitanCloud = "TitanCloud",
    TitanLM = "TitanLM",
    Unsupported = "Unsupported",
    Unregistered = "Unregistered",

