from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_shape import SectionShape
    from .shape_point import ShapePoint

from .section_shape import SectionShape

@dataclass
class LinesShape(SectionShape, Parsable):
    """
    Thin-walled outline defined by a point polyline.
    """
    # Default corner radius applied at points flagged `useDefaultRadius`.
    general_radius: Optional[float] = None
    # Polyline vertices.
    points: Optional[list[ShapePoint]] = None
    # Selects this object type. Always "LinesShape".
    shape_type: Optional[LinesShape_shapeType] = None
    # Wall thickness along the polyline.
    thickness: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinesShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinesShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LinesShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_shape import SectionShape
        from .shape_point import ShapePoint

        from .section_shape import SectionShape
        from .shape_point import ShapePoint

        fields: dict[str, Callable[[Any], None]] = {
            "generalRadius": lambda n : setattr(self, 'general_radius', n.get_float_value()),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(ShapePoint)),
            "thickness": lambda n : setattr(self, 'thickness', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_float_value("generalRadius", self.general_radius)
        writer.write_collection_of_object_values("points", self.points)
        writer.write_float_value("thickness", self.thickness)
    

