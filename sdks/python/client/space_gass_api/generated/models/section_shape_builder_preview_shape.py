from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .reference_point import ReferencePoint
    from .section_bounds import SectionBounds
    from .section_outline import SectionOutline

@dataclass
class SectionShapeBuilderPreviewShape(Parsable):
    """
    The geometry of one shape of a shape-builder preview, with its extent and numberedreference points.
    """
    # An axis-aligned extent in the member's local Y-Z plane, with the origin at the section centroid.
    bounds: Optional[SectionBounds] = None
    # The outlines drawn for the shape, each an outer boundary with any holes.
    outlines: Optional[list[SectionOutline]] = None
    # The shape's reference points, numbered from 1: the points the SPACE GASS shape buildersnaps to, in the same plane, origin and unit as the outlines.
    reference_points: Optional[list[ReferencePoint]] = None
    # Id of the shape: its one-based position in the section's shape list.
    shape: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionShapeBuilderPreviewShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionShapeBuilderPreviewShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionShapeBuilderPreviewShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .reference_point import ReferencePoint
        from .section_bounds import SectionBounds
        from .section_outline import SectionOutline

        from .reference_point import ReferencePoint
        from .section_bounds import SectionBounds
        from .section_outline import SectionOutline

        fields: dict[str, Callable[[Any], None]] = {
            "bounds": lambda n : setattr(self, 'bounds', n.get_object_value(SectionBounds)),
            "outlines": lambda n : setattr(self, 'outlines', n.get_collection_of_object_values(SectionOutline)),
            "referencePoints": lambda n : setattr(self, 'reference_points', n.get_collection_of_object_values(ReferencePoint)),
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
        writer.write_object_value("bounds", self.bounds)
        writer.write_collection_of_object_values("outlines", self.outlines)
        writer.write_collection_of_object_values("referencePoints", self.reference_points)
        writer.write_int_value("shape", self.shape)
    

