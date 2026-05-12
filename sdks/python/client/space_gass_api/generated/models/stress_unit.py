from enum import Enum

class StressUnit(str, Enum):
    Ksf = "Ksf",
    Psf = "Psf",
    Ksi = "Ksi",
    Psi = "Psi",
    MPa = "MPa",
    KPa = "kPa",
    Pa = "Pa",
    Kgperm2 = "kgperm2",
    Kgpercm2 = "kgpercm2",
    Kgpermm2 = "kgpermm2",
    KNperm2 = "kNperm2",
    Npermm2 = "Npermm2",

