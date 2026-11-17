from enum import Enum

class DesignCheckStatus(str, Enum):
    Passed = "Passed",
    PassedWithWarnings = "PassedWithWarnings",
    Failed = "Failed",

