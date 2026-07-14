from enum import Enum

class JobFileOpeningStatus(str, Enum):
    NotFound = "NotFound",
    ReadyToOpen = "ReadyToOpen",
    Locked = "Locked",
    RecoveryFilesOnly = "RecoveryFilesOnly",
    UnsavedChanges = "UnsavedChanges",
    LockedWithUnsavedChanges = "LockedWithUnsavedChanges",
    Unknown = "Unknown",

