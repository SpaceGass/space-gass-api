from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_shape_builder_create_shapes import SectionShapeBuilderCreate_shapes

@dataclass
class SectionShapeBuilderCreate(Parsable):
    """
    DTO for creating a shape-builder (multi-shape) section. The section's structuralproperties (A, J, Iy, Iz, …) are computed by SPACE GASS from the supplied shapes —they are not asserted by the caller.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # Section mark / designation.
    mark: Optional[str] = None
    # Section name.
    name: Optional[str] = None
    # The shapes composited into the section, in order.
    shapes: Optional[list[SectionShapeBuilderCreate_shapes]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionShapeBuilderCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionShapeBuilderCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionShapeBuilderCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_shape_builder_create_shapes import SectionShapeBuilderCreate_shapes

        from .section_shape_builder_create_shapes import SectionShapeBuilderCreate_shapes

        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mark": lambda n : setattr(self, 'mark', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "shapes": lambda n : setattr(self, 'shapes', n.get_collection_of_object_values(SectionShapeBuilderCreate_shapes)),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_str_value("mark", self.mark)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("shapes", self.shapes)
    

