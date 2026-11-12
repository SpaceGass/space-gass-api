from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

@dataclass
class SteelMemberDesignSettingsBs5950_1990(SteelMemberDesignSettingsBase, Parsable):
    """
    Steel member design settings for BS5950:1990.
    """
    # Selects this object type. Always "Bs5950_1990".
    code: Optional[SteelMemberDesignSettingsBs5950_1990_code] = SteelMemberDesignSettingsBs5950_1990_code("Bs5950_1990")
    # Consider eccentric effects.
    consider_eccentric_effects: Optional[bool] = None
    # Convert compression effective lengths to principal axes.
    convert_compression_effective_lengths: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsBs5950_1990:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsBs5950_1990
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsBs5950_1990()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("convertCompressionEffectiveLengths", self.convert_compression_effective_lengths)
    

