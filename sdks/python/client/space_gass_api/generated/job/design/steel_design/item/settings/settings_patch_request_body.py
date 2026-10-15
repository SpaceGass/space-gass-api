from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update
    from ......models.steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

@dataclass
class SettingsPatchRequestBody(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes SteelMemberDesignSettingsAS4100Update, SteelMemberDesignSettingsNZS3404Update
    """
    # Composed type representation for type SteelMemberDesignSettingsAS4100Update
    steel_member_design_settings_a_s4100_update: Optional[SteelMemberDesignSettingsAS4100Update] = None
    # Composed type representation for type SteelMemberDesignSettingsNZS3404Update
    steel_member_design_settings_n_z_s3404_update: Optional[SteelMemberDesignSettingsNZS3404Update] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SettingsPatchRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingsPatchRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SettingsPatchRequestBody()
        if mapping_value and mapping_value.casefold() == "As4100".casefold():
            from ......models.steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update

            result.steel_member_design_settings_a_s4100_update = SteelMemberDesignSettingsAS4100Update()
        elif mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from ......models.steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

            result.steel_member_design_settings_n_z_s3404_update = SteelMemberDesignSettingsNZS3404Update()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update
        from ......models.steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

        if self.steel_member_design_settings_a_s4100_update:
            return self.steel_member_design_settings_a_s4100_update.get_field_deserializers()
        if self.steel_member_design_settings_n_z_s3404_update:
            return self.steel_member_design_settings_n_z_s3404_update.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.steel_member_design_settings_a_s4100_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_a_s4100_update)
        elif self.steel_member_design_settings_n_z_s3404_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_n_z_s3404_update)
    

