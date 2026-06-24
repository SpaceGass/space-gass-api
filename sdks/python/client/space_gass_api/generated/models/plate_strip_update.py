from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlateStripUpdate(Parsable):
    """
    DTO for updating an existing plate strip.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # End node number for the strip.
    end_node: Optional[int] = None
    # Longitudinal offset at the end of the strip.
    end_offset_longitudinal: Optional[float] = None
    # Transverse offset at the end of the strip.
    end_offset_transverse: Optional[float] = None
    # End plate number for the strip.
    end_plate: Optional[int] = None
    # Left width at the end of the strip.
    end_width_left: Optional[float] = None
    # Right width at the end of the strip.
    end_width_right: Optional[float] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Out-of-plane tolerance for the strip.
    out_of_plane_tolerance: Optional[float] = None
    # Start node number for the strip.
    start_node: Optional[int] = None
    # Longitudinal offset at the start of the strip.
    start_offset_longitudinal: Optional[float] = None
    # Transverse offset at the start of the strip.
    start_offset_transverse: Optional[float] = None
    # Start plate number for the strip.
    start_plate: Optional[int] = None
    # Left width at the start of the strip.
    start_width_left: Optional[float] = None
    # Right width at the start of the strip.
    start_width_right: Optional[float] = None
    # User-defined title for the plate strip.
    title: Optional[str] = None
    # Transverse increment spacing along the strip.
    transverse_increment: Optional[float] = None
    # Whether the strip has uniform width along its length.
    uniform_width: Optional[bool] = None
    # Uniform width of the strip.
    width: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateStripUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateStripUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateStripUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "endNode": lambda n : setattr(self, 'end_node', n.get_int_value()),
            "endOffsetLongitudinal": lambda n : setattr(self, 'end_offset_longitudinal', n.get_float_value()),
            "endOffsetTransverse": lambda n : setattr(self, 'end_offset_transverse', n.get_float_value()),
            "endPlate": lambda n : setattr(self, 'end_plate', n.get_int_value()),
            "endWidthLeft": lambda n : setattr(self, 'end_width_left', n.get_float_value()),
            "endWidthRight": lambda n : setattr(self, 'end_width_right', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "outOfPlaneTolerance": lambda n : setattr(self, 'out_of_plane_tolerance', n.get_float_value()),
            "startNode": lambda n : setattr(self, 'start_node', n.get_int_value()),
            "startOffsetLongitudinal": lambda n : setattr(self, 'start_offset_longitudinal', n.get_float_value()),
            "startOffsetTransverse": lambda n : setattr(self, 'start_offset_transverse', n.get_float_value()),
            "startPlate": lambda n : setattr(self, 'start_plate', n.get_int_value()),
            "startWidthLeft": lambda n : setattr(self, 'start_width_left', n.get_float_value()),
            "startWidthRight": lambda n : setattr(self, 'start_width_right', n.get_float_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "transverseIncrement": lambda n : setattr(self, 'transverse_increment', n.get_float_value()),
            "uniformWidth": lambda n : setattr(self, 'uniform_width', n.get_bool_value()),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
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
        writer.write_int_value("endNode", self.end_node)
        writer.write_float_value("endOffsetLongitudinal", self.end_offset_longitudinal)
        writer.write_float_value("endOffsetTransverse", self.end_offset_transverse)
        writer.write_int_value("endPlate", self.end_plate)
        writer.write_float_value("endWidthLeft", self.end_width_left)
        writer.write_float_value("endWidthRight", self.end_width_right)
        writer.write_int_value("id", self.id)
        writer.write_float_value("outOfPlaneTolerance", self.out_of_plane_tolerance)
        writer.write_int_value("startNode", self.start_node)
        writer.write_float_value("startOffsetLongitudinal", self.start_offset_longitudinal)
        writer.write_float_value("startOffsetTransverse", self.start_offset_transverse)
        writer.write_int_value("startPlate", self.start_plate)
        writer.write_float_value("startWidthLeft", self.start_width_left)
        writer.write_float_value("startWidthRight", self.start_width_right)
        writer.write_str_value("title", self.title)
        writer.write_float_value("transverseIncrement", self.transverse_increment)
        writer.write_bool_value("uniformWidth", self.uniform_width)
        writer.write_float_value("width", self.width)
    

