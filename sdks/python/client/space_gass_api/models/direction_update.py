from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .direction_axis import DirectionAxis

@dataclass
class DirectionUpdate(Parsable):
    """
    DTO for updating the direction on a member or plate (partial-update semantics).
    """
    # Direction angle for orientation. Mutually exclusive with `dirNode` and `dirAxis`.
    dir_angle: Optional[float] = None
    # Direction axis for member orientation.Maps to SPACE GASS lookup table "Direction Axis".
    dir_axis: Optional[DirectionAxis] = None
    # Direction node Id for orientation. Mutually exclusive with `dirAngle` and `dirAxis`.
    dir_node: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectionUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectionUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectionUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .direction_axis import DirectionAxis

        from .direction_axis import DirectionAxis

        fields: dict[str, Callable[[Any], None]] = {
            "dirAngle": lambda n : setattr(self, 'dir_angle', n.get_float_value()),
            "dirAxis": lambda n : setattr(self, 'dir_axis', n.get_enum_value(DirectionAxis)),
            "dirNode": lambda n : setattr(self, 'dir_node', n.get_int_value()),
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
        writer.write_float_value("dirAngle", self.dir_angle)
        writer.write_enum_value("dirAxis", self.dir_axis)
        writer.write_int_value("dirNode", self.dir_node)
    

