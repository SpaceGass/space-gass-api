from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_axes import LoadAxes

@dataclass
class PlatePressureLoadCreate(Parsable):
    """
    DTO for creating a new plate pressure load.
    """
    # Coordinate axes type for distributed loads and plate pressure loads.Maps to SPACE GASS lookup table "L/GI/GP Axes".
    axes: Optional[LoadAxes] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The load case number to create this load in.
    load_case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The plate number to apply this pressure load to.
    plate: Optional[int] = None
    # Pressure in the X direction of the selected axes.
    px: Optional[float] = None
    # Pressure in the Y direction of the selected axes.
    py: Optional[float] = None
    # Pressure in the Z direction of the selected axes.
    pz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlatePressureLoadCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlatePressureLoadCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlatePressureLoadCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .load_axes import LoadAxes

        from .load_axes import LoadAxes

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_enum_value(LoadAxes)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "plate": lambda n : setattr(self, 'plate', n.get_int_value()),
            "px": lambda n : setattr(self, 'px', n.get_float_value()),
            "py": lambda n : setattr(self, 'py', n.get_float_value()),
            "pz": lambda n : setattr(self, 'pz', n.get_float_value()),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("plate", self.plate)
        writer.write_float_value("px", self.px)
        writer.write_float_value("py", self.py)
        writer.write_float_value("pz", self.pz)
    

