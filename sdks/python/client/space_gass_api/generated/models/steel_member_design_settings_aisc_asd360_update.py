from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aisc360_single_angle_method import Aisc360SingleAngleMethod
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsAiscAsd360Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the AISC ASD 360 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not a AISC ASD 360 setting is rejected.
    """
    # Selects this object type. Always "AiscAsd360".
    code: Optional[SteelMemberDesignSettingsAiscAsd360Update_code] = SteelMemberDesignSettingsAiscAsd360Update_code("AiscAsd360")
    # The addEccentricMoments property
    add_eccentric_moments: Optional[bool] = None
    # The calculateCb property
    calculate_cb: Optional[bool] = None
    # The calculateUFactor property
    calculate_u_factor: Optional[bool] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertCompressionEffectiveLengths property
    convert_compression_effective_lengths: Optional[bool] = None
    # Which AISC 360 clause E5 is used for single angles, where it applies.
    single_angle_method: Optional[Aisc360SingleAngleMethod] = None
    # The useAisc360_22 property
    use_aisc360_22: Optional[bool] = None
    # The useClauseH1_3 property
    use_clause_h1_3: Optional[bool] = None
    # The useClauseH2 property
    use_clause_h2: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAiscAsd360Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAiscAsd360Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAiscAsd360Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aisc360_single_angle_method import Aisc360SingleAngleMethod
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .aisc360_single_angle_method import Aisc360SingleAngleMethod
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "calculateCb": lambda n : setattr(self, 'calculate_cb', n.get_bool_value()),
            "calculateUFactor": lambda n : setattr(self, 'calculate_u_factor', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertCompressionEffectiveLengths": lambda n : setattr(self, 'convert_compression_effective_lengths', n.get_bool_value()),
            "singleAngleMethod": lambda n : setattr(self, 'single_angle_method', n.get_enum_value(Aisc360SingleAngleMethod)),
            "useAisc360_22": lambda n : setattr(self, 'use_aisc360_22', n.get_bool_value()),
            "useClauseH1_3": lambda n : setattr(self, 'use_clause_h1_3', n.get_bool_value()),
            "useClauseH2": lambda n : setattr(self, 'use_clause_h2', n.get_bool_value()),
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
        writer.write_bool_value("calculateCb", self.calculate_cb)
        writer.write_bool_value("calculateUFactor", self.calculate_u_factor)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertCompressionEffectiveLengths", self.convert_compression_effective_lengths)
        writer.write_enum_value("singleAngleMethod", self.single_angle_method)
        writer.write_bool_value("useAisc360_22", self.use_aisc360_22)
        writer.write_bool_value("useClauseH1_3", self.use_clause_h1_3)
        writer.write_bool_value("useClauseH2", self.use_clause_h2)
    

