from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobHeadingsUpdate(Parsable):
    """
    Write DTO for updating job headings via PATCH /job/headings.Omit a field to leave it unchanged.
    """
    # Designer initials. Omit to leave unchanged.
    designer_initials: Optional[str] = None
    # Job heading. Omit to leave unchanged.
    heading: Optional[str] = None
    # Job notes. Omit to leave unchanged.
    notes: Optional[str] = None
    # Project heading. Omit to leave unchanged.
    project_heading: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobHeadingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobHeadingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobHeadingsUpdate()
    
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
    

