from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .eurocode3_bending_and_axial_compression_method import Eurocode3BendingAndAxialCompressionMethod
    from .eurocode3_lateral_torsional_buckling_method import Eurocode3LateralTorsionalBucklingMethod
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsEurocode3_2005Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the Eurocode 3:2005 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not a Eurocode 3:2005 setting is rejected.
    """
    # Selects this object type. Always "Eurocode3_2005".
    code: Optional[SteelMemberDesignSettingsEurocode3_2005Update_code] = SteelMemberDesignSettingsEurocode3_2005Update_code("Eurocode3_2005")
    # The addEccentricMoments property
    add_eccentric_moments: Optional[bool] = None
    # Which Eurocode 3 annex is used for bending and axial compression (clause 6.3.3).
    bending_and_axial_compression_method: Optional[Eurocode3BendingAndAxialCompressionMethod] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertCompressionEffectiveLengths property
    convert_compression_effective_lengths: Optional[bool] = None
    # Which Eurocode 3 clause 6.3.2 method is used for lateral torsional buckling.
    lateral_torsional_buckling_method: Optional[Eurocode3LateralTorsionalBucklingMethod] = None
    # The modifyReductionFactorF property
    modify_reduction_factor_f: Optional[bool] = None
    # The useTableB2 property
    use_table_b2: Optional[bool] = None
    # The useUkFactors property
    use_uk_factors: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsEurocode3_2005Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsEurocode3_2005Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsEurocode3_2005Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .eurocode3_bending_and_axial_compression_method import Eurocode3BendingAndAxialCompressionMethod
        from .eurocode3_lateral_torsional_buckling_method import Eurocode3LateralTorsionalBucklingMethod
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .eurocode3_bending_and_axial_compression_method import Eurocode3BendingAndAxialCompressionMethod
        from .eurocode3_lateral_torsional_buckling_method import Eurocode3LateralTorsionalBucklingMethod
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "bendingAndAxialCompressionMethod": lambda n : setattr(self, 'bending_and_axial_compression_method', n.get_enum_value(Eurocode3BendingAndAxialCompressionMethod)),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertCompressionEffectiveLengths": lambda n : setattr(self, 'convert_compression_effective_lengths', n.get_bool_value()),
            "lateralTorsionalBucklingMethod": lambda n : setattr(self, 'lateral_torsional_buckling_method', n.get_enum_value(Eurocode3LateralTorsionalBucklingMethod)),
            "modifyReductionFactorF": lambda n : setattr(self, 'modify_reduction_factor_f', n.get_bool_value()),
            "useTableB2": lambda n : setattr(self, 'use_table_b2', n.get_bool_value()),
            "useUkFactors": lambda n : setattr(self, 'use_uk_factors', n.get_bool_value()),
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
        writer.write_enum_value("bendingAndAxialCompressionMethod", self.bending_and_axial_compression_method)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertCompressionEffectiveLengths", self.convert_compression_effective_lengths)
        writer.write_enum_value("lateralTorsionalBucklingMethod", self.lateral_torsional_buckling_method)
        writer.write_bool_value("modifyReductionFactorF", self.modify_reduction_factor_f)
        writer.write_bool_value("useTableB2", self.use_table_b2)
        writer.write_bool_value("useUkFactors", self.use_uk_factors)
    

