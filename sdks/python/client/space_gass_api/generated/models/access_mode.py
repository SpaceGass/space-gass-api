from enum import Enum

class AccessMode(str, Enum):
    ReadWrite = "ReadWrite",
    ReadOnly = "ReadOnly",
    NoAccess = "NoAccess",

