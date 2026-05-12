from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_headings import JobHeadings
    from .job_settings import JobSettings
    from .units import Units

@dataclass
class Job(Parsable):
    """
    Read DTO for job responses.Model counts and file state are available via GET /job/status (JobStatusDto).
    """
    # Read DTO for job headings (text properties).
    headings: Optional[JobHeadings] = None
    # Read DTO for job-level settings.Groups configuration properties that apply to the job as a whole.
    settings: Optional[JobSettings] = None
    # Unit settings for the current job.
    units: Optional[Units] = None
    
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
        from .job_headings import JobHeadings
        from .job_settings import JobSettings
        from .units import Units

        from .job_headings import JobHeadings
        from .job_settings import JobSettings
        from .units import Units

        fields: dict[str, Callable[[Any], None]] = {
            "headings": lambda n : setattr(self, 'headings', n.get_object_value(JobHeadings)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(JobSettings)),
            "units": lambda n : setattr(self, 'units', n.get_object_value(Units)),
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
        writer.write_object_value("headings", self.headings)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("units", self.units)
    

