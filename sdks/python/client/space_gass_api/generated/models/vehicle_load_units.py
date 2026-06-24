from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .force_unit import ForceUnit
    from .length_unit import LengthUnit
    from .moment_unit import MomentUnit

@dataclass
class VehicleLoadUnits(Parsable):
    """
    The units a vehicle's wheel loads are stored in. Independent of the job-level units.
    """
    # Force unit. Members mirror SPACE GASS `SgForce`.
    force: Optional[ForceUnit] = None
    # Length unit. Members mirror SPACE GASS `SGLength`(`NetCommon/CommonEnums.vb`); integer values and identifiers must stay inlock-step with it. The System.ComponentModel.DescriptionAttribute carries the displaylabel (mirrors `gcUNITS_LABEL_*`).
    length: Optional[LengthUnit] = None
    # Moment unit. Members mirror SPACE GASS `SgMoment`.
    moment: Optional[MomentUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VehicleLoadUnits:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VehicleLoadUnits
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VehicleLoadUnits()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .force_unit import ForceUnit
        from .length_unit import LengthUnit
        from .moment_unit import MomentUnit

        from .force_unit import ForceUnit
        from .length_unit import LengthUnit
        from .moment_unit import MomentUnit

        fields: dict[str, Callable[[Any], None]] = {
            "force": lambda n : setattr(self, 'force', n.get_enum_value(ForceUnit)),
            "length": lambda n : setattr(self, 'length', n.get_enum_value(LengthUnit)),
            "moment": lambda n : setattr(self, 'moment', n.get_enum_value(MomentUnit)),
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
        writer.write_enum_value("force", self.force)
        writer.write_enum_value("length", self.length)
        writer.write_enum_value("moment", self.moment)
    

