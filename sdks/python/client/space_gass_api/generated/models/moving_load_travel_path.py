from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .moving_load_station import MovingLoadStation

@dataclass
class MovingLoadTravelPath(Parsable):
    """
    A moving-load travel path — a named, ordered list of stations defining the route avehicle or pressure travels along. Stations are hydrated inline only when `expand=All`.
    """
    # Whether the travel path has any stations.
    has_stations: Optional[bool] = None
    # The item Id.
    id: Optional[int] = None
    # The travel-path name. Unique across all travel paths.
    name: Optional[str] = None
    # The travel path's stations, in order. Populated only when `expand=All`; otherwise omitted.
    stations: Optional[list[MovingLoadStation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadTravelPath:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadTravelPath
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadTravelPath()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .moving_load_station import MovingLoadStation

        from .moving_load_station import MovingLoadStation

        fields: dict[str, Callable[[Any], None]] = {
            "hasStations": lambda n : setattr(self, 'has_stations', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "stations": lambda n : setattr(self, 'stations', n.get_collection_of_object_values(MovingLoadStation)),
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
        writer.write_bool_value("hasStations", self.has_stations)
        writer.write_int_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("stations", self.stations)
    

