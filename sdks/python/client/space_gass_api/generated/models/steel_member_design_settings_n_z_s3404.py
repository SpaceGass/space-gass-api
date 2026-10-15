from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

from .steel_member_design_settings_base import SteelMemberDesignSettingsBase

@dataclass
class SteelMemberDesignSettingsNZS3404(SteelMemberDesignSettingsBase, Parsable):
    """
    Steel member design settings for NZS3404 1997.
    """
    # Selects this object type. Always "Nzs3404".
    code: Optional[SteelMemberDesignSettingsNZS3404_code] = None
    # Consider eccentric effects.
    consider_eccentric_effects: Optional[bool] = None
    # Convert compression effective lengths to principal axes.
    convert_compression_effective_lengths: Optional[bool] = None
    # Perform seismic checks for category 1-4 members.
    perform_seismic_checks: Optional[bool] = None
    # Use Kt factor for tension members.
    use_kt_factor_for_tension: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsNZS3404:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsNZS3404
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsNZS3404()
    
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
            "performSeismicChecks": lambda n : setattr(self, 'perform_seismic_checks', n.get_bool_value()),
            "useKtFactorForTension": lambda n : setattr(self, 'use_kt_factor_for_tension', n.get_bool_value()),
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
        writer.write_bool_value("performSeismicChecks", self.perform_seismic_checks)
        writer.write_bool_value("useKtFactorForTension", self.use_kt_factor_for_tension)
    

