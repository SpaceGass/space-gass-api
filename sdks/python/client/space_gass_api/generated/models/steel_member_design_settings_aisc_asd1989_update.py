from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsAiscAsd1989Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the AISC ASD 1989 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not an AISC ASD 1989 setting is rejected.
    """
    # Selects this object type. Always "AiscAsd1989".
    code: Optional[SteelMemberDesignSettingsAiscAsd1989Update_code] = SteelMemberDesignSettingsAiscAsd1989Update_code("AiscAsd1989")
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsAiscAsd1989Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsAiscAsd1989Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsAiscAsd1989Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "calculateCb": lambda n : setattr(self, 'calculate_cb', n.get_bool_value()),
            "calculateUFactor": lambda n : setattr(self, 'calculate_u_factor', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "convertCompressionEffectiveLengths": lambda n : setattr(self, 'convert_compression_effective_lengths', n.get_bool_value()),
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
    

