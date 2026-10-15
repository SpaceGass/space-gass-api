from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_shape import SectionShape

from .section_shape import SectionShape

@dataclass
class WedgeShape(SectionShape, Parsable):
    """
    Wedge.
    """
    # Width.
    b: Optional[float] = None
    # Depth at the first edge.
    d1: Optional[float] = None
    # Depth at the second edge.
    d2: Optional[float] = None
    # Selects this object type. Always "Wedge".
    shape_type: Optional[WedgeShape_shapeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WedgeShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WedgeShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WedgeShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_shape import SectionShape

        from .section_shape import SectionShape

        fields: dict[str, Callable[[Any], None]] = {
            "b": lambda n : setattr(self, 'b', n.get_float_value()),
            "d1": lambda n : setattr(self, 'd1', n.get_float_value()),
            "d2": lambda n : setattr(self, 'd2', n.get_float_value()),
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
        writer.write_float_value("d1", self.d1)
        writer.write_float_value("d2", self.d2)
    

