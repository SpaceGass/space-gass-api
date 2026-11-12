from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .as3990_reduction_skip import As3990ReductionSkip
    from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

@dataclass
class SteelMemberDesignSettingsAs3990(SteelMemberDesignSettingsBase, Parsable):
    """
    Steel member design settings for AS3990.
    """
    # Selects this object type. Always "As3990".
    code: Optional[SteelMemberDesignSettingsAs3990_code] = SteelMemberDesignSettingsAs3990_code("As3990")
    # Add eccentric moments for tension members.
    add_eccentric_moments: Optional[bool] = None
    # Assume fully stiffened webs for shear checks.
    assume_fully_stiffened_webs: Optional[bool] = None
    # Consider eccentric effects.
    consider_eccentric_effects: Optional[bool] = None
    # Convert CHS biaxial moments to mono if possible.
    convert_chs_biaxial_moments_to_mono: Optional[bool] = None
    # Which AS3990 clause 4.3.2 reductions are skipped. AS1250 uses the same setting.
    skip_clause4_3_2_reductions: Optional[As3990ReductionSkip] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAs3990:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAs3990
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAs3990()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .as3990_reduction_skip import As3990ReductionSkip
        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        from .as3990_reduction_skip import As3990ReductionSkip
        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "assumeFullyStiffenedWebs": lambda n : setattr(self, 'assume_fully_stiffened_webs', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertChsBiaxialMomentsToMono": lambda n : setattr(self, 'convert_chs_biaxial_moments_to_mono', n.get_bool_value()),
            "skipClause4_3_2Reductions": lambda n : setattr(self, 'skip_clause4_3_2_reductions', n.get_enum_value(As3990ReductionSkip)),
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
        writer.write_bool_value("assumeFullyStiffenedWebs", self.assume_fully_stiffened_webs)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertChsBiaxialMomentsToMono", self.convert_chs_biaxial_moments_to_mono)
        writer.write_enum_value("skipClause4_3_2Reductions", self.skip_clause4_3_2_reductions)
    

