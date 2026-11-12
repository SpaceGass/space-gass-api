from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .is800_importance_factor import Is800ImportanceFactor
    from .is800_seismic_zone import Is800SeismicZone
    from .is800_single_angle_bolts import Is800SingleAngleBolts
    from .is800_single_angle_end_fixity import Is800SingleAngleEndFixity
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsIs800_2007Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the IS 800:2007 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not an IS 800:2007 setting is rejected.
    """
    # Selects this object type. Always "Is800_2007".
    code: Optional[SteelMemberDesignSettingsIs800_2007Update_code] = SteelMemberDesignSettingsIs800_2007Update_code("Is800_2007")
    # The addEccentricMoments property
    add_eccentric_moments: Optional[bool] = None
    # The calculateCmFactors property
    calculate_cm_factors: Optional[bool] = None
    # The calculateKFactors property
    calculate_k_factors: Optional[bool] = None
    # The calculateMcrUsingAnnexE property
    calculate_mcr_using_annex_e: Optional[bool] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertCompressionEffectiveLengths property
    convert_compression_effective_lengths: Optional[bool] = None
    # The importance factor used by the IS 800 seismic checks.
    importance_factor: Optional[Is800ImportanceFactor] = None
    # The performSeismicChecks property
    perform_seismic_checks: Optional[bool] = None
    # The reduceClass4ToClass3 property
    reduce_class4_to_class3: Optional[bool] = None
    # The IS 1893 seismic zone used by the IS 800 seismic checks.
    seismic_zone: Optional[Is800SeismicZone] = None
    # The number of bolts at each end of a single angle loaded through one leg (IS 800 clause 7.5.1.2).
    single_angle_bolts_at_each_end: Optional[Is800SingleAngleBolts] = None
    # The member fixity of a single angle loaded through one leg (IS 800 clause 7.5.1.2).
    single_angle_end_fixity: Optional[Is800SingleAngleEndFixity] = None
    # The useClause7_5_1_2ForSingleAngles property
    use_clause7_5_1_2_for_single_angles: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsIs800_2007Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsIs800_2007Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsIs800_2007Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .is800_importance_factor import Is800ImportanceFactor
        from .is800_seismic_zone import Is800SeismicZone
        from .is800_single_angle_bolts import Is800SingleAngleBolts
        from .is800_single_angle_end_fixity import Is800SingleAngleEndFixity
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .is800_importance_factor import Is800ImportanceFactor
        from .is800_seismic_zone import Is800SeismicZone
        from .is800_single_angle_bolts import Is800SingleAngleBolts
        from .is800_single_angle_end_fixity import Is800SingleAngleEndFixity
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "calculateCmFactors": lambda n : setattr(self, 'calculate_cm_factors', n.get_bool_value()),
            "calculateKFactors": lambda n : setattr(self, 'calculate_k_factors', n.get_bool_value()),
            "calculateMcrUsingAnnexE": lambda n : setattr(self, 'calculate_mcr_using_annex_e', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertCompressionEffectiveLengths": lambda n : setattr(self, 'convert_compression_effective_lengths', n.get_bool_value()),
            "importanceFactor": lambda n : setattr(self, 'importance_factor', n.get_enum_value(Is800ImportanceFactor)),
            "performSeismicChecks": lambda n : setattr(self, 'perform_seismic_checks', n.get_bool_value()),
            "reduceClass4ToClass3": lambda n : setattr(self, 'reduce_class4_to_class3', n.get_bool_value()),
            "seismicZone": lambda n : setattr(self, 'seismic_zone', n.get_enum_value(Is800SeismicZone)),
            "singleAngleBoltsAtEachEnd": lambda n : setattr(self, 'single_angle_bolts_at_each_end', n.get_enum_value(Is800SingleAngleBolts)),
            "singleAngleEndFixity": lambda n : setattr(self, 'single_angle_end_fixity', n.get_enum_value(Is800SingleAngleEndFixity)),
            "useClause7_5_1_2ForSingleAngles": lambda n : setattr(self, 'use_clause7_5_1_2_for_single_angles', n.get_bool_value()),
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
        writer.write_bool_value("calculateCmFactors", self.calculate_cm_factors)
        writer.write_bool_value("calculateKFactors", self.calculate_k_factors)
        writer.write_bool_value("calculateMcrUsingAnnexE", self.calculate_mcr_using_annex_e)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertCompressionEffectiveLengths", self.convert_compression_effective_lengths)
        writer.write_enum_value("importanceFactor", self.importance_factor)
        writer.write_bool_value("performSeismicChecks", self.perform_seismic_checks)
        writer.write_bool_value("reduceClass4ToClass3", self.reduce_class4_to_class3)
        writer.write_enum_value("seismicZone", self.seismic_zone)
        writer.write_enum_value("singleAngleBoltsAtEachEnd", self.single_angle_bolts_at_each_end)
        writer.write_enum_value("singleAngleEndFixity", self.single_angle_end_fixity)
        writer.write_bool_value("useClause7_5_1_2ForSingleAngles", self.use_clause7_5_1_2_for_single_angles)
    

