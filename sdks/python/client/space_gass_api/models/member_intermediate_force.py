from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberIntermediateForce(Parsable):
    """
    Member intermediate force results grouped by load case and member.Columnar arrays hold force values at each station along the member.
    """
    # Load case ID.
    case: Optional[int] = None
    # Axial force at each station. Unit: Force (see GET /job/units).
    fx: Optional[list[float]] = None
    # Shear force in Y at each station. Unit: Force (see GET /job/units).
    fy: Optional[list[float]] = None
    # Shear force in Z at each station. Unit: Force (see GET /job/units).
    fz: Optional[list[float]] = None
    # Distance along member at each station. Unit: Length (see GET /job/units).
    location: Optional[list[float]] = None
    # Member key.
    member: Optional[int] = None
    # Torsion moment at each station. Unit: Moment (see GET /job/units).
    mx: Optional[list[float]] = None
    # Bending moment about Y at each station. Unit: Moment (see GET /job/units).
    my: Optional[list[float]] = None
    # Bending moment about Z at each station. Unit: Moment (see GET /job/units).
    mz: Optional[list[float]] = None
    # Station index at each output point.
    station: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberIntermediateForce:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberIntermediateForce
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberIntermediateForce()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "fx": lambda n : setattr(self, 'fx', n.get_collection_of_primitive_values(float)),
            "fy": lambda n : setattr(self, 'fy', n.get_collection_of_primitive_values(float)),
            "fz": lambda n : setattr(self, 'fz', n.get_collection_of_primitive_values(float)),
            "location": lambda n : setattr(self, 'location', n.get_collection_of_primitive_values(float)),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_collection_of_primitive_values(float)),
            "my": lambda n : setattr(self, 'my', n.get_collection_of_primitive_values(float)),
            "mz": lambda n : setattr(self, 'mz', n.get_collection_of_primitive_values(float)),
            "station": lambda n : setattr(self, 'station', n.get_collection_of_primitive_values(int)),
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
        writer.write_int_value("case", self.case)
        writer.write_collection_of_primitive_values("fx", self.fx)
        writer.write_collection_of_primitive_values("fy", self.fy)
        writer.write_collection_of_primitive_values("fz", self.fz)
        writer.write_collection_of_primitive_values("location", self.location)
        writer.write_int_value("member", self.member)
        writer.write_collection_of_primitive_values("mx", self.mx)
        writer.write_collection_of_primitive_values("my", self.my)
        writer.write_collection_of_primitive_values("mz", self.mz)
        writer.write_collection_of_primitive_values("station", self.station)
    

