from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode
    from .filter_steel_member_type import FilterSteelMemberType

@dataclass
class FilterSteelMembersUpdate(Parsable):
    """
    Partial update for the Steel Members sub-filter.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    # Steel-member design-state categories available as a Filter resource criterion.Mirrors SG's `SGItemFilter_SteelMemberTypes` verbatim — note SG's enumname is plural; the API name is singular for consistency with the other`Filter*Type` enums.
    steel_member_type: Optional[FilterSteelMemberType] = None
    # The steelMembers property
    steel_members: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterSteelMembersUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterSteelMembersUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterSteelMembersUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode
        from .filter_steel_member_type import FilterSteelMemberType

        from .filter_mode import FilterMode
        from .filter_steel_member_type import FilterSteelMemberType

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "steelMemberType": lambda n : setattr(self, 'steel_member_type', n.get_enum_value(FilterSteelMemberType)),
            "steelMembers": lambda n : setattr(self, 'steel_members', n.get_str_value()),
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
        writer.write_enum_value("mode", self.mode)
        writer.write_enum_value("steelMemberType", self.steel_member_type)
        writer.write_str_value("steelMembers", self.steel_members)
    

