from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelMemberDesignIterationSettingsUpdate(Parsable):
    """
    Update request for the steel member design iteration settings.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # The autoIterate property
    auto_iterate: Optional[bool] = None
    # The bucklingLoadFactorLimit property
    buckling_load_factor_limit: Optional[float] = None
    # The iterations property
    iterations: Optional[int] = None
    # The rerunBucklingAnalysis property
    rerun_buckling_analysis: Optional[bool] = None
    # The rerunStaticAnalysis property
    rerun_static_analysis: Optional[bool] = None
    # The rerunSteelMemberDesign property
    rerun_steel_member_design: Optional[bool] = None
    # The warnLowBucklingLoadFactor property
    warn_low_buckling_load_factor: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignIterationSettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignIterationSettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignIterationSettingsUpdate()
    
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
    

