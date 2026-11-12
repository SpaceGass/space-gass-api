from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_axes import LoadAxes
    from .load_position_units import LoadPositionUnits

@dataclass
class MemberDistributedMomentUpdate(Parsable):
    """
    DTO for updating an existing member distributed moment (a distributed torsion about the member's local X axis).Only fields included in the request are updated; omit a field to keep its current value.
    """
    # Coordinate axes type for distributed loads and plate pressure loads.Maps to SPACE GASS lookup table "L/GI/GP Axes".
    axes: Optional[LoadAxes] = None
    # Finish position of the distributed moment along the member.
    finish_position: Optional[float] = None
    # The load case number.
    load_case: Optional[int] = None
    # Id of a load category (GET /job/loads/load-categories). Send 0 to clear the category; omit to keep the current one.
    load_category: Optional[int] = None
    # The member number.
    member: Optional[int] = None
    # Distributed torsion (moment about the member X axis) at the finish position.
    mx_finish: Optional[float] = None
    # Distributed torsion (moment about the member X axis) at the start position.
    mx_start: Optional[float] = None
    # Position units for member load placement along a member.Maps to SPACE GASS lookup table "Load Units".
    position_units: Optional[LoadPositionUnits] = None
    # Start position of the distributed moment along the member.
    start_position: Optional[float] = None
    # The sub-load number.
    sub_load: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberDistributedMomentUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberDistributedMomentUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberDistributedMomentUpdate()
    
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
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mxFinish": lambda n : setattr(self, 'mx_finish', n.get_float_value()),
            "mxStart": lambda n : setattr(self, 'mx_start', n.get_float_value()),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("member", self.member)
        writer.write_float_value("mxFinish", self.mx_finish)
        writer.write_float_value("mxStart", self.mx_start)
        writer.write_enum_value("positionUnits", self.position_units)
        writer.write_float_value("startPosition", self.start_position)
        writer.write_int_value("subLoad", self.sub_load)
    

