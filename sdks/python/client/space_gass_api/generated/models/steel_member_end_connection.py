from enum import Enum

class SteelMemberEndConnection(str, Enum):
    Concentric = "Concentric",
    AngleShort = "AngleShort",
    AngleLong = "AngleLong",
    Flanges = "Flanges",
    Web = "Web",

