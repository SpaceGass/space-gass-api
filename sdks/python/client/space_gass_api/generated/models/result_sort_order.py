from enum import Enum

class ResultSortOrder(str, Enum):
    Asc = "Asc",
    Desc = "Desc",
    AbsDesc = "AbsDesc",
    AbsAsc = "AbsAsc",

