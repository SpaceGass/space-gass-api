from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelMemberDesignIterationSettings(Parsable):
    """
    Steel member design iteration settings — what follows a steel member design run:re-running the analyses and the design with the newly selected sections, anditerating until the design settles.
    """
    # Whether to repeat the analysis / design cycle automatically until the design settles.
    auto_iterate: Optional[bool] = None
    # Lowest acceptable buckling load factor.
    buckling_load_factor_limit: Optional[float] = None
    # Maximum number of analysis / design iterations.
    iterations: Optional[int] = None
    # Whether to re-run the buckling analysis with the updated sections.
    rerun_buckling_analysis: Optional[bool] = None
    # Whether to re-run the static analysis with the updated sections.
    rerun_static_analysis: Optional[bool] = None
    # Whether to re-run the steel member design after the analyses.
    rerun_steel_member_design: Optional[bool] = None
    # Whether to warn when the lowest buckling load factor falls below bucklingLoadFactorLimit.
    warn_low_buckling_load_factor: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignIterationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignIterationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignIterationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "autoIterate": lambda n : setattr(self, 'auto_iterate', n.get_bool_value()),
            "bucklingLoadFactorLimit": lambda n : setattr(self, 'buckling_load_factor_limit', n.get_float_value()),
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "rerunBucklingAnalysis": lambda n : setattr(self, 'rerun_buckling_analysis', n.get_bool_value()),
            "rerunStaticAnalysis": lambda n : setattr(self, 'rerun_static_analysis', n.get_bool_value()),
            "rerunSteelMemberDesign": lambda n : setattr(self, 'rerun_steel_member_design', n.get_bool_value()),
            "warnLowBucklingLoadFactor": lambda n : setattr(self, 'warn_low_buckling_load_factor', n.get_bool_value()),
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
        writer.write_bool_value("autoIterate", self.auto_iterate)
        writer.write_float_value("bucklingLoadFactorLimit", self.buckling_load_factor_limit)
        writer.write_int_value("iterations", self.iterations)
        writer.write_bool_value("rerunBucklingAnalysis", self.rerun_buckling_analysis)
        writer.write_bool_value("rerunStaticAnalysis", self.rerun_static_analysis)
        writer.write_bool_value("rerunSteelMemberDesign", self.rerun_steel_member_design)
        writer.write_bool_value("warnLowBucklingLoadFactor", self.warn_low_buckling_load_factor)
    

