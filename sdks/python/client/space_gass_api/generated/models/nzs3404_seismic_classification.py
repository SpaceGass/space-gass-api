from enum import Enum

class Nzs3404SeismicClassification(str, Enum):
    NonSeismic = "NonSeismic",
    Category1 = "Category1",
    Category2 = "Category2",
    Category3 = "Category3",
    Category4 = "Category4",

