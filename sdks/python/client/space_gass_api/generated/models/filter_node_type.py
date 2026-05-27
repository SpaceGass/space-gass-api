from enum import Enum

class FilterNodeType(str, Enum):
    All = "All",
    Restrained = "Restrained",
    Constrained = "Constrained",
    Dummy = "Dummy",
    Duplicated = "Duplicated",
    Slave = "Slave",
    Master = "Master",
    RestrainedFixed = "RestrainedFixed",
    RestrainedReleased = "RestrainedReleased",
    RestrainedBiDirectional = "RestrainedBiDirectional",
    RestrainedPosDirectional = "RestrainedPosDirectional",
    RestrainedNegDirectional = "RestrainedNegDirectional",
    RestrainedOneWay = "RestrainedOneWay",
    RestrainedSpring = "RestrainedSpring",
    RestrainedVariableSpring = "RestrainedVariableSpring",
    RestrainedPlastic = "RestrainedPlastic",
    RestrainedFriction = "RestrainedFriction",
    RestrainedLinear = "RestrainedLinear",
    RestrainedNonLinear = "RestrainedNonLinear",

