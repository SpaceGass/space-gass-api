from enum import Enum

class LoadCaseType(str, Enum):
    Primary = "Primary",
    Combination = "Combination",
    Step = "Step",
    Unused = "Unused",

