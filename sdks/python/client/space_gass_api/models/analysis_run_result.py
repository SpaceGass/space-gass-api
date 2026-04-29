from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .analysis_run_status import AnalysisRunStatus
    from .analysis_type import AnalysisType
    from .convergence_entry import ConvergenceEntry

@dataclass
class AnalysisRunResult(Parsable):
    """
    Result summary DTO returned once an analysis run completes.For actual analysis result data, use the query endpoints(e.g., /api/v1/job/query/analysis/static/node/reactions).
    """
    # SPACEGASS analysis types. Values map to the SPACEGASS internal SGAnalysisType IDs.
    analysis_type: Optional[AnalysisType] = None
    # Convergence history from non-linear analysis iterations.Null for linear analyses or if no convergence was recorded.
    convergence_history: Optional[list[ConvergenceEntry]] = None
    # Total elapsed time as a formatted string
    elapsed_time: Optional[str] = None
    # Error message if the run failed
    error_message: Optional[str] = None
    # Unique identifier for this run
    run_id: Optional[UUID] = None
    # Status of an analysis run through its lifecycle.
    status: Optional[AnalysisRunStatus] = None
    # Warning messages generated during the analysis
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalysisRunResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalysisRunResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalysisRunResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analysis_run_status import AnalysisRunStatus
        from .analysis_type import AnalysisType
        from .convergence_entry import ConvergenceEntry

        from .analysis_run_status import AnalysisRunStatus
        from .analysis_type import AnalysisType
        from .convergence_entry import ConvergenceEntry

        fields: dict[str, Callable[[Any], None]] = {
            "analysisType": lambda n : setattr(self, 'analysis_type', n.get_enum_value(AnalysisType)),
            "convergenceHistory": lambda n : setattr(self, 'convergence_history', n.get_collection_of_object_values(ConvergenceEntry)),
            "elapsedTime": lambda n : setattr(self, 'elapsed_time', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_uuid_value()),
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
        writer.write_collection_of_object_values("convergenceHistory", self.convergence_history)
        writer.write_str_value("elapsedTime", self.elapsed_time)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_uuid_value("runId", self.run_id)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
    

