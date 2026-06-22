from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_axes import LoadAxes
    from .load_position_units import LoadPositionUnits

@dataclass
class MemberConcentratedLoad(Parsable):
    """
    DTO for reading a member concentrated load entity.Represents a concentrated force or moment applied at a point along a member.Composite Id: (Case, Member, SubLoad).
    """
    # Coordinate axes type for distributed loads and plate pressure loads.Maps to SPACE GASS lookup table "L/GI/GP Axes".
    axes: Optional[LoadAxes] = None
    # Force in the local/global X direction.
    fx: Optional[float] = None
    # Force in the local/global Y direction.
    fy: Optional[float] = None
    # Force in the local/global Z direction.
    fz: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The load case number this load belongs to.
    load_case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The member number this load is applied to.
    member: Optional[int] = None
    # Moment about the local/global X axis.
    mx: Optional[float] = None
    # Moment about the local/global Y axis.
    my: Optional[float] = None
    # Moment about the local/global Z axis.
    mz: Optional[float] = None
    # Position of the load along the member.
    position: Optional[float] = None
    # Position units for member load placement along a member.Maps to SPACE GASS lookup table "Load Units".
    position_units: Optional[LoadPositionUnits] = None
    # The auto-assigned sub-load number within the member+case combination.
    sub_load: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberConcentratedLoad:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberConcentratedLoad
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberConcentratedLoad()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .load_axes import LoadAxes
        from .load_position_units import LoadPositionUnits

        from .load_axes import LoadAxes
        from .load_position_units import LoadPositionUnits

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_enum_value(LoadAxes)),
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fz": lambda n : setattr(self, 'fz', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "mz": lambda n : setattr(self, 'mz', n.get_float_value()),
            "position": lambda n : setattr(self, 'position', n.get_float_value()),
            "positionUnits": lambda n : setattr(self, 'position_units', n.get_enum_value(LoadPositionUnits)),
            "subLoad": lambda n : setattr(self, 'sub_load', n.get_int_value()),
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
        writer.write_float_value("fx", self.fx)
        writer.write_float_value("fy", self.fy)
        writer.write_float_value("fz", self.fz)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("member", self.member)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("my", self.my)
        writer.write_float_value("mz", self.mz)
        writer.write_float_value("position", self.position)
        writer.write_enum_value("positionUnits", self.position_units)
        writer.write_int_value("subLoad", self.sub_load)
    

