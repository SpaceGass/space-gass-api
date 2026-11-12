from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignSettingsHkCp2011Update(SteelMemberDesignSettingsBaseUpdate, Parsable):
    """
    Update request for the HK CP2011 steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.A field that is not a HK CP2011 setting is rejected.
    """
    # Selects this object type. Always "HkCp2011".
    code: Optional[SteelMemberDesignSettingsHkCp2011Update_code] = SteelMemberDesignSettingsHkCp2011Update_code("HkCp2011")
    # The addEccentricMoments property
    add_eccentric_moments: Optional[bool] = None
    # The calculateMltFactor property
    calculate_mlt_factor: Optional[bool] = None
    # The calculatePcbarFromGroupLength property
    calculate_pcbar_from_group_length: Optional[bool] = None
    # The considerEccentricEffects property
    consider_eccentric_effects: Optional[bool] = None
    # The useClause6_8_3 property
    use_clause6_8_3: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsHkCp2011Update:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsHkCp2011Update
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignSettingsHkCp2011Update()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "addEccentricMoments": lambda n : setattr(self, 'add_eccentric_moments', n.get_bool_value()),
            "calculateMltFactor": lambda n : setattr(self, 'calculate_mlt_factor', n.get_bool_value()),
            "calculatePcbarFromGroupLength": lambda n : setattr(self, 'calculate_pcbar_from_group_length', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "useClause6_8_3": lambda n : setattr(self, 'use_clause6_8_3', n.get_bool_value()),
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
        writer.write_bool_value("calculateMltFactor", self.calculate_mlt_factor)
        writer.write_bool_value("calculatePcbarFromGroupLength", self.calculate_pcbar_from_group_length)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_bool_value("useClause6_8_3", self.use_clause6_8_3)
    

