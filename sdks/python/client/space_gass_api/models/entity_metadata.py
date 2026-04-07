from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_id import EntityId
    from .field_metadata import FieldMetadata

@dataclass
class EntityMetadata(Parsable):
    """
    Generic metadata for any entity type.Provides schema information for clients to validate and display entity data.
    """
    # Current count of entities
    count: Optional[int] = None
    # Human-readable display name
    display_name: Optional[str] = None
    # Field definitions describing the entity's schema.Populated from the SPACE GASS DataSpecification.Null if field metadata is not available.
    fields: Optional[list[FieldMetadata]] = None
    # Whether this entity has a GUID field
    has_guid_field: Optional[bool] = None
    # Identifies entity types managed by the API.Kept separate from SGFileID to allow for future API-only entitiesthat may not have a formal SPACE GASS FileID.
    id: Optional[EntityId] = None
    # Maximum key currently in use (for single-int key entities only)
    max_key: Optional[int] = None
    # Next available key (for single-int key entities only)
    next_key: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntityMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntityMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntityMetadata()
    
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
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(FieldMetadata)),
            "hasGuidField": lambda n : setattr(self, 'has_guid_field', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_enum_value(EntityId)),
            "maxKey": lambda n : setattr(self, 'max_key', n.get_int_value()),
            "nextKey": lambda n : setattr(self, 'next_key', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_bool_value("hasGuidField", self.has_guid_field)
        writer.write_enum_value("id", self.id)
        writer.write_int_value("maxKey", self.max_key)
        writer.write_int_value("nextKey", self.next_key)
    

