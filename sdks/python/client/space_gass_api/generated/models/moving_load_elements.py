from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadElements(Parsable):
    """
    The structural elements that moving loads are applied to — the selected members andplates. Both are SG list-strings (comma-separated Ids and ranges, e.g. `"1,3-7,10"`).
    """
    # The members selected to receive moving loads, in SG list-string format.
    members: Optional[str] = None
    # The plates selected to receive moving loads, in SG list-string format.
    plates: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadElements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadElements
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadElements()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_str_value()),
            "plates": lambda n : setattr(self, 'plates', n.get_str_value()),
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
        writer.write_str_value("members", self.members)
        writer.write_str_value("plates", self.plates)
    

