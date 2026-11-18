from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ShapeAnchorPosition(Parsable):
    """
    Positions a shape by snapping one of its reference points onto a reference point of anearlier shape. Input only: it sets the shape's `translateZ` / `translateY`, whichare returned in its place.
    """
    # The numbered reference point of `anchorShape` to snap onto.
    anchor_point: Optional[int] = None
    # One-based Id of the shape to snap onto.
    anchor_shape: Optional[int] = None
    # The numbered reference point of this shape that lands on `anchorPoint`.
    shape_point: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ShapeAnchorPosition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ShapeAnchorPosition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ShapeAnchorPosition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "anchorPoint": lambda n : setattr(self, 'anchor_point', n.get_int_value()),
            "anchorShape": lambda n : setattr(self, 'anchor_shape', n.get_int_value()),
            "shapePoint": lambda n : setattr(self, 'shape_point', n.get_int_value()),
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
        writer.write_int_value("anchorPoint", self.anchor_point)
        writer.write_int_value("anchorShape", self.anchor_shape)
        writer.write_int_value("shapePoint", self.shape_point)
    

