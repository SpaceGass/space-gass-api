from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
    from .steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

@dataclass
class SteelMemberDesignSettingsBase(AdditionalDataHolder, Parsable):
    """
    Steel member design settings specific to one design code.Read via GET and updated via PATCH at`/job/design/steel-design/{code}/settings`; the response is the designcode's own settings object, carrying only the settings that apply to that code.The code property names the design code and selects the settings object.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The code property
    code: Optional[str] = None
    # Whether to perform the slenderness ratio check.
    slenderness_ratio_check: Optional[bool] = None
    # Slenderness ratio limit.
    slenderness_ratio_limit: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "As4100".casefold():
            from .steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100

            return SteelMemberDesignSettingsAS4100()
        if mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from .steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

            return SteelMemberDesignSettingsNZS3404()
        return SteelMemberDesignSettingsBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
        from .steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

        from .steel_member_design_settings_a_s4100 import SteelMemberDesignSettingsAS4100
        from .steel_member_design_settings_n_z_s3404 import SteelMemberDesignSettingsNZS3404

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "slendernessRatioCheck": lambda n : setattr(self, 'slenderness_ratio_check', n.get_bool_value()),
            "slendernessRatioLimit": lambda n : setattr(self, 'slenderness_ratio_limit', n.get_float_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("code", self.code)
        writer.write_bool_value("slendernessRatioCheck", self.slenderness_ratio_check)
        writer.write_float_value("slendernessRatioLimit", self.slenderness_ratio_limit)
        writer.write_additional_data_value(self.additional_data)
    

