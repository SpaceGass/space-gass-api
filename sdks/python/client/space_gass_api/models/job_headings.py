from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobHeadings(Parsable):
    """
    Read DTO for job headings (text properties).
    """
    # Designer initials
    designer_initials: Optional[str] = None
    # Job heading
    heading: Optional[str] = None
    # Job notes
    notes: Optional[str] = None
    # Project heading
    project_heading: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobHeadings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobHeadings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobHeadings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "designerInitials": lambda n : setattr(self, 'designer_initials', n.get_str_value()),
            "heading": lambda n : setattr(self, 'heading', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "projectHeading": lambda n : setattr(self, 'project_heading', n.get_str_value()),
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
        writer.write_str_value("designerInitials", self.designer_initials)
        writer.write_str_value("heading", self.heading)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("projectHeading", self.project_heading)
    

