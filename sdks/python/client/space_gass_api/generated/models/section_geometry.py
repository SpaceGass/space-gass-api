from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_bounds import SectionBounds
    from .section_shape_geometry import SectionShapeGeometry

@dataclass
class SectionGeometry(Parsable):
    """
    Derived geometry of a section — its cross-section outline, computed from the section'sshapes. Positioned in the member's local Y-Z plane with the origin at the sectioncentroid, so a member's solid is the outlines swept from `pointA` to `pointB`along the member's `localAxes` (see GET /job/query/geometry/members).
    """
    # An axis-aligned extent in the member's local Y-Z plane, with the origin at the section centroid.
    bounds: Optional[SectionBounds] = None
    # Section name.
    name: Optional[str] = None
    # The section this geometry belongs to.
    section: Optional[int] = None
    # The geometry of each shape, in the order of the section's shape list.
    shapes: Optional[list[SectionShapeGeometry]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionGeometry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionGeometry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionGeometry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_bounds import SectionBounds
        from .section_shape_geometry import SectionShapeGeometry

        from .section_bounds import SectionBounds
        from .section_shape_geometry import SectionShapeGeometry

        fields: dict[str, Callable[[Any], None]] = {
            "bounds": lambda n : setattr(self, 'bounds', n.get_object_value(SectionBounds)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "section": lambda n : setattr(self, 'section', n.get_int_value()),
            "shapes": lambda n : setattr(self, 'shapes', n.get_collection_of_object_values(SectionShapeGeometry)),
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
        writer.write_str_value("name", self.name)
        writer.write_int_value("section", self.section)
        writer.write_collection_of_object_values("shapes", self.shapes)
    

