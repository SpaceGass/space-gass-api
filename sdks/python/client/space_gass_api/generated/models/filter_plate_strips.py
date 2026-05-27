from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode
    from .filter_plate_strip_type import FilterPlateStripType

@dataclass
class FilterPlateStrips(Parsable):
    """
    Sub-filter carrying a list of plate-strip Ids and a strip-typecategorical filter.Maps to SG `SGFilterType.PlateStrip`.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    # Plate-strip categories available as a Filter resource criterion.Mirrors SG's `SGItemFilter_PlateStripType` verbatim.
    plate_strip_type: Optional[FilterPlateStripType] = None
    # Plate-strip Ids in SG list format. Empty string means no Id criterion.
    plate_strips: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterPlateStrips:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterPlateStrips
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterPlateStrips()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode
        from .filter_plate_strip_type import FilterPlateStripType

        from .filter_mode import FilterMode
        from .filter_plate_strip_type import FilterPlateStripType

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "plateStripType": lambda n : setattr(self, 'plate_strip_type', n.get_enum_value(FilterPlateStripType)),
            "plateStrips": lambda n : setattr(self, 'plate_strips', n.get_str_value()),
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
        writer.write_enum_value("plateStripType", self.plate_strip_type)
        writer.write_str_value("plateStrips", self.plate_strips)
    

