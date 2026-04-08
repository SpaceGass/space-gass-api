from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_case_type import LoadCaseType

@dataclass
class LoadCase(Parsable):
    """
    DTO for a load case (from Loads - Titles table, FileID=28).Returns all load cases including primary, combination, and step types.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary key - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    key: Optional[int] = None
    # Load case notes (supports multi-line text).
    notes: Optional[str] = None
    # Load case title.
    title: Optional[str] = None
    # Type of load case in the structural model.Read-only — computed internally by SPACE GASS based on assigned loads.
    type: Optional[LoadCaseType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoadCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoadCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoadCase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .load_case_type import LoadCaseType

        from .load_case_type import LoadCaseType

        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(LoadCaseType)),
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
        writer.write_int_value("key", self.key)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("title", self.title)
        writer.write_enum_value("type", self.type)
    

