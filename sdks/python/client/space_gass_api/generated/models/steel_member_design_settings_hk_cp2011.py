from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

@dataclass
class SteelMemberDesignSettingsHkCp2011(SteelMemberDesignSettingsBase, Parsable):
    """
    Steel member design settings for HK CP2011.
    """
    # Selects this object type. Always "HkCp2011".
    code: Optional[SteelMemberDesignSettingsHkCp2011_code] = SteelMemberDesignSettingsHkCp2011_code("HkCp2011")
    # Add eccentric moments for tension members.
    add_eccentric_moments: Optional[bool] = None
    # Calculate mLT moment factor (otherwise mLT=1.0).
    calculate_mlt_factor: Optional[bool] = None
    # Calculate Pcbar in eq 8.80 based on group length only.
    calculate_pcbar_from_group_length: Optional[bool] = None
    # Consider eccentric effects.
    consider_eccentric_effects: Optional[bool] = None
    # Use clause 6.8.3 instead of clause 8.9.2.
    use_clause6_8_3: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsHkCp2011:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsHkCp2011
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsHkCp2011()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "calculateMltFactor": lambda n : setattr(self, 'calculate_mlt_factor', n.get_bool_value()),
            "calculatePcbarFromGroupLength": lambda n : setattr(self, 'calculate_pcbar_from_group_length', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "useClause6_8_3": lambda n : setattr(self, 'use_clause6_8_3', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("addEccentricMoments", self.add_eccentric_moments)
        writer.write_bool_value("calculateMltFactor", self.calculate_mlt_factor)
        writer.write_bool_value("calculatePcbarFromGroupLength", self.calculate_pcbar_from_group_length)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("useClause6_8_3", self.use_clause6_8_3)
    

