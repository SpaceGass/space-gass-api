from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .library_match_type import LibraryMatchType

@dataclass
class LibrarySearchSummary(Parsable):
    """
    Describes the outcome of one library search.
    """
    # How a search result matched the query, from strongest to weakest. Results are orderedby match type first, then by score.Matching is case-insensitive and ignores spaces and separator characters(`. - _ * , /`), so `310ub40.4` matches `310 UB 40.4`.
    top_match_type: Optional[LibraryMatchType] = None
    # The number of items that matched, before limit is applied.
    total_matches: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LibrarySearchSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LibrarySearchSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LibrarySearchSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .library_match_type import LibraryMatchType

        from .library_match_type import LibraryMatchType

        fields: dict[str, Callable[[Any], None]] = {
            "topMatchType": lambda n : setattr(self, 'top_match_type', n.get_enum_value(LibraryMatchType)),
            "totalMatches": lambda n : setattr(self, 'total_matches', n.get_int_value()),
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
        writer.write_enum_value("topMatchType", self.top_match_type)
        writer.write_int_value("totalMatches", self.total_matches)
    

