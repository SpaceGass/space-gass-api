from enum import Enum

class ReactionSummaryType(str, Enum):
    Load = "Load",
    Reaction = "Reaction",
    Residual = "Residual",

