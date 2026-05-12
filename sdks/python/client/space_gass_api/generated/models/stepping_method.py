from enum import Enum

class SteppingMethod(str, Enum):
    Linear = "Linear",
    Parabolic = "Parabolic",
    File = "File",

