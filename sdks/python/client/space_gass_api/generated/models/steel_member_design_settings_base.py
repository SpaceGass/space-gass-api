from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989
    from .steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360
    from .steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993
    from .steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360
    from .steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250
    from .steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990
    from .steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100
    from .steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600
    from .steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly
    from .steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990
    from .steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000
    from .steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005
    from .steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011
    from .steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007
    from .steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

@dataclass
class SteelMemberDesignSettingsBase(AdditionalDataHolder, Parsable):
    """
    Steel member design settings specific to one design code.Read via GET and updated via PATCH at`/job/design/steel-member/{code}/settings`; the response is the designcode's own settings object, carrying only the settings that apply to that code.The code property names the design code and selects the settings object.
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
        if not mapping_value:
            return SteelMemberDesignSettingsBase()
        if mapping_value.casefold() == "AiscAsd1989".casefold():
            from .steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989

            return SteelMemberDesignSettingsAiscAsd1989()
        if mapping_value.casefold() == "AiscAsd360".casefold():
            from .steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360

            return SteelMemberDesignSettingsAiscAsd360()
        if mapping_value.casefold() == "AiscLrfd1993".casefold():
            from .steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993

            return SteelMemberDesignSettingsAiscLrfd1993()
        if mapping_value.casefold() == "AiscLrfd360".casefold():
            from .steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360

            return SteelMemberDesignSettingsAiscLrfd360()
        if mapping_value.casefold() == "As1250".casefold():
            from .steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250

            return SteelMemberDesignSettingsAs1250()
        if mapping_value.casefold() == "As3990".casefold():
            from .steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990

            return SteelMemberDesignSettingsAs3990()
        if mapping_value.casefold() == "As4100".casefold():
            from .steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100

            return SteelMemberDesignSettingsAs4100()
        if mapping_value.casefold() == "AsNzs4600".casefold():
            from .steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600

            return SteelMemberDesignSettingsAsNzs4600()
        if mapping_value.casefold() == "AsNzs4600DuragalOnly".casefold():
            from .steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly

            return SteelMemberDesignSettingsAsNzs4600DuragalOnly()
        if mapping_value.casefold() == "Bs5950_1990".casefold():
            from .steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990

            return SteelMemberDesignSettingsBs5950_1990()
        if mapping_value.casefold() == "Bs5950_2000".casefold():
            from .steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000

            return SteelMemberDesignSettingsBs5950_2000()
        if mapping_value.casefold() == "Eurocode3_2005".casefold():
            from .steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005

            return SteelMemberDesignSettingsEurocode3_2005()
        if mapping_value.casefold() == "HkCp2011".casefold():
            from .steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011

            return SteelMemberDesignSettingsHkCp2011()
        if mapping_value.casefold() == "Is800_2007".casefold():
            from .steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007

            return SteelMemberDesignSettingsIs800_2007()
        if mapping_value.casefold() == "Nzs3404".casefold():
            from .steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

            return SteelMemberDesignSettingsNzs3404()
        return SteelMemberDesignSettingsBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989
        from .steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360
        from .steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993
        from .steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360
        from .steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250
        from .steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990
        from .steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100
        from .steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600
        from .steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly
        from .steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990
        from .steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000
        from .steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005
        from .steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011
        from .steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007
        from .steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

        from .steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989
        from .steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360
        from .steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993
        from .steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360
        from .steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250
        from .steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990
        from .steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100
        from .steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600
        from .steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly
        from .steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990
        from .steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000
        from .steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005
        from .steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011
        from .steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007
        from .steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

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
    

