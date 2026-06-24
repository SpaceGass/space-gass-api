from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .moving_load_vehicle_source import MovingLoadVehicleSource
    from .vehicle_load_units import VehicleLoadUnits
    from .vehicle_wheel_load import VehicleWheelLoad

@dataclass
class MovingLoadVehicle(Parsable):
    """
    A moving-load vehicle — a named set of wheel loads, either user-defined or imported froma vehicle library. A vehicle carries its own units (length/force/moment); its wheel loadsare stored in those units and are not affected by job-level unit conversion.
    """
    # The item Id.
    id: Optional[int] = None
    # The name of the library the vehicle was imported from.
    library: Optional[str] = None
    # The units a vehicle's wheel loads are stored in. Independent of the job-level units.
    load_units: Optional[VehicleLoadUnits] = None
    # The vehicle's wheel loads.
    loads: Optional[list[VehicleWheelLoad]] = None
    # The vehicle name. Unique across all vehicles.
    name: Optional[str] = None
    # Origin of a moving-load vehicle. Mirrors SPACE GASS `MLVehicleSource`(`NETSpaceGass/Loads/Moving/MLCommon.vb`).
    source: Optional[MovingLoadVehicleSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadVehicle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadVehicle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadVehicle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .moving_load_vehicle_source import MovingLoadVehicleSource
        from .vehicle_load_units import VehicleLoadUnits
        from .vehicle_wheel_load import VehicleWheelLoad

        from .moving_load_vehicle_source import MovingLoadVehicleSource
        from .vehicle_load_units import VehicleLoadUnits
        from .vehicle_wheel_load import VehicleWheelLoad

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "loadUnits": lambda n : setattr(self, 'load_units', n.get_object_value(VehicleLoadUnits)),
            "loads": lambda n : setattr(self, 'loads', n.get_collection_of_object_values(VehicleWheelLoad)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(MovingLoadVehicleSource)),
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
        writer.write_int_value("id", self.id)
        writer.write_str_value("library", self.library)
        writer.write_object_value("loadUnits", self.load_units)
        writer.write_collection_of_object_values("loads", self.loads)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("source", self.source)
    

