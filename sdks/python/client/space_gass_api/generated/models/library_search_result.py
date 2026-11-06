from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .library_item import LibraryItem
    from .library_search_summary import LibrarySearchSummary

@dataclass
class LibrarySearchResult(Parsable):
    """
    The result of a library search: a summary of the outcome plus thematching items, strongest match first.
    """
    # The matching items, strongest match first — or, when the request had no searchtext, every item in scope in library order.
    items: Optional[list[LibraryItem]] = None
    # Describes the outcome of one library search.
    summary: Optional[LibrarySearchSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LibrarySearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LibrarySearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LibrarySearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .library_item import LibraryItem
        from .library_search_summary import LibrarySearchSummary

        from .library_item import LibraryItem
        from .library_search_summary import LibrarySearchSummary

        fields: dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(LibraryItem)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(LibrarySearchSummary)),
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
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("summary", self.summary)
    

