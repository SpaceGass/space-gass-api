from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .design_check_status import DesignCheckStatus

@dataclass
class SteelCheckSummary(Parsable):
    """
    Steel member design check summary: one row per steel member (design group) the runchecked. Steel members are the design groups at GET /job/design/steel-members.
    """
    # Load case Id of the critical case.
    critical_case: Optional[int] = None
    # Governing failure mode description.
    failure: Optional[str] = None
    # Design load factor: the factor by which the design actions could be increased before the steel member fails, so 1 is at capacity and below 1 is overloaded; the check fails when it is below the design settings' loadFactorLimit. For the permissible-stress codes (AISC-ASD, AS1250, SABS0162, AS3990) it is the combined stress ratio instead, where above 1 is overloaded.
    load_factor: Optional[float] = None
    # The section the check was made with: the steel member's section for a Check run, or the section the design selected for a Design run.
    section: Optional[str] = None
    # Whether `section` differs from the section the steel member's analysis members carry in the model: `true` when the design selected a different section (the model has not been updated to it), `false` when they match, `null` when the steel member or its members no longer exist in the model (the results predate a change to it).
    section_differs_from_model: Optional[bool] = None
    # Critical segment length. Unit: Length (see GET /job/units).
    segment_length: Optional[float] = None
    # Outcome of a design check for one entity — a steel member (design group) in steel member design.
    status: Optional[DesignCheckStatus] = None
    # Steel member (design group) Id, as used by GET /job/design/steel-members/{id}.
    steel_member: Optional[int] = None
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
        from .design_check_status import DesignCheckStatus

        from .design_check_status import DesignCheckStatus

        fields: dict[str, Callable[[Any], None]] = {
            "criticalCase": lambda n : setattr(self, 'critical_case', n.get_int_value()),
            "failure": lambda n : setattr(self, 'failure', n.get_str_value()),
            "loadFactor": lambda n : setattr(self, 'load_factor', n.get_float_value()),
            "section": lambda n : setattr(self, 'section', n.get_str_value()),
            "sectionDiffersFromModel": lambda n : setattr(self, 'section_differs_from_model', n.get_bool_value()),
            "segmentLength": lambda n : setattr(self, 'segment_length', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DesignCheckStatus)),
            "steelMember": lambda n : setattr(self, 'steel_member', n.get_int_value()),
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
        writer.write_float_value("loadFactor", self.load_factor)
        writer.write_str_value("section", self.section)
        writer.write_bool_value("sectionDiffersFromModel", self.section_differs_from_model)
        writer.write_float_value("segmentLength", self.segment_length)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("steelMember", self.steel_member)
        writer.write_float_value("totalLength", self.total_length)
        writer.write_float_value("yield", self.yield_)
    

