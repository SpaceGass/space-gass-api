from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BucklingEffectiveLength(Parsable):
    """
    Buckling effective length result (FileId 217).
    """
    # Member length. Unit: Length (see GET /job/units).
    length: Optional[float] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Effective length about Y axis. Unit: Length (see GET /job/units).
    ly: Optional[float] = None
    # Effective length about Z axis. Unit: Length (see GET /job/units).
    lz: Optional[float] = None
    # Member key.
    member: Optional[int] = None
    # Buckling mode number.
    mode: Optional[int] = None
    # Critical buckling load. Unit: Force (see GET /job/units).
    pcr: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BucklingEffectiveLength:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BucklingEffectiveLength
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BucklingEffectiveLength()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "length": lambda n : setattr(self, 'length', n.get_float_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "ly": lambda n : setattr(self, 'ly', n.get_float_value()),
            "lz": lambda n : setattr(self, 'lz', n.get_float_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
            "pcr": lambda n : setattr(self, 'pcr', n.get_float_value()),
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
        writer.write_float_value("length", self.length)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("ly", self.ly)
        writer.write_float_value("lz", self.lz)
        writer.write_int_value("member", self.member)
        writer.write_int_value("mode", self.mode)
        writer.write_float_value("pcr", self.pcr)
    

