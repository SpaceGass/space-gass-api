from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .combination_load_case_item import CombinationLoadCaseItem

@dataclass
class CombinationLoadCaseUpdate(Parsable):
    """
    Request payload for updating a combination load case.Inherits Id, Title and Notes from SpaceGassApi.Models.Dtos.Entity.Loads.LoadCaseUpdateDto (each optional forpartial update) and adds an optional `combinationItems` list.
    """
    # Replacement combination items for this case. Omit to leave items unchanged.
    combination_items: Optional[list[CombinationLoadCaseItem]] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Load case notes (supports multi-line text).
    notes: Optional[str] = None
    # Load case title.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CombinationLoadCaseUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CombinationLoadCaseUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CombinationLoadCaseUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .combination_load_case_item import CombinationLoadCaseItem

        from .combination_load_case_item import CombinationLoadCaseItem

        fields: dict[str, Callable[[Any], None]] = {
            "combinationItems": lambda n : setattr(self, 'combination_items', n.get_collection_of_object_values(CombinationLoadCaseItem)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("combinationItems", self.combination_items)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("title", self.title)
    

