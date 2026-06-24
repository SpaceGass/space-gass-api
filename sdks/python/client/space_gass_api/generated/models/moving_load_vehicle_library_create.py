from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadVehicleLibraryCreate(Parsable):
    """
    Imports a vehicle from a vehicle library by name. The imported wheel loads are convertedto the current job units.
    """
    # The Id to assign to the new item.
    id: Optional[int] = None
    # The library name to import from.
    library: Optional[str] = None
    # The vehicle item name within the library.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadVehicleLibraryCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadVehicleLibraryCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadVehicleLibraryCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_str_value("library", self.library)
        writer.write_str_value("name", self.name)
    

