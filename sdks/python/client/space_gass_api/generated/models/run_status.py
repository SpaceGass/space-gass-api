from enum import Enum

class RunStatus(str, Enum):
    Queued = "Queued",
    Running = "Running",
    Cancelling = "Cancelling",
    Completed = "Completed",
    Failed = "Failed",
    Cancelled = "Cancelled",

