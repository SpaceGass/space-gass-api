from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlateCutUpdate(Parsable):
    """
    DTO for updating an existing plate cut.All fields are nullable to support partial updates.
    """
    # End node number for the cut.
    end_node: Optional[int] = None
    # Longitudinal offset at the end of the cut.
    end_offset_longitudinal: Optional[float] = None
    # Transverse offset at the end of the cut.
    end_offset_transverse: Optional[float] = None
    # End plate number for the cut.
    end_plate: Optional[int] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary key identifying the entity to update.Optional for single updates (key comes from route), required for batch updates.
    key: Optional[int] = None
    # Out-of-plane tolerance for the cut.
    out_of_plane_tolerance: Optional[float] = None
    # Start node number for the cut.
    start_node: Optional[int] = None
    # Longitudinal offset at the start of the cut.
    start_offset_longitudinal: Optional[float] = None
    # Transverse offset at the start of the cut.
    start_offset_transverse: Optional[float] = None
    # Start plate number for the cut.
    start_plate: Optional[int] = None
    # User-defined title for the plate cut.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateCutUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateCutUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateCutUpdate()
    
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
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "outOfPlaneTolerance": lambda n : setattr(self, 'out_of_plane_tolerance', n.get_float_value()),
            "startNode": lambda n : setattr(self, 'start_node', n.get_int_value()),
            "startOffsetLongitudinal": lambda n : setattr(self, 'start_offset_longitudinal', n.get_float_value()),
            "startOffsetTransverse": lambda n : setattr(self, 'start_offset_transverse', n.get_float_value()),
            "startPlate": lambda n : setattr(self, 'start_plate', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("key", self.key)
        writer.write_float_value("outOfPlaneTolerance", self.out_of_plane_tolerance)
        writer.write_int_value("startNode", self.start_node)
        writer.write_float_value("startOffsetLongitudinal", self.start_offset_longitudinal)
        writer.write_float_value("startOffsetTransverse", self.start_offset_transverse)
        writer.write_int_value("startPlate", self.start_plate)
        writer.write_str_value("title", self.title)
    

