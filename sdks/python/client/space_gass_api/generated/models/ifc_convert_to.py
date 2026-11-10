from enum import Enum

class IfcConvertTo(str, Enum):
    Other = "Other",
    RevitStructure = "RevitStructure",
    ProSteel = "ProSteel",
    TeklaStructural = "TeklaStructural",
    XSteel = "XSteel",
    BentleyStructural = "BentleyStructural",
    StruCAD = "StruCAD",
    FrameworksPlus = "FrameworksPlus",
    Staad = "Staad",
    AdvanceSteel = "AdvanceSteel",
    Midas = "Midas",
    SAP2000 = "SAP2000",
    ETABS = "ETABS",
    BlueBeam = "BlueBeam",

