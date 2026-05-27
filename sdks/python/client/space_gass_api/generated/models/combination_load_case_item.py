from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CombinationLoadCaseItem(Parsable):
    """
    Represents a single component within a load combination — a component case Id andthe multiplying factor applied to it.
    """
    # Component load case number.
    load_case: Optional[int] = None
    # Multiplying factor applied to the component load case (default: 1.0).
    multiplying_factor: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CombinationLoadCaseItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CombinationLoadCaseItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CombinationLoadCaseItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "multiplyingFactor": lambda n : setattr(self, 'multiplying_factor', n.get_float_value()),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("multiplyingFactor", self.multiplying_factor)
    

