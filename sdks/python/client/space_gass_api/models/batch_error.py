from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BatchError(Parsable):
    """
    Error details for a failed batch item.
    """
    # Error message describing what went wrong.
    error: Optional[str] = None
    # Entity Id of the failed item (for single-Id entities).
    id: Optional[int] = None
    # Id values of the failed item (for multi-Id entities).
    ids: Optional[list[int]] = None
    # Index of the item in the original request (0-based).
    index: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "ids": lambda n : setattr(self, 'ids', n.get_collection_of_primitive_values(int)),
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
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
        writer.write_str_value("error", self.error)
        writer.write_int_value("id", self.id)
        writer.write_collection_of_primitive_values("ids", self.ids)
        writer.write_int_value("index", self.index)
    

