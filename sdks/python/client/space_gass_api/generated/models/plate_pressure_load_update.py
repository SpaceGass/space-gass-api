from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .load_axes import LoadAxes

@dataclass
class PlatePressureLoadUpdate(Parsable):
    """
    DTO for updating an existing plate pressure load.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # Coordinate axes type for distributed loads and plate pressure loads.Maps to SPACE GASS lookup table "L/GI/GP Axes".
    axes: Optional[LoadAxes] = None
    # The load case number.
    case: Optional[int] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The plate number.
    plate: Optional[int] = None
    # Pressure in the X direction of the selected axes.
    px: Optional[float] = None
    # Pressure in the Y direction of the selected axes.
    py: Optional[float] = None
    # Pressure in the Z direction of the selected axes.
    pz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlatePressureLoadUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlatePressureLoadUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlatePressureLoadUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .load_axes import LoadAxes

        from .load_axes import LoadAxes

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_enum_value(LoadAxes)),
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
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
        writer.write_int_value("case", self.case)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("plate", self.plate)
        writer.write_float_value("px", self.px)
        writer.write_float_value("py", self.py)
        writer.write_float_value("pz", self.pz)
    

