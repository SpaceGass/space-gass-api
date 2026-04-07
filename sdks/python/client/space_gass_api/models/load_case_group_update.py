from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LoadCaseGroupUpdate(Parsable):
    """
    DTO for updating an existing load case group.All fields optional for partial updates.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary key identifying the entity to update.Optional for single updates (key comes from route), required for batch updates.
    key: Optional[int] = None
    # Comma-separated list of load case numbers and ranges (e.g., "1,3,5-10").
    load_case_list: Optional[str] = None
    # Group title.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoadCaseGroupUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoadCaseGroupUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoadCaseGroupUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "loadCaseList": lambda n : setattr(self, 'load_case_list', n.get_str_value()),
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
        writer.write_int_value("key", self.key)
        writer.write_str_value("loadCaseList", self.load_case_list)
        writer.write_str_value("title", self.title)
    

