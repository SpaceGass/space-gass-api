from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ShapePoint(Parsable):
    """
    A vertex of a points-based shape outline.
    """
    # Corner radius at the point.
    radius: Optional[float] = None
    # Whether the shape's general radius is used at this point instead of `radius`.
    use_default_radius: Optional[bool] = None
    # Y coordinate of the point.
    y: Optional[float] = None
    # Z coordinate of the point.
    z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ShapePoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ShapePoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ShapePoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "radius": lambda n : setattr(self, 'radius', n.get_float_value()),
            "useDefaultRadius": lambda n : setattr(self, 'use_default_radius', n.get_bool_value()),
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
        writer.write_float_value("radius", self.radius)
        writer.write_bool_value("useDefaultRadius", self.use_default_radius)
        writer.write_float_value("y", self.y)
        writer.write_float_value("z", self.z)
    

