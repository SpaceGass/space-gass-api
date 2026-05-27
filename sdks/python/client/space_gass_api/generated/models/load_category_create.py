from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LoadCategoryCreate(Parsable):
    """
    DTO for creating a new load category.Read-only fields (Source, Version, Username) are excluded.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # Notes (supports multi-line text).
    notes: Optional[str] = None
    # Category title.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoadCategoryCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoadCategoryCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoadCategoryCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("title", self.title)
    

