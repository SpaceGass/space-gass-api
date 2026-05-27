from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ModeShape(Parsable):
    """
    Dynamic mode shape results grouped by load case and mode (FileId 219).Columnar arrays hold displacement values at each node.
    """
    # Load case ID.
    load_case: Optional[int] = None
    # Mode number.
    mode: Optional[int] = None
    # Node keys.
    node: Optional[list[int]] = None
    # Rotational X displacement at each node. Unit: Rotation (see GET /job/units).
    rx: Optional[list[float]] = None
    # Rotational Y displacement at each node. Unit: Rotation (see GET /job/units).
    ry: Optional[list[float]] = None
    # Rotational Z displacement at each node. Unit: Rotation (see GET /job/units).
    rz: Optional[list[float]] = None
    # Translational X displacement at each node. Unit: Translation (see GET /job/units).
    tx: Optional[list[float]] = None
    # Translational Y displacement at each node. Unit: Translation (see GET /job/units).
    ty: Optional[list[float]] = None
    # Translational Z displacement at each node. Unit: Translation (see GET /job/units).
    tz: Optional[list[float]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModeShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModeShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModeShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
            "node": lambda n : setattr(self, 'node', n.get_collection_of_primitive_values(int)),
            "rx": lambda n : setattr(self, 'rx', n.get_collection_of_primitive_values(float)),
            "ry": lambda n : setattr(self, 'ry', n.get_collection_of_primitive_values(float)),
            "rz": lambda n : setattr(self, 'rz', n.get_collection_of_primitive_values(float)),
            "tx": lambda n : setattr(self, 'tx', n.get_collection_of_primitive_values(float)),
            "ty": lambda n : setattr(self, 'ty', n.get_collection_of_primitive_values(float)),
            "tz": lambda n : setattr(self, 'tz', n.get_collection_of_primitive_values(float)),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("mode", self.mode)
        writer.write_collection_of_primitive_values("node", self.node)
        writer.write_collection_of_primitive_values("rx", self.rx)
        writer.write_collection_of_primitive_values("ry", self.ry)
        writer.write_collection_of_primitive_values("rz", self.rz)
        writer.write_collection_of_primitive_values("tx", self.tx)
        writer.write_collection_of_primitive_values("ty", self.ty)
        writer.write_collection_of_primitive_values("tz", self.tz)
    

