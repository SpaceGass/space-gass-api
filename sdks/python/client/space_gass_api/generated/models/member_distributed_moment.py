from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_axes import LoadAxes
    from .load_position_units import LoadPositionUnits

@dataclass
class MemberDistributedMoment(Parsable):
    """
    DTO for reading a member distributed moment entity.Represents distributed moments applied along a member.Composite Id: (Case, Member, SubLoad).
    """
    # Coordinate axes type for distributed loads and plate pressure loads.Maps to SPACE GASS lookup table "L/GI/GP Axes".
    axes: Optional[LoadAxes] = None
    # Finish position of the distributed moment along the member.
    finish_position: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The load case number this load belongs to.
    load_case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The member number this load is applied to.
    member: Optional[int] = None
    # Distributed moment intensity about X axis at the finish position.
    mx_finish: Optional[float] = None
    # Distributed moment intensity about X axis at the start position.
    mx_start: Optional[float] = None
    # Distributed moment intensity about Y axis at the finish position.
    my_finish: Optional[float] = None
    # Distributed moment intensity about Y axis at the start position.
    my_start: Optional[float] = None
    # Distributed moment intensity about Z axis at the finish position.
    mz_finish: Optional[float] = None
    # Distributed moment intensity about Z axis at the start position.
    mz_start: Optional[float] = None
    # Position units for member load placement along a member.Maps to SPACE GASS lookup table "Load Units".
    position_units: Optional[LoadPositionUnits] = None
    # Start position of the distributed moment along the member.
    start_position: Optional[float] = None
    # The auto-assigned sub-load number within the member+case combination.
    sub_load: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberDistributedMoment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberDistributedMoment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberDistributedMoment()
    
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
            "finishPosition": lambda n : setattr(self, 'finish_position', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mxFinish": lambda n : setattr(self, 'mx_finish', n.get_float_value()),
            "mxStart": lambda n : setattr(self, 'mx_start', n.get_float_value()),
            "myFinish": lambda n : setattr(self, 'my_finish', n.get_float_value()),
            "myStart": lambda n : setattr(self, 'my_start', n.get_float_value()),
            "mzFinish": lambda n : setattr(self, 'mz_finish', n.get_float_value()),
            "mzStart": lambda n : setattr(self, 'mz_start', n.get_float_value()),
            "positionUnits": lambda n : setattr(self, 'position_units', n.get_enum_value(LoadPositionUnits)),
            "startPosition": lambda n : setattr(self, 'start_position', n.get_float_value()),
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
        writer.write_float_value("finishPosition", self.finish_position)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("member", self.member)
        writer.write_float_value("mxFinish", self.mx_finish)
        writer.write_float_value("mxStart", self.mx_start)
        writer.write_float_value("myFinish", self.my_finish)
        writer.write_float_value("myStart", self.my_start)
        writer.write_float_value("mzFinish", self.mz_finish)
        writer.write_float_value("mzStart", self.mz_start)
        writer.write_enum_value("positionUnits", self.position_units)
        writer.write_float_value("startPosition", self.start_position)
        writer.write_int_value("subLoad", self.sub_load)
    

