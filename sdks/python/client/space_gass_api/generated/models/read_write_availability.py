from enum import Enum

class ReadWriteAvailability(str, Enum):
    Available = "Available",
    AllSeatsInUse = "AllSeatsInUse",
    NotLicensed = "NotLicensed",
    Expired = "Expired",
    Unknown = "Unknown",

