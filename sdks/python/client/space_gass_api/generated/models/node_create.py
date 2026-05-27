from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeCreate(Parsable):
    """
    DTO for creating a new nodeNode number may be auto-assigned if not provided
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # X coordinate. Unit: Length (see GET /job/units).
    x: Optional[float] = None
    # Y coordinate. Unit: Length (see GET /job/units).
    y: Optional[float] = None
    # Z coordinate. Unit: Length (see GET /job/units).
    z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "x": lambda n : setattr(self, 'x', n.get_float_value()),
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
            "z": lambda n : setattr(self, 'z', n.get_float_value()),
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
        writer.write_float_value("x", self.x)
        writer.write_float_value("y", self.y)
        writer.write_float_value("z", self.z)
    

