from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .analysis_progress import AnalysisProgress
    from .analysis_run_status import AnalysisRunStatus
    from .steel_design_code import SteelDesignCode
    from .steel_design_mode import SteelDesignMode

@dataclass
class DesignRun(Parsable):
    """
    Response DTO representing a steel member design run and its current state.Used for the initial 202 response and subsequent status polling; once the runcompletes it also carries the result summary fields (membersChecked,membersFailed, iterations, analysisRerun) — there is no separate resultendpoint. Per-member results are queried viaGET /job/query/design/steel-member/check-summary.
    """
    # Whether the run re-ran an analysis (static or buckling) after updating theanalysis sections, as the design iteration settings direct. Present oncethe run has ended, including a failed or cancelled run. Always false for Check runs.
    analysis_rerun: Optional[bool] = None
    # Steel member design code used to check or design steel members.
    code: Optional[SteelDesignCode] = None
    # When the run finished. Null if still running.
    completed_at: Optional[datetime.datetime] = None
    # Total elapsed time as a formatted string (e.g., "00:01:23.456").Live-computed while Running or Cancelling, stored after completion. Null while Queued.
    elapsed_time: Optional[str] = None
    # Why the run failed, or why a queued run was cancelled without starting (forexample the job was closed or replaced first).
    error_message: Optional[str] = None
    # Design/analysis passes performed: 1 for a Check run or a design-only run,otherwise the number of section-update passes. Present once the run hasended, including a failed or cancelled run.
    iterations: Optional[int] = None
    # Members checked by the run. Present once the run has completed.
    members_checked: Optional[int] = None
    # Members whose design check failed. Present once the run has completed.
    members_failed: Optional[int] = None
    # Whether a steel member design run verifies the existing sections (Check)or selects new sections (Design).
    mode: Optional[SteelDesignMode] = None
    # Live progress data from the analysis solver.
    progress: Optional[AnalysisProgress] = None
    # 1-based position among the queued engine operations (analysis and designruns share one queue). Only present while the run is Queued.
    queue_position: Optional[int] = None
    # Unique identifier for this run
    run_id: Optional[UUID] = None
    # Whether the run changed the analysis sections to the designed sizes, whichclears the results that belonged to the old sections. Present once the runhas ended, including a failed or cancelled run, so the model change isknown whatever the outcome. Always false for Check runs.
    sections_updated: Optional[bool] = None
    # When the run was initiated
    started_at: Optional[datetime.datetime] = None
    # Status of an analysis run through its lifecycle.
    status: Optional[AnalysisRunStatus] = None
    # Warning messages generated during the run
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DesignRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DesignRun
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DesignRun()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_progress import AnalysisProgress
        from .analysis_run_status import AnalysisRunStatus
        from .steel_design_code import SteelDesignCode
        from .steel_design_mode import SteelDesignMode

        from .analysis_progress import AnalysisProgress
        from .analysis_run_status import AnalysisRunStatus
        from .steel_design_code import SteelDesignCode
        from .steel_design_mode import SteelDesignMode

        fields: dict[str, Callable[[Any], None]] = {
            "analysisRerun": lambda n : setattr(self, 'analysis_rerun', n.get_bool_value()),
            "code": lambda n : setattr(self, 'code', n.get_enum_value(SteelDesignCode)),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "elapsedTime": lambda n : setattr(self, 'elapsed_time', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "membersChecked": lambda n : setattr(self, 'members_checked', n.get_int_value()),
            "membersFailed": lambda n : setattr(self, 'members_failed', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(SteelDesignMode)),
            "progress": lambda n : setattr(self, 'progress', n.get_object_value(AnalysisProgress)),
            "queuePosition": lambda n : setattr(self, 'queue_position', n.get_int_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_uuid_value()),
            "sectionsUpdated": lambda n : setattr(self, 'sections_updated', n.get_bool_value()),
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
        writer.write_bool_value("analysisRerun", self.analysis_rerun)
        writer.write_enum_value("code", self.code)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("elapsedTime", self.elapsed_time)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_int_value("iterations", self.iterations)
        writer.write_int_value("membersChecked", self.members_checked)
        writer.write_int_value("membersFailed", self.members_failed)
        writer.write_enum_value("mode", self.mode)
        writer.write_object_value("progress", self.progress)
        writer.write_int_value("queuePosition", self.queue_position)
        writer.write_uuid_value("runId", self.run_id)
        writer.write_bool_value("sectionsUpdated", self.sections_updated)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
    

