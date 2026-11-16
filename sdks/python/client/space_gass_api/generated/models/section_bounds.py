from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SectionBounds(Parsable):
    """
    An axis-aligned extent in the member's local Y-Z plane, with the origin at the section centroid.
    """
    # Highest position along the member's local Y axis.
    max_y: Optional[float] = None
    # Highest position along the member's local Z axis.
    max_z: Optional[float] = None
    # Lowest position along the member's local Y axis.
    min_y: Optional[float] = None
    # Lowest position along the member's local Z axis.
    min_z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionBounds:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionBounds
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionBounds()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "maxY": lambda n : setattr(self, 'max_y', n.get_float_value()),
            "maxZ": lambda n : setattr(self, 'max_z', n.get_float_value()),
            "minY": lambda n : setattr(self, 'min_y', n.get_float_value()),
            "minZ": lambda n : setattr(self, 'min_z', n.get_float_value()),
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
        writer.write_float_value("maxY", self.max_y)
        writer.write_float_value("maxZ", self.max_z)
        writer.write_float_value("minY", self.min_y)
        writer.write_float_value("minZ", self.min_z)
    

