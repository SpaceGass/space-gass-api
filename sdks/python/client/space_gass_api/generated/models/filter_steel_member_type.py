from enum import Enum

class FilterSteelMemberType(str, Enum):
    All = "All",
    Passed = "Passed",
    JustPassed = "JustPassed",
    JustFailed = "JustFailed",
    Failed = "Failed",
    SeismicFailure = "SeismicFailure",
    LrFailure = "LrFailure",
    DesignError = "DesignError",
    NotDesigned = "NotDesigned",

