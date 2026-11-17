from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
    from .steel_member_design_iteration_settings_update import SteelMemberDesignIterationSettingsUpdate
    from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

@dataclass
class SteelMemberDesignRunDesignRequest(Parsable):
    """
    Request body for POST /job/design/steel-member/{code}/run-design.The body is optional. Supplied settings are written to the job's storedsettings before the run starts, and remain stored after it.
    """
    # Update request for the settings specific to one design code.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-member/{code}/settings and the codeSettingsblock on the run endpoints. The code property selects the design code's ownupdate object, and a field that object does not have is rejected. code may beomitted: it defaults to the route's design code. When given, it must be theroute's design code.
    code_settings: Optional[SteelMemberDesignSettingsBaseUpdate] = None
    # Update request for the steel member design iteration settings.Only fields included in the request are updated; omit a field to keep its current value.
    design_iteration_settings: Optional[SteelMemberDesignIterationSettingsUpdate] = None
    # Update request for the general steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-member/settings and the settings overrides on the run endpoints.
    settings: Optional[SteelMemberDesignGeneralSettingsUpdate] = None
    # Whether to update the analysis sections to the designed sizes after the design.
    update_sections: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignRunDesignRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignRunDesignRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignRunDesignRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
        from .steel_member_design_iteration_settings_update import SteelMemberDesignIterationSettingsUpdate
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        from .steel_member_design_general_settings_update import SteelMemberDesignGeneralSettingsUpdate
        from .steel_member_design_iteration_settings_update import SteelMemberDesignIterationSettingsUpdate
        from .steel_member_design_settings_base_update import SteelMemberDesignSettingsBaseUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "codeSettings": lambda n : setattr(self, 'code_settings', n.get_object_value(SteelMemberDesignSettingsBaseUpdate)),
            "designIterationSettings": lambda n : setattr(self, 'design_iteration_settings', n.get_object_value(SteelMemberDesignIterationSettingsUpdate)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(SteelMemberDesignGeneralSettingsUpdate)),
            "updateSections": lambda n : setattr(self, 'update_sections', n.get_bool_value()),
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
        writer.write_object_value("designIterationSettings", self.design_iteration_settings)
        writer.write_object_value("settings", self.settings)
        writer.write_bool_value("updateSections", self.update_sections)
    

