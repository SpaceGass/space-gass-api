from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .analysis_progress import AnalysisProgress
    from .analysis_run_parameters import AnalysisRun_parameters
    from .analysis_run_status import AnalysisRunStatus
    from .analysis_type import AnalysisType
    from .convergence_entry import ConvergenceEntry

@dataclass
class AnalysisRun(Parsable):
    """
    Response DTO representing an analysis run and its current state.Used for both the initial 202 response and subsequent status polling.
    """
    # SPACEGASS analysis types. Values map to the SPACEGASS internal SGAnalysisType IDs.
    analysis_type: Optional[AnalysisType] = None
    # When the run finished. Null if still running.
    completed_at: Optional[datetime.datetime] = None
    # Convergence history from non-linear analysis iterations.Available while running (from live progress) and after completion (persisted on run).Null for linear analyses or before any convergence is reached.
    convergence_history: Optional[list[ConvergenceEntry]] = None
    # Total elapsed time as a formatted string (e.g., "00:01:23.456").Live-computed while Running or Cancelling, stored after completion. Null while Queued.
    elapsed_time: Optional[str] = None
    # Error message if the run failed
    error_message: Optional[str] = None
    # Header describing the analysis type (e.g., "Non-Linear Static Analysis (64-bit)").Available while running (from live progress) and after completion (persisted on run).
    header: Optional[str] = None
    # Static analysis parameters as label→value pairs.Set during analysis initialisation and do not change during execution.e.g., { "Input data:": "4.6 Mb (Mem)", "Degrees of freedom:": "26244", "Load cases:": "55" }Available while running (from live progress) and after completion (persisted on run).
    parameters: Optional[AnalysisRun_parameters] = None
    # Live progress data from the analysis solver.Captured via Windows messages from SGSolver.EXE to the display proxy window.
    progress: Optional[AnalysisProgress] = None
    # Unique identifier for this run
    run_id: Optional[UUID] = None
    # When the run was initiated
    started_at: Optional[datetime.datetime] = None
    # Status of an analysis run through its lifecycle.
    status: Optional[AnalysisRunStatus] = None
    # Warning messages generated during the analysis
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisRun
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisRun()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_progress import AnalysisProgress
        from .analysis_run_parameters import AnalysisRun_parameters
        from .analysis_run_status import AnalysisRunStatus
        from .analysis_type import AnalysisType
        from .convergence_entry import ConvergenceEntry

        from .analysis_progress import AnalysisProgress
        from .analysis_run_parameters import AnalysisRun_parameters
        from .analysis_run_status import AnalysisRunStatus
        from .analysis_type import AnalysisType
        from .convergence_entry import ConvergenceEntry

        fields: dict[str, Callable[[Any], None]] = {
            "analysisType": lambda n : setattr(self, 'analysis_type', n.get_enum_value(AnalysisType)),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "convergenceHistory": lambda n : setattr(self, 'convergence_history', n.get_collection_of_object_values(ConvergenceEntry)),
            "elapsedTime": lambda n : setattr(self, 'elapsed_time', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "header": lambda n : setattr(self, 'header', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_object_value(AnalysisRun_parameters)),
            "progress": lambda n : setattr(self, 'progress', n.get_object_value(AnalysisProgress)),
            "runId": lambda n : setattr(self, 'run_id', n.get_uuid_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AnalysisRunStatus)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("analysisType", self.analysis_type)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_collection_of_object_values("convergenceHistory", self.convergence_history)
        writer.write_str_value("elapsedTime", self.elapsed_time)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_str_value("header", self.header)
        writer.write_object_value("parameters", self.parameters)
        writer.write_object_value("progress", self.progress)
        writer.write_uuid_value("runId", self.run_id)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
    

