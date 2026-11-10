from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_shape import SectionShape

from .section_shape import SectionShape

@dataclass
class DALongShape(SectionShape, Parsable):
    """
    Double angles, long legs back-to-back.
    """
    # Other-leg length.
    b: Optional[float] = None
    # Leg length.
    d: Optional[float] = None
    # Root radius.
    radius: Optional[float] = None
    # Selects this object type. Always "DALong".
    shape_type: Optional[DALongShape_shapeType] = None
    # Horizontal-leg thickness.
    tb: Optional[float] = None
    # Vertical-leg thickness.
    tw: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DALongShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DALongShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DALongShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_shape import SectionShape

        from .section_shape import SectionShape

        fields: dict[str, Callable[[Any], None]] = {
            "b": lambda n : setattr(self, 'b', n.get_float_value()),
            "d": lambda n : setattr(self, 'd', n.get_float_value()),
            "radius": lambda n : setattr(self, 'radius', n.get_float_value()),
            "tb": lambda n : setattr(self, 'tb', n.get_float_value()),
            "tw": lambda n : setattr(self, 'tw', n.get_float_value()),
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
        writer.write_float_value("b", self.b)
        writer.write_float_value("d", self.d)
        writer.write_float_value("radius", self.radius)
        writer.write_float_value("tb", self.tb)
        writer.write_float_value("tw", self.tw)
    

