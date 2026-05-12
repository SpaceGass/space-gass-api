from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelCheckSummary(Parsable):
    """
    Steel member design check summary.
    """
    # Load case ID of the critical case.
    critical_case: Optional[int] = None
    # Failure mode description.
    failure: Optional[str] = None
    # Design check status flag.
    flag: Optional[str] = None
    # Design load factor (capacity ratio).
    load_factor: Optional[float] = None
    # Member key (group key).
    member: Optional[int] = None
    # Section name used for the design check.
    section: Optional[str] = None
    # Critical segment length. Unit: Length (see GET /job/units).
    segment_length: Optional[float] = None
    # Total member length. Unit: Length (see GET /job/units).
    total_length: Optional[float] = None
    # Yield stress. Unit: Stress (see GET /job/units).
    yield_: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelCheckSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelCheckSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelCheckSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "criticalCase": lambda n : setattr(self, 'critical_case', n.get_int_value()),
            "failure": lambda n : setattr(self, 'failure', n.get_str_value()),
            "flag": lambda n : setattr(self, 'flag', n.get_str_value()),
            "loadFactor": lambda n : setattr(self, 'load_factor', n.get_float_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "section": lambda n : setattr(self, 'section', n.get_str_value()),
            "segmentLength": lambda n : setattr(self, 'segment_length', n.get_float_value()),
            "totalLength": lambda n : setattr(self, 'total_length', n.get_float_value()),
            "yield": lambda n : setattr(self, 'yield_', n.get_float_value()),
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
        writer.write_int_value("criticalCase", self.critical_case)
        writer.write_str_value("failure", self.failure)
        writer.write_str_value("flag", self.flag)
        writer.write_float_value("loadFactor", self.load_factor)
        writer.write_int_value("member", self.member)
        writer.write_str_value("section", self.section)
        writer.write_float_value("segmentLength", self.segment_length)
        writer.write_float_value("totalLength", self.total_length)
        writer.write_float_value("yield", self.yield_)
    

