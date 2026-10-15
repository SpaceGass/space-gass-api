from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update
    from .steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

@dataclass
class SteelMemberDesignSettingsBaseUpdate(AdditionalDataHolder, Parsable):
    """
    Update request for the settings specific to one design code.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-design/{code}/settings and the codeSettingsblock on the run endpoints. The code property is required and must be theroute's design code; it selects the design code's own update object, and afield that object does not have is rejected.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The code property
    code: Optional[str] = None
    # The slendernessRatioCheck property
    slenderness_ratio_check: Optional[bool] = None
    # The slendernessRatioLimit property
    slenderness_ratio_limit: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignSettingsBaseUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignSettingsBaseUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "As4100".casefold():
            from .steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update

            return SteelMemberDesignSettingsAS4100Update()
        if mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from .steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

            return SteelMemberDesignSettingsNZS3404Update()
        return SteelMemberDesignSettingsBaseUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update
        from .steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

        from .steel_member_design_settings_a_s4100_update import SteelMemberDesignSettingsAS4100Update
        from .steel_member_design_settings_n_z_s3404_update import SteelMemberDesignSettingsNZS3404Update

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
    

