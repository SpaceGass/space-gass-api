from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberEndForce(Parsable):
    """
    Member end force results grouped by load case and member.Columnar arrays hold force values at each node (start/end).
    """
    # Final cable length at each node. Unit: Length (see GET /job/units).
    final_cable_length: Optional[list[float]] = None
    # Axial force at each node. Unit: Force (see GET /job/units).
    fx: Optional[list[float]] = None
    # Shear force in Y at each node. Unit: Force (see GET /job/units).
    fy: Optional[list[float]] = None
    # Shear force in Z at each node. Unit: Force (see GET /job/units).
    fz: Optional[list[float]] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Member key.
    member: Optional[int] = None
    # Torsion moment at each node. Unit: Moment (see GET /job/units).
    mx: Optional[list[float]] = None
    # Bending moment about Y at each node. Unit: Moment (see GET /job/units).
    my: Optional[list[float]] = None
    # Bending moment about Z at each node. Unit: Moment (see GET /job/units).
    mz: Optional[list[float]] = None
    # Node keys at start and end of member.
    node: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberEndForce:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberEndForce
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberEndForce()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "finalCableLength": lambda n : setattr(self, 'final_cable_length', n.get_collection_of_primitive_values(float)),
            "fx": lambda n : setattr(self, 'fx', n.get_collection_of_primitive_values(float)),
            "fy": lambda n : setattr(self, 'fy', n.get_collection_of_primitive_values(float)),
            "fz": lambda n : setattr(self, 'fz', n.get_collection_of_primitive_values(float)),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_collection_of_primitive_values(float)),
            "my": lambda n : setattr(self, 'my', n.get_collection_of_primitive_values(float)),
            "mz": lambda n : setattr(self, 'mz', n.get_collection_of_primitive_values(float)),
            "node": lambda n : setattr(self, 'node', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("finalCableLength", self.final_cable_length)
        writer.write_collection_of_primitive_values("fx", self.fx)
        writer.write_collection_of_primitive_values("fy", self.fy)
        writer.write_collection_of_primitive_values("fz", self.fz)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("member", self.member)
        writer.write_collection_of_primitive_values("mx", self.mx)
        writer.write_collection_of_primitive_values("my", self.my)
        writer.write_collection_of_primitive_values("mz", self.mz)
        writer.write_collection_of_primitive_values("node", self.node)
    

