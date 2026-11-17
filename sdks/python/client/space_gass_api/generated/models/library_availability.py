from enum import Enum

class LibraryAvailability(str, Enum):
    Common = "Common",
    Special = "Special",
    Legacy = "Legacy",
    Obsolete = "Obsolete",

