from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .thermal_element_type import ThermalElementType

@dataclass
class ThermalLoadCreate(Parsable):
    """
    DTO for creating a new thermal load.Specify the element type to target either a member or a plate element.
    """
    # The load case number to create this load in.
    case: Optional[int] = None
    # Element type discriminator for thermal loads.Determines whether a thermal load applies to a member or plate element.Maps to SPACE GASS lookup table "Element Type".
    element_type: Optional[ThermalElementType] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The key of the element to apply this load to (member number or plate number, depending on ElementType).
    key: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The uniform temperature change applied to the element.
    thermal_load: Optional[float] = None
    # The thermal gradient about the local Y axis.
    y_thermal_gradient: Optional[float] = None
    # The thermal gradient about the local Z axis.
    z_thermal_gradient: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThermalLoadCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThermalLoadCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThermalLoadCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .thermal_element_type import ThermalElementType

        from .thermal_element_type import ThermalElementType

        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "elementType": lambda n : setattr(self, 'element_type', n.get_enum_value(ThermalElementType)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "thermalLoad": lambda n : setattr(self, 'thermal_load', n.get_float_value()),
            "yThermalGradient": lambda n : setattr(self, 'y_thermal_gradient', n.get_float_value()),
            "zThermalGradient": lambda n : setattr(self, 'z_thermal_gradient', n.get_float_value()),
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
        writer.write_enum_value("elementType", self.element_type)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("key", self.key)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_float_value("thermalLoad", self.thermal_load)
        writer.write_float_value("yThermalGradient", self.y_thermal_gradient)
        writer.write_float_value("zThermalGradient", self.z_thermal_gradient)
    

