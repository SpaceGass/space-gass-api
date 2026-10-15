from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
    from ......models.steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

@dataclass
class SettingsPatchResponse(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes SteelMemberDesignSettingsAS4100, SteelMemberDesignSettingsNZS3404
    """
    # Composed type representation for type SteelMemberDesignSettingsAS4100
    steel_member_design_settings_a_s4100: Optional[SteelMemberDesignSettingsAS4100] = None
    # Composed type representation for type SteelMemberDesignSettingsNZS3404
    steel_member_design_settings_n_z_s3404: Optional[SteelMemberDesignSettingsNZS3404] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SettingsPatchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingsPatchResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SettingsPatchResponse()
        if mapping_value and mapping_value.casefold() == "As4100".casefold():
            from ......models.steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100

            result.steel_member_design_settings_a_s4100 = SteelMemberDesignSettingsAS4100()
        elif mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from ......models.steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

            result.steel_member_design_settings_n_z_s3404 = SteelMemberDesignSettingsNZS3404()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
        from ......models.steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

        if self.steel_member_design_settings_a_s4100:
            return self.steel_member_design_settings_a_s4100.get_field_deserializers()
        if self.steel_member_design_settings_n_z_s3404:
            return self.steel_member_design_settings_n_z_s3404.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.steel_member_design_settings_a_s4100 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_a_s4100)
        elif self.steel_member_design_settings_n_z_s3404 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_n_z_s3404)
    

