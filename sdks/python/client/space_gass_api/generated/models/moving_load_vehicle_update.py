from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vehicle_wheel_load import VehicleWheelLoad

@dataclass
class MovingLoadVehicleUpdate(Parsable):
    """
    Partial update for a user-defined vehicle. All properties are optional; omitted propertieskeep their current value. A library vehicle's source and library cannot be changed here.
    """
    # The Id of the item to update.
    id: Optional[int] = None
    # Replacement wheel loads. When present, replaces the entire wheel-load list. Omit to keep current.
    loads: Optional[list[VehicleWheelLoad]] = None
    # Replacement vehicle name. Must remain unique. Omit to keep current.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadVehicleUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadVehicleUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadVehicleUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .vehicle_wheel_load import VehicleWheelLoad

        from .vehicle_wheel_load import VehicleWheelLoad

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_collection_of_object_values("loads", self.loads)
        writer.write_str_value("name", self.name)
    

