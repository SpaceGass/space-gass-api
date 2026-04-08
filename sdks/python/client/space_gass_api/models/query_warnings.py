from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class QueryWarnings(Parsable):
    """
    Warnings returned when query filter parameters reference keys or load casesthat do not exist in the result set.
    """
    # Load case IDs that were requested but produced no results.
    invalid_cases: Optional[list[int]] = None
    # Entity keys that were requested but produced no results.
    invalid_keys: Optional[list[int]] = None
    # Mode numbers that were requested but produced no results.
    invalid_modes: Optional[list[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QueryWarnings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QueryWarnings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QueryWarnings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "invalidCases": lambda n : setattr(self, 'invalid_cases', n.get_collection_of_primitive_values(int)),
            "invalidKeys": lambda n : setattr(self, 'invalid_keys', n.get_collection_of_primitive_values(int)),
            "invalidModes": lambda n : setattr(self, 'invalid_modes', n.get_collection_of_primitive_values(int)),
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
        writer.write_collection_of_primitive_values("invalidCases", self.invalid_cases)
        writer.write_collection_of_primitive_values("invalidKeys", self.invalid_keys)
        writer.write_collection_of_primitive_values("invalidModes", self.invalid_modes)
    

