from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsNZS3404Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the NZS3404 1997 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not an NZS3404 setting is rejected.
    """
    # Selects this object type. Always "Nzs3404".
    code: Optional[SteelMemberDesignSettingsNZS3404Update_code] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The convertCompressionEffectiveLengths property
    convert_compression_effective_lengths: Optional[bool] = None
    # The performSeismicChecks property
    perform_seismic_checks: Optional[bool] = None
    # The useKtFactorForTension property
    use_kt_factor_for_tension: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsNZS3404Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsNZS3404Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsNZS3404Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

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
    

