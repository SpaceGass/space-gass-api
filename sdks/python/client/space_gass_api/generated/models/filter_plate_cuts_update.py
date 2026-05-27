from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode
    from .filter_plate_cut_type import FilterPlateCutType

@dataclass
class FilterPlateCutsUpdate(Parsable):
    """
    Partial update for the Plate Cuts sub-filter.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    # Plate-cut categories available as a Filter resource criterion.Mirrors SG's `SGItemFilter_PlateCutType` verbatim (identicalmembers to SpaceGassApi.Models.Enums.Filters.FilterPlateStripType at the SG layer, butkept as a distinct type so future SG additions don't require anAPI refactor).
    plate_cut_type: Optional[FilterPlateCutType] = None
    # The plateCuts property
    plate_cuts: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterPlateCutsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterPlateCutsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterPlateCutsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode
        from .filter_plate_cut_type import FilterPlateCutType

        from .filter_mode import FilterMode
        from .filter_plate_cut_type import FilterPlateCutType

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "plateCutType": lambda n : setattr(self, 'plate_cut_type', n.get_enum_value(FilterPlateCutType)),
            "plateCuts": lambda n : setattr(self, 'plate_cuts', n.get_str_value()),
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
        writer.write_enum_value("plateCutType", self.plate_cut_type)
        writer.write_str_value("plateCuts", self.plate_cuts)
    

