from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SectionPoint(Parsable):
    """
    A point on a section outline, in the member's local Y-Z plane with the origin at thesection centroid.
    """
    # Position along the member's local Y axis (through the section depth).
    y: Optional[float] = None
    # Position along the member's local Z axis (across the section width).
    z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
            "z": lambda n : setattr(self, 'z', n.get_float_value()),
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
        writer.write_float_value("y", self.y)
        writer.write_float_value("z", self.z)
    

