from enum import Enum

class ShapeFabrication(str, Enum):
    Hot_Rolled = "Hot_Rolled",
    Stress_Relieved = "Stress_Relieved",
    Lightly_Welded = "Lightly_Welded",
    Heavily_Welded = "Heavily_Welded",
    Cold_Formed = "Cold_Formed",
    Cold_Formed_Stress_Relieved = "Cold_Formed_Stress_Relieved",

