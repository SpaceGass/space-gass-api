from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_force_access_option import JobForceAccessOption

@dataclass
class OpenJobRequest(Parsable):
    """
    Request DTO for opening a job file.
    """
    # Full path to the .sg job file to open.
    file_path: Optional[str] = None
    # Options for forcing access to a job file that is in a locked or unsaved state.Used when temporary files exist from a previous session that was not properly closed.
    force_option: Optional[JobForceAccessOption] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenJobRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenJobRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenJobRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_force_access_option import JobForceAccessOption

        from .job_force_access_option import JobForceAccessOption

        fields: dict[str, Callable[[Any], None]] = {
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "forceOption": lambda n : setattr(self, 'force_option', n.get_enum_value(JobForceAccessOption)),
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
        writer.write_str_value("filePath", self.file_path)
        writer.write_enum_value("forceOption", self.force_option)
    

