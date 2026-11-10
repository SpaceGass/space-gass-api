from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelStrength(Parsable):
    """
    Steel strength values for one grade of a shape (yield and ultimate stresses).
    """
    # Ultimate tensile strength.
    fu: Optional[float] = None
    # Flange yield stress.
    fy: Optional[float] = None
    # Web yield stress.
    fyw: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelStrength:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelStrength
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelStrength()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fu": lambda n : setattr(self, 'fu', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fyw": lambda n : setattr(self, 'fyw', n.get_float_value()),
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
        writer.write_float_value("fu", self.fu)
        writer.write_float_value("fy", self.fy)
        writer.write_float_value("fyw", self.fyw)
    

