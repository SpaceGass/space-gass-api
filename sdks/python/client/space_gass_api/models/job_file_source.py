from enum import Enum

class JobFileSource(str, Enum):
    None_ = "None",
    LocalFile = "LocalFile",
    NewJob = "NewJob",

