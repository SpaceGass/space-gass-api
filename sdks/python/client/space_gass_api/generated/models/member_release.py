from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberRelease(Parsable):
    """
    DTO for reading member release data.Releases define fixity codes and spring stiffness at each end of a member.Always present on every member, so the owning member Idis not duplicated here — the parent MemberDto's `id` is authoritative whenreturned inline, and the route parameter is authoritative on the standalone endpoint.
    """
    # Fixity code at end A of the member.
    fixity_code_at_a: Optional[str] = None
    # Fixity code at end B of the member.
    fixity_code_at_b: Optional[str] = None
    # Rotational X spring stiffness at end A. Unit: Moment/Radian (see GET /job/units).
    rx_stiffness_at_a: Optional[float] = None
    # Rotational X spring stiffness at end B. Unit: Moment/Radian (see GET /job/units).
    rx_stiffness_at_b: Optional[float] = None
    # Rotational Y spring stiffness at end A. Unit: Moment/Radian (see GET /job/units).
    ry_stiffness_at_a: Optional[float] = None
    # Rotational Y spring stiffness at end B. Unit: Moment/Radian (see GET /job/units).
    ry_stiffness_at_b: Optional[float] = None
    # Rotational Z spring stiffness at end A. Unit: Moment/Radian (see GET /job/units).
    rz_stiffness_at_a: Optional[float] = None
    # Rotational Z spring stiffness at end B. Unit: Moment/Radian (see GET /job/units).
    rz_stiffness_at_b: Optional[float] = None
    # Translational X spring stiffness at end A. Unit: Force/Length (see GET /job/units).
    tx_stiffness_at_a: Optional[float] = None
    # Translational X spring stiffness at end B. Unit: Force/Length (see GET /job/units).
    tx_stiffness_at_b: Optional[float] = None
    # Translational Y spring stiffness at end A. Unit: Force/Length (see GET /job/units).
    ty_stiffness_at_a: Optional[float] = None
    # Translational Y spring stiffness at end B. Unit: Force/Length (see GET /job/units).
    ty_stiffness_at_b: Optional[float] = None
    # Translational Z spring stiffness at end A. Unit: Force/Length (see GET /job/units).
    tz_stiffness_at_a: Optional[float] = None
    # Translational Z spring stiffness at end B. Unit: Force/Length (see GET /job/units).
    tz_stiffness_at_b: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberRelease:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberRelease
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberRelease()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fixityCodeAtA": lambda n : setattr(self, 'fixity_code_at_a', n.get_str_value()),
            "fixityCodeAtB": lambda n : setattr(self, 'fixity_code_at_b', n.get_str_value()),
            "rxStiffnessAtA": lambda n : setattr(self, 'rx_stiffness_at_a', n.get_float_value()),
            "rxStiffnessAtB": lambda n : setattr(self, 'rx_stiffness_at_b', n.get_float_value()),
            "ryStiffnessAtA": lambda n : setattr(self, 'ry_stiffness_at_a', n.get_float_value()),
            "ryStiffnessAtB": lambda n : setattr(self, 'ry_stiffness_at_b', n.get_float_value()),
            "rzStiffnessAtA": lambda n : setattr(self, 'rz_stiffness_at_a', n.get_float_value()),
            "rzStiffnessAtB": lambda n : setattr(self, 'rz_stiffness_at_b', n.get_float_value()),
            "txStiffnessAtA": lambda n : setattr(self, 'tx_stiffness_at_a', n.get_float_value()),
            "txStiffnessAtB": lambda n : setattr(self, 'tx_stiffness_at_b', n.get_float_value()),
            "tyStiffnessAtA": lambda n : setattr(self, 'ty_stiffness_at_a', n.get_float_value()),
            "tyStiffnessAtB": lambda n : setattr(self, 'ty_stiffness_at_b', n.get_float_value()),
            "tzStiffnessAtA": lambda n : setattr(self, 'tz_stiffness_at_a', n.get_float_value()),
            "tzStiffnessAtB": lambda n : setattr(self, 'tz_stiffness_at_b', n.get_float_value()),
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
        writer.write_str_value("fixityCodeAtA", self.fixity_code_at_a)
        writer.write_str_value("fixityCodeAtB", self.fixity_code_at_b)
        writer.write_float_value("rxStiffnessAtA", self.rx_stiffness_at_a)
        writer.write_float_value("rxStiffnessAtB", self.rx_stiffness_at_b)
        writer.write_float_value("ryStiffnessAtA", self.ry_stiffness_at_a)
        writer.write_float_value("ryStiffnessAtB", self.ry_stiffness_at_b)
        writer.write_float_value("rzStiffnessAtA", self.rz_stiffness_at_a)
        writer.write_float_value("rzStiffnessAtB", self.rz_stiffness_at_b)
        writer.write_float_value("txStiffnessAtA", self.tx_stiffness_at_a)
        writer.write_float_value("txStiffnessAtB", self.tx_stiffness_at_b)
        writer.write_float_value("tyStiffnessAtA", self.ty_stiffness_at_a)
        writer.write_float_value("tyStiffnessAtB", self.ty_stiffness_at_b)
        writer.write_float_value("tzStiffnessAtA", self.tz_stiffness_at_a)
        writer.write_float_value("tzStiffnessAtB", self.tz_stiffness_at_b)
    

