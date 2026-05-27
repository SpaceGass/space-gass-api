from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SelfWeightLoadCreate(Parsable):
    """
    DTO for creating a new self-weight load.Only one self-weight load is permitted per load case (case is the entire key).
    """
    # Gravitational acceleration in the global X direction.
    acceleration_x: Optional[float] = None
    # Gravitational acceleration in the global Y direction.
    acceleration_y: Optional[float] = None
    # Gravitational acceleration in the global Z direction.
    acceleration_z: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # The load case number to create this load in.
    load_case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelfWeightLoadCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfWeightLoadCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelfWeightLoadCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accelerationX": lambda n : setattr(self, 'acceleration_x', n.get_float_value()),
            "accelerationY": lambda n : setattr(self, 'acceleration_y', n.get_float_value()),
            "accelerationZ": lambda n : setattr(self, 'acceleration_z', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
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
        writer.write_float_value("accelerationX", self.acceleration_x)
        writer.write_float_value("accelerationY", self.acceleration_y)
        writer.write_float_value("accelerationZ", self.acceleration_z)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_int_value("loadCategory", self.load_category)
    

