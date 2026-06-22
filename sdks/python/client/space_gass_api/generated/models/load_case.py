from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .combination_load_case_item import CombinationLoadCaseItem
    from .load_case_type import LoadCaseType

@dataclass
class LoadCase(Parsable):
    """
    DTO for a load case (from Loads - Titles table, FileID=28).Returns all load cases including primary, combination, and step types.When `Type` is `Combination`, the case owns a list of combination items(hydrated inline via `?expand=all`).
    """
    # The combination items (component case + multiplying factor rows) that make up this case.Populated only when `?expand=all` is passed AND `hasCombinationItems` is true;omitted from the wire otherwise.
    combination_items: Optional[list[CombinationLoadCaseItem]] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # True when this case has at least one combination item defined.Only meaningful for cases where `Type` is `Combination`.Use `?expand=all` to include the full `combinationItems` array.
    has_combination_items: Optional[bool] = None
    # Primary identifier - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    id: Optional[int] = None
    # Load case notes (supports multi-line text).
    notes: Optional[str] = None
    # Load case title.
    title: Optional[str] = None
    # Type of load case in the structural model.Read-only — computed internally by SPACE GASS based on assigned loads.
    type: Optional[LoadCaseType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoadCase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoadCase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoadCase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .combination_load_case_item import CombinationLoadCaseItem
        from .load_case_type import LoadCaseType

        from .combination_load_case_item import CombinationLoadCaseItem
        from .load_case_type import LoadCaseType

        fields: dict[str, Callable[[Any], None]] = {
            "combinationItems": lambda n : setattr(self, 'combination_items', n.get_collection_of_object_values(CombinationLoadCaseItem)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "hasCombinationItems": lambda n : setattr(self, 'has_combination_items', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(LoadCaseType)),
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
        writer.write_bool_value("hasCombinationItems", self.has_combination_items)
        writer.write_int_value("id", self.id)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("title", self.title)
        writer.write_enum_value("type", self.type)
    

