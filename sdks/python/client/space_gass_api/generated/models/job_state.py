from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_file import JobFile

@dataclass
class JobState(Parsable):
    """
    Current session/file state of the job.
    """
    # File information for the current job.
    file: Optional[JobFile] = None
    # Whether the job has unsaved modifications.
    is_modified: Optional[bool] = None
    # Whether this is a new job that has never been saved.If true, provide a filePath when calling POST /save.
    is_new: Optional[bool] = None
    # Whether a job is currently loaded in memory.
    is_open: Optional[bool] = None
    # When the job was opened (null if not open).
    opened_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_file import JobFile

        from .job_file import JobFile

        fields: dict[str, Callable[[Any], None]] = {
            "file": lambda n : setattr(self, 'file', n.get_object_value(JobFile)),
            "isModified": lambda n : setattr(self, 'is_modified', n.get_bool_value()),
            "isNew": lambda n : setattr(self, 'is_new', n.get_bool_value()),
            "isOpen": lambda n : setattr(self, 'is_open', n.get_bool_value()),
            "openedAt": lambda n : setattr(self, 'opened_at', n.get_datetime_value()),
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
        writer.write_object_value("file", self.file)
        writer.write_bool_value("isModified", self.is_modified)
        writer.write_bool_value("isNew", self.is_new)
        writer.write_bool_value("isOpen", self.is_open)
        writer.write_datetime_value("openedAt", self.opened_at)
    

