from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .reaction_summary_type import ReactionSummaryType

@dataclass
class ReactionSummary(Parsable):
    """
    One row of the per-load-case equilibrium summary (FileId 205). SPACE GASS reportsthree aggregate totals per load case alongside the per-node reactions — the sum ofapplied loads, the sum of support reactions, and the maximum residuals — distinguishedby SummaryType. These are whole-model totals, not reactions at a realnode; see SpaceGassApi.Models.Dtos.Query.Analysis.NodeReactionDto for per-node values.
    """
    # Force component in X direction. Unit: Force (see GET /job/units).
    fx: Optional[float] = None
    # Force component in Y direction. Unit: Force (see GET /job/units).
    fy: Optional[float] = None
    # Force component in Z direction. Unit: Force (see GET /job/units).
    fz: Optional[float] = None
    # Load case Id.
    load_case: Optional[int] = None
    # Moment component about X axis. Unit: Moment (see GET /job/units).
    mx: Optional[float] = None
    # Moment component about Y axis. Unit: Moment (see GET /job/units).
    my: Optional[float] = None
    # Moment component about Z axis. Unit: Moment (see GET /job/units).
    mz: Optional[float] = None
    # Identifies which per-load-case equilibrium total a reaction summary row holds.
    summary_type: Optional[ReactionSummaryType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReactionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReactionSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReactionSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .reaction_summary_type import ReactionSummaryType

        from .reaction_summary_type import ReactionSummaryType

        fields: dict[str, Callable[[Any], None]] = {
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fz": lambda n : setattr(self, 'fz', n.get_float_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "mz": lambda n : setattr(self, 'mz', n.get_float_value()),
            "summaryType": lambda n : setattr(self, 'summary_type', n.get_enum_value(ReactionSummaryType)),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("my", self.my)
        writer.write_float_value("mz", self.mz)
        writer.write_enum_value("summaryType", self.summary_type)
    

