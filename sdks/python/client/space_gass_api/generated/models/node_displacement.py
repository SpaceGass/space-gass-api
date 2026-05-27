from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeDisplacement(Parsable):
    """
    Node displacement result for a specific load case (FileId 203).
    """
    # Load case ID.
    load_case: Optional[int] = None
    # Node key.
    node: Optional[int] = None
    # Rotational X displacement. Unit: Rotation (see GET /job/units).
    rx: Optional[float] = None
    # Rotational Y displacement. Unit: Rotation (see GET /job/units).
    ry: Optional[float] = None
    # Rotational Z displacement. Unit: Rotation (see GET /job/units).
    rz: Optional[float] = None
    # Translational X displacement. Unit: Translation (see GET /job/units).
    tx: Optional[float] = None
    # Translational Y displacement. Unit: Translation (see GET /job/units).
    ty: Optional[float] = None
    # Translational Z displacement. Unit: Translation (see GET /job/units).
    tz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeDisplacement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeDisplacement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeDisplacement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
            "rx": lambda n : setattr(self, 'rx', n.get_float_value()),
            "ry": lambda n : setattr(self, 'ry', n.get_float_value()),
            "rz": lambda n : setattr(self, 'rz', n.get_float_value()),
            "tx": lambda n : setattr(self, 'tx', n.get_float_value()),
            "ty": lambda n : setattr(self, 'ty', n.get_float_value()),
            "tz": lambda n : setattr(self, 'tz', n.get_float_value()),
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
        writer.write_int_value("node", self.node)
        writer.write_float_value("rx", self.rx)
        writer.write_float_value("ry", self.ry)
        writer.write_float_value("rz", self.rz)
        writer.write_float_value("tx", self.tx)
        writer.write_float_value("ty", self.ty)
        writer.write_float_value("tz", self.tz)
    

