from enum import Enum

class JobFileOpeningStatus(str, Enum):
    NoSGandNoATS = "NoSGandNoATS",
    SGNotOpenAndNoAts = "SGNotOpenAndNoAts",
    SGOpenAndNoAts = "SGOpenAndNoAts",
    NoSGButAts = "NoSGButAts",
    SGNotOpenButAts = "SGNotOpenButAts",
    SGOpenAndAts = "SGOpenAndAts",
    UnknownStatus = "UnknownStatus",

