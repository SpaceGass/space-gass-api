from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode

@dataclass
class FilterAxisRangeUpdate(Parsable):
    """
    Partial update for an axis-range sub-filter (X, Y or Z).
    """
    # Whether the upper bound is inclusive.
    high_inclusive: Optional[bool] = None
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Upper bound of the range. Unit: Length.
    limit_high: Optional[float] = None
    # Lower bound of the range. Unit: Length.
    limit_low: Optional[float] = None
    # Whether the lower bound is inclusive.
    low_inclusive: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterAxisRangeUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterAxisRangeUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterAxisRangeUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode

        from .filter_mode import FilterMode

        fields: dict[str, Callable[[Any], None]] = {
            "highInclusive": lambda n : setattr(self, 'high_inclusive', n.get_bool_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "limitHigh": lambda n : setattr(self, 'limit_high', n.get_float_value()),
            "limitLow": lambda n : setattr(self, 'limit_low', n.get_float_value()),
            "lowInclusive": lambda n : setattr(self, 'low_inclusive', n.get_bool_value()),
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
        writer.write_bool_value("highInclusive", self.high_inclusive)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_float_value("limitHigh", self.limit_high)
        writer.write_float_value("limitLow", self.limit_low)
        writer.write_bool_value("lowInclusive", self.low_inclusive)
        writer.write_enum_value("mode", self.mode)
    

