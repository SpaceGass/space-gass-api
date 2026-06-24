from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allowed_value import AllowedValue

@dataclass
class FieldMetadata(Parsable):
    """
    Metadata for a single field in a resource. The shape mirrors what clients see onthe wire — SpaceGassApi.Models.Dtos.Common.FieldMetadataDto.JsonName is the exact property key a JSON consumer willread, so a client can correlate metadata to payload without any translation.
    """
    # For enum-backed fields, the permitted values with their wire tokens and display labels.Use `value` in request bodies; `label` is for display only. Null for non-enum fields.
    allowed_values: Optional[list[AllowedValue]] = None
    # Data type: "Integer" | "Double" | "String" | "Enum" | "Boolean" | "Guid".For enums, see SpaceGassApi.Models.Dtos.Common.FieldMetadataDto.AllowedValues for the permitted values.
    data_type: Optional[str] = None
    # Default value when the field is omitted on create.
    default: Optional[str] = None
    # Optional hint text for this field, useful for UI labels and tooltips. Null when not available.
    description: Optional[str] = None
    # Wire-format property key — the JSON object key a client sees in a GETresponse body. This is the authoritative public identifier for the field.
    json_name: Optional[str] = None
    # Maximum allowed value for this field (as a string; use `dataType` to determine how to parse it).Null if no maximum constraint applies.
    max: Optional[str] = None
    # Maximum length for string fields (characters). Null for non-string fields.
    max_length: Optional[int] = None
    # Minimum allowed value for this field (as a string; use `dataType` to determine how to parse it).Null if no minimum constraint applies.
    min: Optional[str] = None
    # Resolved unit label based on the current job units — e.g. "mm", "kN","kN/mm^2". Null when the field has no units.
    units: Optional[str] = None
    
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
        from .allowed_value import AllowedValue

        from .allowed_value import AllowedValue

        fields: dict[str, Callable[[Any], None]] = {
            "allowedValues": lambda n : setattr(self, 'allowed_values', n.get_collection_of_object_values(AllowedValue)),
            "dataType": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "default": lambda n : setattr(self, 'default', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "jsonName": lambda n : setattr(self, 'json_name', n.get_str_value()),
            "max": lambda n : setattr(self, 'max', n.get_str_value()),
            "maxLength": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "min": lambda n : setattr(self, 'min', n.get_str_value()),
            "units": lambda n : setattr(self, 'units', n.get_str_value()),
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
        writer.write_collection_of_object_values("allowedValues", self.allowed_values)
        writer.write_str_value("dataType", self.data_type)
        writer.write_str_value("default", self.default)
        writer.write_str_value("description", self.description)
        writer.write_str_value("jsonName", self.json_name)
        writer.write_str_value("max", self.max)
        writer.write_int_value("maxLength", self.max_length)
        writer.write_str_value("min", self.min)
        writer.write_str_value("units", self.units)
    

