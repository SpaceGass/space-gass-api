from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_aisc_asd1989_update import SteelMemberDesignSettingsAiscAsd1989Update
    from .steel_member_design_settings_aisc_asd360_update import SteelMemberDesignSettingsAiscAsd360Update
    from .steel_member_design_settings_aisc_lrfd1993_update import SteelMemberDesignSettingsAiscLrfd1993Update
    from .steel_member_design_settings_aisc_lrfd360_update import SteelMemberDesignSettingsAiscLrfd360Update
    from .steel_member_design_settings_as1250_update import SteelMemberDesignSettingsAs1250Update
    from .steel_member_design_settings_as3990_update import SteelMemberDesignSettingsAs3990Update
    from .steel_member_design_settings_as4100_update import SteelMemberDesignSettingsAs4100Update
    from .steel_member_design_settings_as_nzs4600_duragal_only_update import SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate
    from .steel_member_design_settings_as_nzs4600_update import SteelMemberDesignSettingsAsNzs4600Update
    from .steel_member_design_settings_bs5950_1990_update import SteelMemberDesignSettingsBs5950_1990Update
    from .steel_member_design_settings_bs5950_2000_update import SteelMemberDesignSettingsBs5950_2000Update
    from .steel_member_design_settings_eurocode3_2005_update import SteelMemberDesignSettingsEurocode3_2005Update
    from .steel_member_design_settings_hk_cp2011_update import SteelMemberDesignSettingsHkCp2011Update
    from .steel_member_design_settings_is800_2007_update import SteelMemberDesignSettingsIs800_2007Update
    from .steel_member_design_settings_nzs3404_update import SteelMemberDesignSettingsNzs3404Update

