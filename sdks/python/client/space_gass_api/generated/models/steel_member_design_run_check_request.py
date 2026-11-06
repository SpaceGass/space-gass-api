from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
    from .steel_member_design_run_check_request_code_settings import SteelMemberDesignRunCheckRequest_codeSettings

@dataclass
class SteelMemberDesignRunCheckRequest(Parsable):
    """
    Request body for POST /job/design/steel-member/{code}/run-check.The body is optional. Supplied settings are written to the job's storedsettings before the run starts, and remain stored after it.
    """
    # Optional partial code settings, written to the stored settings before the run.
    code_settings: Optional[SteelMemberDesignRunCheckRequest_codeSettings] = None
    # Update request for the general steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-member/settings and the settings overrides on the run endpoints.
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignRunCheckRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignRunCheckRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignRunCheckRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
        from .steel_member_design_run_check_request_code_settings import SteelMemberDesignRunCheckRequest_codeSettings

        from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
        from .steel_member_design_run_check_request_code_settings import SteelMemberDesignRunCheckRequest_codeSettings

        fields: dict[str, Callable[[Any], None]] = {
            "codeSettings": lambda n : setattr(self, 'code_settings', n.get_object_value(SteelMemberDesignRunCheckRequest_codeSettings)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(SteelMemberDesignGeneralSettingsUpdate)),
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
        writer.write_object_value("codeSettings", self.code_settings)
        writer.write_object_value("settings", self.settings)
    

