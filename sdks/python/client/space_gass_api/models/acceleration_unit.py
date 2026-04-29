from enum import Enum

class AccelerationUnit(str, Enum):
    Gs = "gs",
    Ftpersec2 = "ftpersec2",
    Inpersec2 = "inpersec2",
    Mpersec2 = "mpersec2",
    Cmpersec2 = "cmpersec2",
    Mmpersec2 = "mmpersec2",
    KNperkg = "kNperkg",