@dataclass
class SteelMemberDesignSettingsBaseUpdate(AdditionalDataHolder, Parsable):
    """
    Update request for the settings specific to one design code.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-member/{code}/settings and the codeSettingsblock on the run endpoints. The code property selects the design code's ownupdate object, and a field that object does not have is rejected. code may beomitted: it defaults to the route's design code. When given, it must be theroute's design code.
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
        if not mapping_value:
            return SteelMemberDesignSettingsBaseUpdate()
        if mapping_value.casefold() == "AiscAsd1989".casefold():
            from .steel_member_design_settings_aisc_asd1989_update import SteelMemberDesignSettingsAiscAsd1989Update

            return SteelMemberDesignSettingsAiscAsd1989Update()
        if mapping_value.casefold() == "AiscAsd360".casefold():
            from .steel_member_design_settings_aisc_asd360_update import SteelMemberDesignSettingsAiscAsd360Update

            return SteelMemberDesignSettingsAiscAsd360Update()
        if mapping_value.casefold() == "AiscLrfd1993".casefold():
            from .steel_member_design_settings_aisc_lrfd1993_update import SteelMemberDesignSettingsAiscLrfd1993Update

            return SteelMemberDesignSettingsAiscLrfd1993Update()
        if mapping_value.casefold() == "AiscLrfd360".casefold():
            from .steel_member_design_settings_aisc_lrfd360_update import SteelMemberDesignSettingsAiscLrfd360Update

            return SteelMemberDesignSettingsAiscLrfd360Update()
        if mapping_value.casefold() == "As1250".casefold():
            from .steel_member_design_settings_as1250_update import SteelMemberDesignSettingsAs1250Update

            return SteelMemberDesignSettingsAs1250Update()
        if mapping_value.casefold() == "As3990".casefold():
            from .steel_member_design_settings_as3990_update import SteelMemberDesignSettingsAs3990Update

            return SteelMemberDesignSettingsAs3990Update()
        if mapping_value.casefold() == "As4100".casefold():
            from .steel_member_design_settings_as4100_update import SteelMemberDesignSettingsAs4100Update

            return SteelMemberDesignSettingsAs4100Update()
        if mapping_value.casefold() == "AsNzs4600".casefold():
            from .steel_member_design_settings_as_nzs4600_update import SteelMemberDesignSettingsAsNzs4600Update

            return SteelMemberDesignSettingsAsNzs4600Update()
        if mapping_value.casefold() == "AsNzs4600DuragalOnly".casefold():
            from .steel_member_design_settings_as_nzs4600_duragal_only_update import SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate

            return SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate()
        if mapping_value.casefold() == "Bs5950_1990".casefold():
            from .steel_member_design_settings_bs5950_1990_update import SteelMemberDesignSettingsBs5950_1990Update

            return SteelMemberDesignSettingsBs5950_1990Update()
        if mapping_value.casefold() == "Bs5950_2000".casefold():
            from .steel_member_design_settings_bs5950_2000_update import SteelMemberDesignSettingsBs5950_2000Update

            return SteelMemberDesignSettingsBs5950_2000Update()
        if mapping_value.casefold() == "Eurocode3_2005".casefold():
            from .steel_member_design_settings_eurocode3_2005_update import SteelMemberDesignSettingsEurocode3_2005Update

            return SteelMemberDesignSettingsEurocode3_2005Update()
        if mapping_value.casefold() == "HkCp2011".casefold():
            from .steel_member_design_settings_hk_cp2011_update import SteelMemberDesignSettingsHkCp2011Update

            return SteelMemberDesignSettingsHkCp2011Update()
        if mapping_value.casefold() == "Is800_2007".casefold():
            from .steel_member_design_settings_is800_2007_update import SteelMemberDesignSettingsIs800_2007Update

            return SteelMemberDesignSettingsIs800_2007Update()
        if mapping_value.casefold() == "Nzs3404".casefold():
            from .steel_member_design_settings_nzs3404_update import SteelMemberDesignSettingsNzs3404Update

            return SteelMemberDesignSettingsNzs3404Update()
        return SteelMemberDesignSettingsBaseUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_aisc_asd1989_update import SteelMemberDesignSettingsAiscAsd1989Update
        from .steel_member_design_settings_aisc_asd360_update import SteelMemberDesignSettingsAiscAsd360Update
        from .steel_member_design_settings_aisc_lrfd1993_update import SteelMemberDesignSettingsAiscLrfd1993Update
        from .steel_member_design_settings_aisc_lrfd360_update import SteelMemberDesignSettingsAiscLrfd360Update
        from .steel_member_design_settings_as1250_update import SteelMemberDesignSettingsAs1250Update
        from .steel_member_design_settings_as3990_update import SteelMemberDesignSettingsAs3990Update
        from .steel_member_design_settings_as4100_update import SteelMemberDesignSettingsAs4100Update
        from .steel_member_design_settings_as_nzs4600_duragal_only_update import SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate
        from .steel_member_design_settings_as_nzs4600_update import SteelMemberDesignSettingsAsNzs4600Update
        from .steel_member_design_settings_bs5950_1990_update import SteelMemberDesignSettingsBs5950_1990Update
        from .steel_member_design_settings_bs5950_2000_update import SteelMemberDesignSettingsBs5950_2000Update
        from .steel_member_design_settings_eurocode3_2005_update import SteelMemberDesignSettingsEurocode3_2005Update
        from .steel_member_design_settings_hk_cp2011_update import SteelMemberDesignSettingsHkCp2011Update
        from .steel_member_design_settings_is800_2007_update import SteelMemberDesignSettingsIs800_2007Update
        from .steel_member_design_settings_nzs3404_update import SteelMemberDesignSettingsNzs3404Update

        from .steel_member_design_settings_aisc_asd1989_update import SteelMemberDesignSettingsAiscAsd1989Update
        from .steel_member_design_settings_aisc_asd360_update import SteelMemberDesignSettingsAiscAsd360Update
        from .steel_member_design_settings_aisc_lrfd1993_update import SteelMemberDesignSettingsAiscLrfd1993Update
        from .steel_member_design_settings_aisc_lrfd360_update import SteelMemberDesignSettingsAiscLrfd360Update
        from .steel_member_design_settings_as1250_update import SteelMemberDesignSettingsAs1250Update
        from .steel_member_design_settings_as3990_update import SteelMemberDesignSettingsAs3990Update
        from .steel_member_design_settings_as4100_update import SteelMemberDesignSettingsAs4100Update
        from .steel_member_design_settings_as_nzs4600_duragal_only_update import SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate
        from .steel_member_design_settings_as_nzs4600_update import SteelMemberDesignSettingsAsNzs4600Update
        from .steel_member_design_settings_bs5950_1990_update import SteelMemberDesignSettingsBs5950_1990Update
        from .steel_member_design_settings_bs5950_2000_update import SteelMemberDesignSettingsBs5950_2000Update
        from .steel_member_design_settings_eurocode3_2005_update import SteelMemberDesignSettingsEurocode3_2005Update
        from .steel_member_design_settings_hk_cp2011_update import SteelMemberDesignSettingsHkCp2011Update
        from .steel_member_design_settings_is800_2007_update import SteelMemberDesignSettingsIs800_2007Update
        from .steel_member_design_settings_nzs3404_update import SteelMemberDesignSettingsNzs3404Update

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
    

