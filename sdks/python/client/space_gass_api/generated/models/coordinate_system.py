from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .point3_d import Point3D
    from .vector3_d import Vector3D

@dataclass
class CoordinateSystem(Parsable):
    """
    A local coordinate system (LCS): an origin plus three local axis unit vectorsexpressed in global coordinates. The axes form a right-handed orthonormal basis —the columns of the element's local-to-global transformation matrix.
    """
    # A 3D point with X, Y, Z coordinates.
    origin: Optional[Point3D] = None
    # A 3D vector with X, Y, Z components.
    x_vector: Optional[Vector3D] = None
    # A 3D vector with X, Y, Z components.
    y_vector: Optional[Vector3D] = None
    # A 3D vector with X, Y, Z components.
    z_vector: Optional[Vector3D] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CoordinateSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CoordinateSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CoordinateSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .point3_d import Point3D
        from .vector3_d import Vector3D

        from .point3_d import Point3D
        from .vector3_d import Vector3D

        fields: dict[str, Callable[[Any], None]] = {
            "origin": lambda n : setattr(self, 'origin', n.get_object_value(Point3D)),
            "xVector": lambda n : setattr(self, 'x_vector', n.get_object_value(Vector3D)),
            "yVector": lambda n : setattr(self, 'y_vector', n.get_object_value(Vector3D)),
            "zVector": lambda n : setattr(self, 'z_vector', n.get_object_value(Vector3D)),
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
        writer.write_object_value("origin", self.origin)
        writer.write_object_value("xVector", self.x_vector)
        writer.write_object_value("yVector", self.y_vector)
        writer.write_object_value("zVector", self.z_vector)
    

