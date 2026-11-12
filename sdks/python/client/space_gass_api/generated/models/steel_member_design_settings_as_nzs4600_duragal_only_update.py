from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the AS/NZS 4600 (Duragal only) steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not an AS/NZS 4600 (Duragal only) setting is rejected.
    """
    # Selects this object type. Always "AsNzs4600DuragalOnly".
    code: Optional[SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate_code] = SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate_code("AsNzs4600DuragalOnly")
    # The calculateCb property
    calculate_cb: Optional[bool] = None
    # The calculateCmAndAlpha property
    calculate_cm_and_alpha: Optional[bool] = None
    # The cb property
    cb: Optional[float] = None
    # The considerDistortionalBuckling property
    consider_distortional_buckling: Optional[bool] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertCompressionEffectiveLengths property
    convert_compression_effective_lengths: Optional[bool] = None
    # The distortionalBucklingCompression property
    distortional_buckling_compression: Optional[bool] = None
    # The distortionalBucklingLateralDisplacement property
    distortional_buckling_lateral_displacement: Optional[bool] = None
    # The distortionalBucklingRotation property
    distortional_buckling_rotation: Optional[bool] = None
    # The kv property
    kv: Optional[float] = None
    # The rFactorDownward property
    r_factor_downward: Optional[float] = None
    # The rFactorUpward property
    r_factor_upward: Optional[float] = None
    # The reduceG550Strengths property
    reduce_g550_strengths: Optional[bool] = None
    # The useClauseD2_1_1_3ForZeds property
    use_clause_d2_1_1_3_for_zeds: Optional[bool] = None
    # The useClause3_4_3ForCeesAndZeds property
    use_clause3_4_3_for_cees_and_zeds: Optional[bool] = None
    # The useEquation2_3_2_2_8ForPlainChannels property
    use_equation2_3_2_2_8_for_plain_channels: Optional[bool] = None
    # The useKtFactorForTension property
    use_kt_factor_for_tension: Optional[bool] = None
    # The useKvFromClause3_3_4_1 property
    use_kv_from_clause3_3_4_1: Optional[bool] = None
    # The useNonPrincipalAxesForZSections property
    use_non_principal_axes_for_z_sections: Optional[bool] = None
    # The useRFactorMethod property
    use_r_factor_method: Optional[bool] = None
    # The useSegmentLengthForCeesAndZeds property
    use_segment_length_for_cees_and_zeds: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "calculateCb": lambda n : setattr(self, 'calculate_cb', n.get_bool_value()),
            "calculateCmAndAlpha": lambda n : setattr(self, 'calculate_cm_and_alpha', n.get_bool_value()),
            "cb": lambda n : setattr(self, 'cb', n.get_float_value()),
            "considerDistortionalBuckling": lambda n : setattr(self, 'consider_distortional_buckling', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertCompressionEffectiveLengths": lambda n : setattr(self, 'convert_compression_effective_lengths', n.get_bool_value()),
            "distortionalBucklingCompression": lambda n : setattr(self, 'distortional_buckling_compression', n.get_bool_value()),
            "distortionalBucklingLateralDisplacement": lambda n : setattr(self, 'distortional_buckling_lateral_displacement', n.get_bool_value()),
            "distortionalBucklingRotation": lambda n : setattr(self, 'distortional_buckling_rotation', n.get_bool_value()),
            "kv": lambda n : setattr(self, 'kv', n.get_float_value()),
            "rFactorDownward": lambda n : setattr(self, 'r_factor_downward', n.get_float_value()),
            "rFactorUpward": lambda n : setattr(self, 'r_factor_upward', n.get_float_value()),
            "reduceG550Strengths": lambda n : setattr(self, 'reduce_g550_strengths', n.get_bool_value()),
            "useClauseD2_1_1_3ForZeds": lambda n : setattr(self, 'use_clause_d2_1_1_3_for_zeds', n.get_bool_value()),
            "useClause3_4_3ForCeesAndZeds": lambda n : setattr(self, 'use_clause3_4_3_for_cees_and_zeds', n.get_bool_value()),
            "useEquation2_3_2_2_8ForPlainChannels": lambda n : setattr(self, 'use_equation2_3_2_2_8_for_plain_channels', n.get_bool_value()),
            "useKtFactorForTension": lambda n : setattr(self, 'use_kt_factor_for_tension', n.get_bool_value()),
            "useKvFromClause3_3_4_1": lambda n : setattr(self, 'use_kv_from_clause3_3_4_1', n.get_bool_value()),
            "useNonPrincipalAxesForZSections": lambda n : setattr(self, 'use_non_principal_axes_for_z_sections', n.get_bool_value()),
            "useRFactorMethod": lambda n : setattr(self, 'use_r_factor_method', n.get_bool_value()),
            "useSegmentLengthForCeesAndZeds": lambda n : setattr(self, 'use_segment_length_for_cees_and_zeds', n.get_bool_value()),
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
        writer.write_bool_value("calculateCb", self.calculate_cb)
        writer.write_bool_value("calculateCmAndAlpha", self.calculate_cm_and_alpha)
        writer.write_float_value("cb", self.cb)
        writer.write_bool_value("considerDistortionalBuckling", self.consider_distortional_buckling)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertCompressionEffectiveLengths", self.convert_compression_effective_lengths)
        writer.write_bool_value("distortionalBucklingCompression", self.distortional_buckling_compression)
        writer.write_bool_value("distortionalBucklingLateralDisplacement", self.distortional_buckling_lateral_displacement)
        writer.write_bool_value("distortionalBucklingRotation", self.distortional_buckling_rotation)
        writer.write_float_value("kv", self.kv)
        writer.write_float_value("rFactorDownward", self.r_factor_downward)
        writer.write_float_value("rFactorUpward", self.r_factor_upward)
        writer.write_bool_value("reduceG550Strengths", self.reduce_g550_strengths)
        writer.write_bool_value("useClauseD2_1_1_3ForZeds", self.use_clause_d2_1_1_3_for_zeds)
        writer.write_bool_value("useClause3_4_3ForCeesAndZeds", self.use_clause3_4_3_for_cees_and_zeds)
        writer.write_bool_value("useEquation2_3_2_2_8ForPlainChannels", self.use_equation2_3_2_2_8_for_plain_channels)
        writer.write_bool_value("useKtFactorForTension", self.use_kt_factor_for_tension)
        writer.write_bool_value("useKvFromClause3_3_4_1", self.use_kv_from_clause3_3_4_1)
        writer.write_bool_value("useNonPrincipalAxesForZSections", self.use_non_principal_axes_for_z_sections)
        writer.write_bool_value("useRFactorMethod", self.use_r_factor_method)
        writer.write_bool_value("useSegmentLengthForCeesAndZeds", self.use_segment_length_for_cees_and_zeds)
    

