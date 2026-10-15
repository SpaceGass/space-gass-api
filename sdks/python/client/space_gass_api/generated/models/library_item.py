from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .library_availability import LibraryAvailability

@dataclass
class LibraryItem(Parsable):
    """
    One library item: its name plus the library and group it belongs to. This is theidentity the job-side create endpoints accept.
    """
    # Commercial availability of a library section — whether it is still produced.
    availability: Optional[LibraryAvailability] = None
    # The group the item belongs to.
    group: Optional[str] = None
    # The library the item belongs to.
    library: Optional[str] = None
    # The item's name as stored in the library.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LibraryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LibraryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LibraryItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .library_availability import LibraryAvailability

        from .library_availability import LibraryAvailability

        fields: dict[str, Callable[[Any], None]] = {
            "availability": lambda n : setattr(self, 'availability', n.get_enum_value(LibraryAvailability)),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_enum_value("availability", self.availability)
        writer.write_str_value("group", self.group)
        writer.write_str_value("library", self.library)
        writer.write_str_value("name", self.name)
    

