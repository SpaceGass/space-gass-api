from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode

@dataclass
class FilterMaterialsUpdate(Parsable):
    """
    Partial update for the Materials sub-filter.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # The materials property
    materials: Optional[str] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterMaterialsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterMaterialsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterMaterialsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode

        from .filter_mode import FilterMode

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "materials": lambda n : setattr(self, 'materials', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
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
        writer.write_bool_value("isActive", self.is_active)
        writer.write_str_value("materials", self.materials)
        writer.write_enum_value("mode", self.mode)
    

