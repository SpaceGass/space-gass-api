from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_outline import SectionOutline

@dataclass
class SectionShapeGeometry(Parsable):
    """
    The geometry of one shape of a section: the outlines drawn for it, in the member's localY-Z plane with the origin at the section centroid.
    """
    # The outlines drawn for the shape, each an outer boundary with any holes.
    outlines: Optional[list[SectionOutline]] = None
    # Id of the shape: its one-based position in the section's shape list.
    shape: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionShapeGeometry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionShapeGeometry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionShapeGeometry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_outline import SectionOutline

        from .section_outline import SectionOutline

        fields: dict[str, Callable[[Any], None]] = {
            "outlines": lambda n : setattr(self, 'outlines', n.get_collection_of_object_values(SectionOutline)),
            "shape": lambda n : setattr(self, 'shape', n.get_int_value()),
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
        writer.write_collection_of_object_values("outlines", self.outlines)
        writer.write_int_value("shape", self.shape)
    

