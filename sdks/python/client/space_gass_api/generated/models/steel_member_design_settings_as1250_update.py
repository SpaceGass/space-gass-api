from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .as3990_reduction_skip import As3990ReductionSkip
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsAs1250Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the AS1250 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not an AS1250 setting is rejected.
    """
    # Selects this object type. Always "As1250".
    code: Optional[SteelMemberDesignSettingsAs1250Update_code] = SteelMemberDesignSettingsAs1250Update_code("As1250")
    # The addEccentricMoments property
    add_eccentric_moments: Optional[bool] = None
    # The assumeFullyStiffenedWebs property
    assume_fully_stiffened_webs: Optional[bool] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertChsBiaxialMomentsToMono property
    convert_chs_biaxial_moments_to_mono: Optional[bool] = None
    # Which AS3990 clause 4.3.2 reductions are skipped. AS1250 uses the same setting.
    skip_clause4_3_2_reductions: Optional[As3990ReductionSkip] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAs1250Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAs1250Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAs1250Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .as3990_reduction_skip import As3990ReductionSkip
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .as3990_reduction_skip import As3990ReductionSkip
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

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
    

