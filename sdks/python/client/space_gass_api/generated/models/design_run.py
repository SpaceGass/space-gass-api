from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .analysis_progress import AnalysisProgress
    from .design_code import DesignCode
    from .design_mode import DesignMode
    from .design_run_phase import DesignRunPhase
    from .run_status import RunStatus

@dataclass
class DesignRun(Parsable):
    """
    Response DTO representing a steel member design run and its current state.Used for the initial 202 response and subsequent status polling; once the runcompletes it also carries the result summary fields (membersChecked,membersFailed, iterations, analysisRerun, sectionsUpdated) — there is noseparate result endpoint. Per-member results are queried viaGET /job/query/design/steel-member/check-summary.
    """
    # Whether the run re-ran an analysis (static or buckling) after updating theanalysis sections, as the design iteration settings direct. Present once theengine has run the design, whether it completed, failed or was cancelledduring it; absent when the run ended before the engine ran it (cancelledbecause the job was replaced, or its settings overrides were rejected).Always false for Check runs.
    analysis_rerun: Optional[bool] = None
    # A design code (standard) a design module checks or designs to. The codes a modulesupports are listed by its codes endpoint, e.g. GET /job/design/steel-member/codes.
    code: Optional[DesignCode] = None
    # When the run finished. Null if still running.
    completed_at: Optional[datetime.datetime] = None
    # Whether steel member design results exist now the run has completed. `true`after a Check run, or a Design run that left the analysis sections as they were:read the checked or selected sections from GET /job/query/design/steel-member/check-summary(`section`). `false` when the run updated the analysis sections to thedesigned sizes without re-running the design, which clears the design results:read the sections from GET /job/structure/members and run the design again tocheck them. Present once the run has completed.
    design_results_available: Optional[bool] = None
    # Execution time as a formatted string (e.g., "00:01:23.456"), from startedAt;the queue wait is not included. Live-computed while Running or Cancelling,stored after completion. Absent while Queued, and for a run cancelled whileit was still queued.
    elapsed_time: Optional[str] = None
    # Why the run failed, or why a queued run was cancelled before it started (forexample the job was closed or replaced first).
    error_message: Optional[str] = None
    # Design/analysis passes performed: the passes so far while the run is Running,the total once it has ended (including a failed or cancelled run). 1 for aCheck run or a design-only run, otherwise the number of section-updatepasses. Absent while Queued, and when the run ended before the engine ranthe design (cancelled because the job was replaced, or its settingsoverrides were rejected).
    iterations: Optional[int] = None
    # Whether a design run verifies the existing sections (Check) or selects newsections (Design). The mode is chosen by the run endpoint (`run-check` /`run-design`), not by a settings field.
    mode: Optional[DesignMode] = None
    # What a steel member design run is doing while it is Running.
    phase: Optional[DesignRunPhase] = None
    # Live progress data from the analysis solver.
    progress: Optional[AnalysisProgress] = None
    # 1-based position among the queued engine operations (analysis and designruns share one queue). Only present while the run is Queued.
    queue_position: Optional[int] = None
    # Unique identifier for this run
    run_id: Optional[UUID] = None
    # Whether the run changed the analysis sections to the designed sizes, whichclears the results that belonged to the old sections. Present once theengine has run the design, whether it completed, failed or was cancelledduring it, so the model change is known whatever the outcome; absent whenthe run ended before the engine ran it (cancelled because the job wasreplaced, or its settings overrides were rejected), which leaves thesections untouched. Always false for Check runs.
    sections_updated: Optional[bool] = None
    # When the run started executing. Absent while Queued, and for a run cancelledwhile it was still queued.
    started_at: Optional[datetime.datetime] = None
    # Status of an engine run (analysis or design) through its lifecycle.
    status: Optional[RunStatus] = None
    # Steel members (design groups) the run checked: one per row ofGET /job/query/design/steel-member/check-summary. Present once the run has completed.
    steel_members_checked: Optional[int] = None
    # Steel members whose check failed — the rows GET /job/query/design/steel-member/check-summaryreturns for `status=Failed`: a load factor below the design settings' loadFactorLimit,or a slenderness or seismic failure. Present once the run has completed.
    steel_members_failed: Optional[int] = None
    # When the run was submitted (and queued)
    submitted_at: Optional[datetime.datetime] = None
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
        from .design_code import DesignCode
        from .design_mode import DesignMode
        from .design_run_phase import DesignRunPhase
        from .run_status import RunStatus

        from .analysis_progress import AnalysisProgress
        from .design_code import DesignCode
        from .design_mode import DesignMode
        from .design_run_phase import DesignRunPhase
        from .run_status import RunStatus

        fields: dict[str, Callable[[Any], None]] = {
            "analysisRerun": lambda n : setattr(self, 'analysis_rerun', n.get_bool_value()),
            "code": lambda n : setattr(self, 'code', n.get_enum_value(DesignCode)),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "designResultsAvailable": lambda n : setattr(self, 'design_results_available', n.get_bool_value()),
            "elapsedTime": lambda n : setattr(self, 'elapsed_time', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(DesignMode)),
            "phase": lambda n : setattr(self, 'phase', n.get_enum_value(DesignRunPhase)),
            "progress": lambda n : setattr(self, 'progress', n.get_object_value(AnalysisProgress)),
            "queuePosition": lambda n : setattr(self, 'queue_position', n.get_int_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_uuid_value()),
            "sectionsUpdated": lambda n : setattr(self, 'sections_updated', n.get_bool_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RunStatus)),
            "steelMembersChecked": lambda n : setattr(self, 'steel_members_checked', n.get_int_value()),
            "steelMembersFailed": lambda n : setattr(self, 'steel_members_failed', n.get_int_value()),
            "submittedAt": lambda n : setattr(self, 'submitted_at', n.get_datetime_value()),
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
        writer.write_bool_value("designResultsAvailable", self.design_results_available)
        writer.write_str_value("elapsedTime", self.elapsed_time)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_int_value("iterations", self.iterations)
        writer.write_enum_value("mode", self.mode)
        writer.write_enum_value("phase", self.phase)
        writer.write_object_value("progress", self.progress)
        writer.write_int_value("queuePosition", self.queue_position)
        writer.write_uuid_value("runId", self.run_id)
        writer.write_bool_value("sectionsUpdated", self.sections_updated)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("steelMembersChecked", self.steel_members_checked)
        writer.write_int_value("steelMembersFailed", self.steel_members_failed)
        writer.write_datetime_value("submittedAt", self.submitted_at)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
    

