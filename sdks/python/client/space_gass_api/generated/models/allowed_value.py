from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AllowedValue(Parsable):
    """
    A permitted value for an enum-backed field.Use `value` in request bodies; `label` is for display only.
    """
    # Human-readable label for display (e.g. `"Compression only"`). Pulled from`[Description]` or `[Display(Name=…)]` on the enum member when present,otherwise falls back to the enum identifier.
    label: Optional[str] = None
    # The exact string token the wire accepts and returns for this enum value(the C# enum identifier, e.g. `"CompressionOnly"`). Use this directly inrequest bodies — it matches what comes back on reads.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllowedValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllowedValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllowedValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("label", self.label)
        writer.write_str_value("value", self.value)
    

