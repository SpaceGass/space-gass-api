from enum import Enum

class JobForceAccessOption(str, Enum):
    None_ = "None",
    OpenPreviousSaved = "OpenPreviousSaved",
    OpenUnsavedMostRecent = "OpenUnsavedMostRecent",

