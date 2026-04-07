from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_file_source import JobFileSource

@dataclass
class JobFile(Parsable):
    """
    File information for the current job.
    """
    # File name only (e.g. "Bridge_Design_v2.sg").
    name: Optional[str] = None
    # Full file path (e.g. "C:/Projects/Bridge_Design_v2.sg").
    path: Optional[str] = None
    # Enum representing the source of a job file
    source: Optional[JobFileSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_file_source import JobFileSource

        from .job_file_source import JobFileSource

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(JobFileSource)),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("path", self.path)
        writer.write_enum_value("source", self.source)
    

