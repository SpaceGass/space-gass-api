from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class VehicleWheelLoad(Parsable):
    """
    A single wheel load on a vehicle — its position and the force/moment components appliedthere. Values are in the vehicle's own units (see SpaceGassApi.Models.Dtos.MovingLoads.MovingLoadVehicleDto.LoadUnits).
    """
    # Force component along global X.
    fx: Optional[float] = None
    # Force component along global Y.
    fy: Optional[float] = None
    # Force component along global Z.
    fz: Optional[float] = None
    # Moment component about global X.
    mx: Optional[float] = None
    # Moment component about global Y.
    my: Optional[float] = None
    # Moment component about global Z.
    mz: Optional[float] = None
    # Wheel position along the vehicle's local X axis.
    x: Optional[float] = None
    # Wheel position along the vehicle's local Y axis.
    y: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VehicleWheelLoad:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VehicleWheelLoad
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VehicleWheelLoad()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fz": lambda n : setattr(self, 'fz', n.get_float_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "mz": lambda n : setattr(self, 'mz', n.get_float_value()),
            "x": lambda n : setattr(self, 'x', n.get_float_value()),
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
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
        writer.write_float_value("fx", self.fx)
        writer.write_float_value("fy", self.fy)
        writer.write_float_value("fz", self.fz)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("my", self.my)
        writer.write_float_value("mz", self.mz)
        writer.write_float_value("x", self.x)
        writer.write_float_value("y", self.y)
    

