from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_id import EntityId
    from .field_metadata import FieldMetadata

@dataclass
class ResourceMetadata(Parsable):
    """
    Metadata describing an API resource — entity, sub-resource, or result set.Returned from `GET …/metadata` endpoints so clients can introspect theshape, units, and valid values of the data without hitting a live endpoint.
    """
    # Current count of items in this resource.Null for sub-resources whose count does not apply uniformly.
    count: Optional[int] = None
    # Field definitions describing the resource's wire shape. Each entry correspondsto a property on the read DTO; `jsonName` matches the JSON key clients see.
    fields: Optional[list[FieldMetadata]] = None
    # Maximum Id currently in use (single-int Id entities only).
    max_id: Optional[int] = None
    # Next available Id (single-int Id entities only).
    next_id: Optional[int] = None
    # Identifies entity types managed by the API.Kept separate from SGFileID to allow for future API-only entitiesthat may not have a formal SPACE GASS FileID.
    resource_type: Optional[EntityId] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResourceMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_id import EntityId
        from .field_metadata import FieldMetadata

        from .entity_id import EntityId
        from .field_metadata import FieldMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(FieldMetadata)),
            "maxId": lambda n : setattr(self, 'max_id', n.get_int_value()),
            "nextId": lambda n : setattr(self, 'next_id', n.get_int_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_enum_value(EntityId)),
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
        writer.write_int_value("count", self.count)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_int_value("maxId", self.max_id)
        writer.write_int_value("nextId", self.next_id)
        writer.write_enum_value("resourceType", self.resource_type)
    

