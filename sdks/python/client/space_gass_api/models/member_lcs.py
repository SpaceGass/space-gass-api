from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .point3d import Point3d
    from .vector3d import Vector3d

@dataclass
class MemberLcs(Parsable):
    """
    DTO for a member's local coordinate system (LCS).Contains the base point and direction vector defining the member's local axes.
    """
    # A 3D point with X, Y, Z coordinates.
    base_point: Optional[Point3d] = None
    # A 3D vector with X, Y, Z components.
    direction_vector: Optional[Vector3d] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberLcs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberLcs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberLcs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .point3d import Point3d
        from .vector3d import Vector3d

        from .point3d import Point3d
        from .vector3d import Vector3d

        fields: dict[str, Callable[[Any], None]] = {
            "basePoint": lambda n : setattr(self, 'base_point', n.get_object_value(Point3d)),
            "directionVector": lambda n : setattr(self, 'direction_vector', n.get_object_value(Vector3d)),
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
        writer.write_object_value("basePoint", self.base_point)
        writer.write_object_value("directionVector", self.direction_vector)
    

