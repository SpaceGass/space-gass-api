from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_details import JobDetails

@dataclass
class Job(Parsable):
    """
    Read DTO for job responses.Model counts are available via GET /job/status (JobStatusDto).Sub-resources (units, details) are managed via their own endpoints.
    """
    # Read DTO for job details (text properties).
    details: Optional[JobDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Job:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Job
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Job()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_details import JobDetails

        from .job_details import JobDetails

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(JobDetails)),
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
    

