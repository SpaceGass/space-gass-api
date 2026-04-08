from enum import Enum

class SolverType(str, Enum):
    Pardiso = "Pardiso",
    Wavefront = "Wavefront",

