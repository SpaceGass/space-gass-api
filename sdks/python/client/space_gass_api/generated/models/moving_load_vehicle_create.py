from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vehicle_load_units import VehicleLoadUnits
    from .vehicle_wheel_load import VehicleWheelLoad

@dataclass
class MovingLoadVehicleCreate(Parsable):
    """
    Creates a user-defined vehicle from supplied wheel loads. To import a vehicle from alibrary instead, use `POST moving-loads/vehicles/library`.
    """
    # The units a vehicle's wheel loads are stored in. Independent of the job-level units.
    load_units: Optional[VehicleLoadUnits] = None
    # The vehicle's wheel loads. Must contain at least one wheel.
    loads: Optional[list[VehicleWheelLoad]] = None
    # The vehicle name. Must be unique across all vehicles.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadVehicleCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadVehicleCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadVehicleCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vehicle_load_units import VehicleLoadUnits
        from .vehicle_wheel_load import VehicleWheelLoad

        from .vehicle_load_units import VehicleLoadUnits
        from .vehicle_wheel_load import VehicleWheelLoad

        fields: dict[str, Callable[[Any], None]] = {
            "loadUnits": lambda n : setattr(self, 'load_units', n.get_object_value(VehicleLoadUnits)),
            "loads": lambda n : setattr(self, 'loads', n.get_collection_of_object_values(VehicleWheelLoad)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_object_value("loadUnits", self.load_units)
        writer.write_collection_of_object_values("loads", self.loads)
        writer.write_str_value("name", self.name)
    

