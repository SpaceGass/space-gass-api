from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeReaction(Parsable):
    """
    Node reaction result for a specific load case (FileId 205).
    """
    # Reaction force in X direction. Unit: Force (see GET /job/units).
    fx: Optional[float] = None
    # Reaction force in Y direction. Unit: Force (see GET /job/units).
    fy: Optional[float] = None
    # Reaction force in Z direction. Unit: Force (see GET /job/units).
    fz: Optional[float] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Reaction moment about X axis. Unit: Moment (see GET /job/units).
    mx: Optional[float] = None
    # Reaction moment about Y axis. Unit: Moment (see GET /job/units).
    my: Optional[float] = None
    # Reaction moment about Z axis. Unit: Moment (see GET /job/units).
    mz: Optional[float] = None
    # Node key.
    node: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeReaction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeReaction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fz": lambda n : setattr(self, 'fz', n.get_float_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "mz": lambda n : setattr(self, 'mz', n.get_float_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
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
        writer.write_float_value("fx", self.fx)
        writer.write_float_value("fy", self.fy)
        writer.write_float_value("fz", self.fz)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("my", self.my)
        writer.write_float_value("mz", self.mz)
        writer.write_int_value("node", self.node)
    

