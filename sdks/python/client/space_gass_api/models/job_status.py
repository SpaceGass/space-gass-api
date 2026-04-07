from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_details import JobDetails
    from .job_state import JobState
    from .model_summary import ModelSummary

@dataclass
class JobStatus(Parsable):
    """
    Full job status response including details, state, and model summary.Returned by lifecycle operations (new, open, save, status) and GET /job/status.
    """
    # Read DTO for job details (text properties).
    details: Optional[JobDetails] = None
    # Summary counts of all model entities in the current job.Counts are read from file headers (lightweight, no datasheet loading).
    model: Optional[ModelSummary] = None
    # Current session/file state of the job.
    state: Optional[JobState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_details import JobDetails
        from .job_state import JobState
        from .model_summary import ModelSummary

        from .job_details import JobDetails
        from .job_state import JobState
        from .model_summary import ModelSummary

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(JobDetails)),
            "model": lambda n : setattr(self, 'model', n.get_object_value(ModelSummary)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(JobState)),
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
        writer.write_object_value("details", self.details)
        writer.write_object_value("model", self.model)
        writer.write_object_value("state", self.state)
    

