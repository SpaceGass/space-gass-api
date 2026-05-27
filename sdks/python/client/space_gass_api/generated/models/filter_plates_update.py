from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode
    from .filter_plate_type import FilterPlateType

@dataclass
class FilterPlatesUpdate(Parsable):
    """
    Partial update for the Plates sub-filter.
    """
    # Whether this sub-filter participates in the filter.
    is_active: Optional[bool] = None
    # Whether a sub-filter block includes or excludes matching entities.
    mode: Optional[FilterMode] = None
    # Plate type categories available as a Filter resource criterion.Mirrors SG's `SGItemFilter_PlateType` verbatim. Richer thanthe entity-property SpaceGassApi.Models.Enums.PlateType / SpaceGassApi.Models.Enums.PlateTheorybecause the filter surface includes validity / orientation states.
    plate_type: Optional[FilterPlateType] = None
    # The plates property
    plates: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterPlatesUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterPlatesUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterPlatesUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode
        from .filter_plate_type import FilterPlateType

        from .filter_mode import FilterMode
        from .filter_plate_type import FilterPlateType

        fields: dict[str, Callable[[Any], None]] = {
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "plateType": lambda n : setattr(self, 'plate_type', n.get_enum_value(FilterPlateType)),
            "plates": lambda n : setattr(self, 'plates', n.get_str_value()),
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
        writer.write_enum_value("plateType", self.plate_type)
        writer.write_str_value("plates", self.plates)
    

