from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analysis_load_case_progress import AnalysisLoadCaseProgress
    from .analysis_log_message import AnalysisLogMessage

@dataclass
class AnalysisProgress(Parsable):
    """
    Live progress data from the analysis solver.Captured via Windows messages from SGSolver.EXE to the display proxy window.
    """
    # Current step being processed (0-based index)
    current_step: Optional[int] = None
    # Iteration progress percentage (0-100) for the current solver iteration
    iteration_percentage: Optional[int] = None
    # Load case progress information
    load_case_count: Optional[AnalysisLoadCaseProgress] = None
    # Live load case status string, updated as load cases are processed.e.g., starts as "55" then becomes "40 (29/55)" during analysis.Null if no load case information is available.
    load_case_status: Optional[str] = None
    # Log messages from the solver (info, warnings, errors).Includes error/warning messages (from negative textIndex) and completion info.
    messages: Optional[list[AnalysisLogMessage]] = None
    # Current status text from the solver (e.g., "Analysing..", "Saving results..")
    status_text: Optional[str] = None
    # Per-step labels/names (e.g., "Assembling geometric data", "Solving stiffness matrix").Array index corresponds to step index. Null entries mean no label received yet.
    step_labels: Optional[list[str]] = None
    # Per-step percentage completion. Array index corresponds to step index.
    step_percentages: Optional[list[int]] = None
    # Total number of analysis steps/phases discovered so far.Inferred dynamically from solver messages (the solver does not declare total steps upfront).
    total_steps: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisProgress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisProgress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_load_case_progress import AnalysisLoadCaseProgress
        from .analysis_log_message import AnalysisLogMessage

        from .analysis_load_case_progress import AnalysisLoadCaseProgress
        from .analysis_log_message import AnalysisLogMessage

        fields: dict[str, Callable[[Any], None]] = {
            "currentStep": lambda n : setattr(self, 'current_step', n.get_int_value()),
            "iterationPercentage": lambda n : setattr(self, 'iteration_percentage', n.get_int_value()),
            "loadCaseCount": lambda n : setattr(self, 'load_case_count', n.get_object_value(AnalysisLoadCaseProgress)),
            "loadCaseStatus": lambda n : setattr(self, 'load_case_status', n.get_str_value()),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(AnalysisLogMessage)),
            "statusText": lambda n : setattr(self, 'status_text', n.get_str_value()),
            "stepLabels": lambda n : setattr(self, 'step_labels', n.get_collection_of_primitive_values(str)),
            "stepPercentages": lambda n : setattr(self, 'step_percentages', n.get_collection_of_primitive_values(int)),
            "totalSteps": lambda n : setattr(self, 'total_steps', n.get_int_value()),
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
        writer.write_int_value("currentStep", self.current_step)
        writer.write_int_value("iterationPercentage", self.iteration_percentage)
        writer.write_object_value("loadCaseCount", self.load_case_count)
        writer.write_str_value("loadCaseStatus", self.load_case_status)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_str_value("statusText", self.status_text)
        writer.write_collection_of_primitive_values("stepLabels", self.step_labels)
        writer.write_collection_of_primitive_values("stepPercentages", self.step_percentages)
        writer.write_int_value("totalSteps", self.total_steps)
    

