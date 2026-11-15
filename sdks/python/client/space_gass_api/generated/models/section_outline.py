from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_point import SectionPoint

@dataclass
class SectionOutline(Parsable):
    """
    One closed region of a section outline: an outer boundary and the holes cut from it.
    """
    # The outer boundary, as a closed polygon. Consecutive points are joined and the lastpoint joins back to the first. Curved edges (fillets, tube corners, circles) arrivealready tessellated into straight segments.
    outer: Optional[list[SectionPoint]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionOutline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionOutline
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionOutline()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_point import SectionPoint

        from .section_point import SectionPoint

        fields: dict[str, Callable[[Any], None]] = {
            "outer": lambda n : setattr(self, 'outer', n.get_collection_of_object_values(SectionPoint)),
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
        writer.write_collection_of_object_values("outer", self.outer)
    

