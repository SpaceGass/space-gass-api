from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberIntermediateDisplacement(Parsable):
    """
    Member intermediate displacement results grouped by load case and member.Columnar arrays hold displacement values at each station along the member.
    """
    # Load case ID.
    case: Optional[int] = None
    # Distance along member at each station. Unit: Length (see GET /job/units).
    location: Optional[list[float]] = None
    # Member key.
    member: Optional[int] = None
    # Station index at each output point.
    station: Optional[list[int]] = None
    # Global translational X displacement at each station. Unit: Translation (see GET /job/units).
    tx_global: Optional[list[float]] = None
    # Local translational X displacement at each station. Unit: Translation (see GET /job/units).
    tx_local: Optional[list[float]] = None
    # Global translational Y displacement at each station. Unit: Translation (see GET /job/units).
    ty_global: Optional[list[float]] = None
    # Local translational Y displacement at each station. Unit: Translation (see GET /job/units).
    ty_local: Optional[list[float]] = None
    # Global translational Z displacement at each station. Unit: Translation (see GET /job/units).
    tz_global: Optional[list[float]] = None
    # Local translational Z displacement at each station. Unit: Translation (see GET /job/units).
    tz_local: Optional[list[float]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberIntermediateDisplacement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberIntermediateDisplacement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberIntermediateDisplacement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "location": lambda n : setattr(self, 'location', n.get_collection_of_primitive_values(float)),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "station": lambda n : setattr(self, 'station', n.get_collection_of_primitive_values(int)),
            "txGlobal": lambda n : setattr(self, 'tx_global', n.get_collection_of_primitive_values(float)),
            "txLocal": lambda n : setattr(self, 'tx_local', n.get_collection_of_primitive_values(float)),
            "tyGlobal": lambda n : setattr(self, 'ty_global', n.get_collection_of_primitive_values(float)),
            "tyLocal": lambda n : setattr(self, 'ty_local', n.get_collection_of_primitive_values(float)),
            "tzGlobal": lambda n : setattr(self, 'tz_global', n.get_collection_of_primitive_values(float)),
            "tzLocal": lambda n : setattr(self, 'tz_local', n.get_collection_of_primitive_values(float)),
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
        writer.write_int_value("case", self.case)
        writer.write_collection_of_primitive_values("location", self.location)
        writer.write_int_value("member", self.member)
        writer.write_collection_of_primitive_values("station", self.station)
        writer.write_collection_of_primitive_values("txGlobal", self.tx_global)
        writer.write_collection_of_primitive_values("txLocal", self.tx_local)
        writer.write_collection_of_primitive_values("tyGlobal", self.ty_global)
        writer.write_collection_of_primitive_values("tyLocal", self.ty_local)
        writer.write_collection_of_primitive_values("tzGlobal", self.tz_global)
        writer.write_collection_of_primitive_values("tzLocal", self.tz_local)
    

