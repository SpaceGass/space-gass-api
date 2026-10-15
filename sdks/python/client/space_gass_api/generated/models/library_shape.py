from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .angle_type import AngleType
    from .section_shape import SectionShape

from .section_shape import SectionShape

@dataclass
class LibraryShape(SectionShape, Parsable):
    """
    A shape taken from a section library item, identified by library and item name.
    """
    # Angle section type for structural sections.Maps to SPACE GASS lookup table "Angle Type".
    angle_type: Optional[AngleType] = None
    # Library holding the item, by its file name.
    library: Optional[str] = None
    # Item name within the library.
    name: Optional[str] = None
    # Selects this object type. Always "Library".
    shape_type: Optional[LibraryShape_shapeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LibraryShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LibraryShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LibraryShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .angle_type import AngleType
        from .section_shape import SectionShape

        from .angle_type import AngleType
        from .section_shape import SectionShape

        fields: dict[str, Callable[[Any], None]] = {
            "angleType": lambda n : setattr(self, 'angle_type', n.get_enum_value(AngleType)),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_enum_value("angleType", self.angle_type)
        writer.write_str_value("library", self.library)
        writer.write_str_value("name", self.name)
    

