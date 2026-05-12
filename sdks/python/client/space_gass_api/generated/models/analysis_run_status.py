from enum import Enum

class AnalysisRunStatus(str, Enum):
    Queued = "Queued",
    Running = "Running",
    Cancelling = "Cancelling",
    Completed = "Completed",
    Failed = "Failed",
    Cancelled = "Cancelled",

