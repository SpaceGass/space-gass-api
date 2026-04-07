from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FieldMetadata(Parsable):
    """
    Metadata for a single field in an entity table.Provides schema information for clients to validate and display entity data.
    """
    # Whether the field can be empty/null
    allow_empty: Optional[bool] = None
    # Data type (Integer, Double, String, etc.)
    data_type: Optional[str] = None
    # Default value (if applicable)
    default: Optional[str] = None
    # Field name
    field_name: Optional[str] = None
    # Field index in the underlying data structure
    index: Optional[int] = None
    # Maximum allowed value (if applicable)
    max: Optional[str] = None
    # Minimum allowed value (if applicable)
    min: Optional[str] = None
    # Resolved unit label based on current job units (e.g., "mm", "kN/mm").This is what values in requests/responses are measured in.Null if the field has no units.
    units: Optional[str] = None
    # Units mask token (e.g., "<Length>") - null if no units.This is the raw mask from the DataSpec.
    units_mask: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FieldMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FieldMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FieldMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowEmpty": lambda n : setattr(self, 'allow_empty', n.get_bool_value()),
            "dataType": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "default": lambda n : setattr(self, 'default', n.get_str_value()),
            "fieldName": lambda n : setattr(self, 'field_name', n.get_str_value()),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "max": lambda n : setattr(self, 'max', n.get_str_value()),
            "min": lambda n : setattr(self, 'min', n.get_str_value()),
            "units": lambda n : setattr(self, 'units', n.get_str_value()),
            "unitsMask": lambda n : setattr(self, 'units_mask', n.get_str_value()),
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
        writer.write_bool_value("allowEmpty", self.allow_empty)
        writer.write_str_value("dataType", self.data_type)
        writer.write_str_value("default", self.default)
        writer.write_str_value("fieldName", self.field_name)
        writer.write_int_value("index", self.index)
        writer.write_str_value("max", self.max)
        writer.write_str_value("min", self.min)
        writer.write_str_value("units", self.units)
        writer.write_str_value("unitsMask", self.units_mask)
    

