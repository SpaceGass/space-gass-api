from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadStation(Parsable):
    """
    One station on a travel path — a point in space, optionally relative to a node. This shapeis used both when reading a path's stations and as the element of the`PUT moving-loads/travel-paths/{id}/stations` body, which replaces the entire list.
    """
    # The node this station is relative to.
    node_key: Optional[int] = None
    # Arc radius into this station from the previous one.
    radius: Optional[float] = None
    # X coordinate (or X offset from SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadStationDto.NodeKey when a node is set).
    x: Optional[float] = None
    # Y coordinate (or Y offset from SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadStationDto.NodeKey when a node is set).
    y: Optional[float] = None
    # Z coordinate (or Z offset from SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadStationDto.NodeKey when a node is set).
    z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadStation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadStation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadStation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "nodeKey": lambda n : setattr(self, 'node_key', n.get_int_value()),
            "radius": lambda n : setattr(self, 'radius', n.get_float_value()),
            "x": lambda n : setattr(self, 'x', n.get_float_value()),
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
            "z": lambda n : setattr(self, 'z', n.get_float_value()),
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
        writer.write_int_value("nodeKey", self.node_key)
        writer.write_float_value("radius", self.radius)
        writer.write_float_value("x", self.x)
        writer.write_float_value("y", self.y)
        writer.write_float_value("z", self.z)
    

