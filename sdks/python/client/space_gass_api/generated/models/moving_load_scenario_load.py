from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .moving_load_stationary_option import MovingLoadStationaryOption
    from .moving_load_type import MovingLoadType

@dataclass
class MovingLoadScenarioLoad(Parsable):
    """
    One load row within a scenario — a vehicle or pressure run along a travel path. This shapeis used both when reading a scenario's loads and as the element of the`PUT moving-loads/scenarios/{id}/loads` body, which replaces the entire list.
    """
    # Delay before the vehicle/pressure starts moving.
    delay: Optional[float] = None
    # Dynamic amplification factor applied to the load.
    dynamic_factor: Optional[float] = None
    # Controls which load cases a scenario load's stationary loads are generated into.Mirrors SPACE GASS `MLGenerateStationary` (`NETSpaceGass/Loads/Moving/MLCommon.vb`).
    generate_stationary_lc: Optional[MovingLoadStationaryOption] = None
    # Lane factor applied to the load.
    lane_factor: Optional[float] = None
    # Multiplier applied to the load magnitudes.
    load_factor: Optional[float] = None
    # Discriminates a moving-load scenario load between a vehicle run and a pressure run.Mirrors SPACE GASS `MLScenarioLoadType` (`NETSpaceGass/Loads/Moving/MLCommon.vb`).
    load_type: Optional[MovingLoadType] = None
    # The pressure Id this load uses.
    pressure_id: Optional[int] = None
    # Travel speed along the path.
    speed: Optional[float] = None
    # Starting position measured along the travel path.
    start_position: Optional[float] = None
    # The travel-path Id this load travels along.
    travel_path_id: Optional[int] = None
    # The vehicle Id this load uses.
    vehicle_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadScenarioLoad:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadScenarioLoad
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadScenarioLoad()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .moving_load_stationary_option import MovingLoadStationaryOption
        from .moving_load_type import MovingLoadType

        from .moving_load_stationary_option import MovingLoadStationaryOption
        from .moving_load_type import MovingLoadType

        fields: dict[str, Callable[[Any], None]] = {
            "delay": lambda n : setattr(self, 'delay', n.get_float_value()),
            "dynamicFactor": lambda n : setattr(self, 'dynamic_factor', n.get_float_value()),
            "generateStationaryLc": lambda n : setattr(self, 'generate_stationary_lc', n.get_enum_value(MovingLoadStationaryOption)),
            "laneFactor": lambda n : setattr(self, 'lane_factor', n.get_float_value()),
            "loadFactor": lambda n : setattr(self, 'load_factor', n.get_float_value()),
            "loadType": lambda n : setattr(self, 'load_type', n.get_enum_value(MovingLoadType)),
            "pressureId": lambda n : setattr(self, 'pressure_id', n.get_int_value()),
            "speed": lambda n : setattr(self, 'speed', n.get_float_value()),
            "startPosition": lambda n : setattr(self, 'start_position', n.get_float_value()),
            "travelPathId": lambda n : setattr(self, 'travel_path_id', n.get_int_value()),
            "vehicleId": lambda n : setattr(self, 'vehicle_id', n.get_int_value()),
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
        writer.write_float_value("delay", self.delay)
        writer.write_float_value("dynamicFactor", self.dynamic_factor)
        writer.write_enum_value("generateStationaryLc", self.generate_stationary_lc)
        writer.write_float_value("laneFactor", self.lane_factor)
        writer.write_float_value("loadFactor", self.load_factor)
        writer.write_enum_value("loadType", self.load_type)
        writer.write_int_value("pressureId", self.pressure_id)
        writer.write_float_value("speed", self.speed)
        writer.write_float_value("startPosition", self.start_position)
        writer.write_int_value("travelPathId", self.travel_path_id)
        writer.write_int_value("vehicleId", self.vehicle_id)
    

