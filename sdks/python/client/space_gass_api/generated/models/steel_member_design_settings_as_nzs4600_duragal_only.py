from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

@dataclass
class SteelMemberDesignSettingsAsNzs4600DuragalOnly(SteelMemberDesignSettingsBase, Parsable):
    """
    Steel member design settings for AS/NZS 4600 (Duragal only).
    """
    # Selects this object type. Always "AsNzs4600DuragalOnly".
    code: Optional[SteelMemberDesignSettingsAsNzs4600DuragalOnly_code] = SteelMemberDesignSettingsAsNzs4600DuragalOnly_code("AsNzs4600DuragalOnly")
    # Calculate Cb for clause D2.1.1 (otherwise specify Cb).
    calculate_cb: Optional[bool] = None
    # Calculate Cm and alpha for clause 3.5.1 (otherwise Cm=1, alpha=1, Nc limited to <= group length).
    calculate_cm_and_alpha: Optional[bool] = None
    # Cb.
    cb: Optional[float] = None
    # Consider distortional buckling if applicable.
    consider_distortional_buckling: Optional[bool] = None
    # Consider eccentric effects.
    consider_eccentric_effects: Optional[bool] = None
    # Convert compression effective lengths to principal axes.
    convert_compression_effective_lengths: Optional[bool] = None
    # Compression (clause 3.4.2).
    distortional_buckling_compression: Optional[bool] = None
    # Lateral displacement (clause 3.3.3.3(b)).
    distortional_buckling_lateral_displacement: Optional[bool] = None
    # Rotation (clause 3.3.3.3(a)).
    distortional_buckling_rotation: Optional[bool] = None
    # kv.
    kv: Optional[float] = None
    # R downward (R-factor method).
    r_factor_downward: Optional[float] = None
    # R upward (R-factor method).
    r_factor_upward: Optional[float] = None
    # Reduce fy, fu for G550 steel < 0.9 mm thick (clause 1.5.1.1(b)(i)).
    reduce_g550_strengths: Optional[bool] = None
    # Use clause D2.1.1.3 for Zeds instead of clause D2.1.1.2(a).
    use_clause_d2_1_1_3_for_zeds: Optional[bool] = None
    # Use clause 3.4.3 for Cees and Zeds.
    use_clause3_4_3_for_cees_and_zeds: Optional[bool] = None
    # Use alternative eq 2.3.2.2(8) for plain channels if applicable.
    use_equation2_3_2_2_8_for_plain_channels: Optional[bool] = None
    # Use Kt factor for tension members.
    use_kt_factor_for_tension: Optional[bool] = None
    # Use kv = 5.34 from clause 3.3.4.1 (otherwise specify kv).
    use_kv_from_clause3_3_4_1: Optional[bool] = None
    # Use non-principal axes for Z sections with continuous lateral restraint.
    use_non_principal_axes_for_z_sections: Optional[bool] = None
    # Use clause 3.3.3.4 instead of clause 3.3.3.2.1.
    use_r_factor_method: Optional[bool] = None
    # Use segment length instead of ley, lez clause D2.1.1.2(a) for Cees and Zeds.
    use_segment_length_for_cees_and_zeds: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAsNzs4600DuragalOnly:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAsNzs4600DuragalOnly
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAsNzs4600DuragalOnly()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

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
    

