from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .axes_type import AxesType

@dataclass
class MemberOffset(Parsable):
    """
    DTO for reading member offset data.Offsets define rigid end zones at each end of a member.This is a sub-resource of Member, not a standalone entity.
    """
    # Coordinate axes type (Local or Global).Maps to SPACE GASS lookup table "L/G Axes".
    axes: Optional[AxesType] = None
    # The member Id this offset applies to.
    member: Optional[int] = None
    # X offset at end A. Unit: Length (see GET /job/units).
    x_offset_at_a: Optional[float] = None
    # X offset at end B. Unit: Length (see GET /job/units).
    x_offset_at_b: Optional[float] = None
    # Y offset at end A. Unit: Length (see GET /job/units).
    y_offset_at_a: Optional[float] = None
    # Y offset at end B. Unit: Length (see GET /job/units).
    y_offset_at_b: Optional[float] = None
    # Z offset at end A. Unit: Length (see GET /job/units).
    z_offset_at_a: Optional[float] = None
    # Z offset at end B. Unit: Length (see GET /job/units).
    z_offset_at_b: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberOffset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberOffset
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberOffset()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .axes_type import AxesType

        from .axes_type import AxesType

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_enum_value(AxesType)),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "xOffsetAtA": lambda n : setattr(self, 'x_offset_at_a', n.get_float_value()),
            "xOffsetAtB": lambda n : setattr(self, 'x_offset_at_b', n.get_float_value()),
            "yOffsetAtA": lambda n : setattr(self, 'y_offset_at_a', n.get_float_value()),
            "yOffsetAtB": lambda n : setattr(self, 'y_offset_at_b', n.get_float_value()),
            "zOffsetAtA": lambda n : setattr(self, 'z_offset_at_a', n.get_float_value()),
            "zOffsetAtB": lambda n : setattr(self, 'z_offset_at_b', n.get_float_value()),
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
        writer.write_enum_value("axes", self.axes)
        writer.write_int_value("member", self.member)
        writer.write_float_value("xOffsetAtA", self.x_offset_at_a)
        writer.write_float_value("xOffsetAtB", self.x_offset_at_b)
        writer.write_float_value("yOffsetAtA", self.y_offset_at_a)
        writer.write_float_value("yOffsetAtB", self.y_offset_at_b)
        writer.write_float_value("zOffsetAtA", self.z_offset_at_a)
        writer.write_float_value("zOffsetAtB", self.z_offset_at_b)
    

