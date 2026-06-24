from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadSettings(Parsable):
    """
    Collection-level moving-load settings — the options shown on the moving-load dialog: theglobal generation flags, the vertical-proximity tolerance, and the loading-area clippingpolygon. Per-field units are described by `GET moving-loads/settings/metadata`; themodel's current units are at `GET /job/units`.
    """
    # Apply member loads to the closest member only.
    apply_to_closest_member: Optional[bool] = None
    # Check vertical proximity when applying loads to members.
    check_vertical_proximity: Optional[bool] = None
    # Ignore loads that transfer load to just one member.
    ignore_loads_on_one_member: Optional[bool] = None
    # Ignore loads that are outside the loading area.
    ignore_outside_loaded_area: Optional[bool] = None
    # Keep loads entirely within the ends of the travel path (crane-beam behaviour).
    keep_loads_within_travel_path: Optional[bool] = None
    # Retain generated loads for deselected scenarios.
    retain_loads: Optional[bool] = None
    # Maximum vertical distance between a load and a member for the load to be applied.
    vertical_proximity: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "applyToClosestMember": lambda n : setattr(self, 'apply_to_closest_member', n.get_bool_value()),
            "checkVerticalProximity": lambda n : setattr(self, 'check_vertical_proximity', n.get_bool_value()),
            "ignoreLoadsOnOneMember": lambda n : setattr(self, 'ignore_loads_on_one_member', n.get_bool_value()),
            "ignoreOutsideLoadedArea": lambda n : setattr(self, 'ignore_outside_loaded_area', n.get_bool_value()),
            "keepLoadsWithinTravelPath": lambda n : setattr(self, 'keep_loads_within_travel_path', n.get_bool_value()),
            "retainLoads": lambda n : setattr(self, 'retain_loads', n.get_bool_value()),
            "verticalProximity": lambda n : setattr(self, 'vertical_proximity', n.get_float_value()),
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
        writer.write_bool_value("applyToClosestMember", self.apply_to_closest_member)
        writer.write_bool_value("checkVerticalProximity", self.check_vertical_proximity)
        writer.write_bool_value("ignoreLoadsOnOneMember", self.ignore_loads_on_one_member)
        writer.write_bool_value("ignoreOutsideLoadedArea", self.ignore_outside_loaded_area)
        writer.write_bool_value("keepLoadsWithinTravelPath", self.keep_loads_within_travel_path)
        writer.write_bool_value("retainLoads", self.retain_loads)
        writer.write_float_value("verticalProximity", self.vertical_proximity)
    

