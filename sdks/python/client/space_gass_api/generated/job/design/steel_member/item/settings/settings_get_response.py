from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989
    from ......models.steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360
    from ......models.steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993
    from ......models.steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360
    from ......models.steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250
    from ......models.steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990
    from ......models.steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100
    from ......models.steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600
    from ......models.steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly
    from ......models.steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990
    from ......models.steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000
    from ......models.steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005
    from ......models.steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011
    from ......models.steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007
    from ......models.steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

@dataclass
class SettingsGetResponse(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes SteelMemberDesignSettingsAiscAsd1989, SteelMemberDesignSettingsAiscAsd360, SteelMemberDesignSettingsAiscLrfd1993, SteelMemberDesignSettingsAiscLrfd360, SteelMemberDesignSettingsAs1250, SteelMemberDesignSettingsAs3990, SteelMemberDesignSettingsAs4100, SteelMemberDesignSettingsAsNzs4600, SteelMemberDesignSettingsAsNzs4600DuragalOnly, SteelMemberDesignSettingsBs5950_1990, SteelMemberDesignSettingsBs5950_2000, SteelMemberDesignSettingsEurocode3_2005, SteelMemberDesignSettingsHkCp2011, SteelMemberDesignSettingsIs800_2007, SteelMemberDesignSettingsNzs3404
    """
    # Composed type representation for type SteelMemberDesignSettingsAiscAsd1989
    steel_member_design_settings_aisc_asd1989: Optional[SteelMemberDesignSettingsAiscAsd1989] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscAsd360
    steel_member_design_settings_aisc_asd360: Optional[SteelMemberDesignSettingsAiscAsd360] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscLrfd1993
    steel_member_design_settings_aisc_lrfd1993: Optional[SteelMemberDesignSettingsAiscLrfd1993] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscLrfd360
    steel_member_design_settings_aisc_lrfd360: Optional[SteelMemberDesignSettingsAiscLrfd360] = None
    # Composed type representation for type SteelMemberDesignSettingsAsNzs4600
    steel_member_design_settings_as_nzs4600: Optional[SteelMemberDesignSettingsAsNzs4600] = None
    # Composed type representation for type SteelMemberDesignSettingsAsNzs4600DuragalOnly
    steel_member_design_settings_as_nzs4600_duragal_only: Optional[SteelMemberDesignSettingsAsNzs4600DuragalOnly] = None
    # Composed type representation for type SteelMemberDesignSettingsAs1250
    steel_member_design_settings_as1250: Optional[SteelMemberDesignSettingsAs1250] = None
    # Composed type representation for type SteelMemberDesignSettingsAs3990
    steel_member_design_settings_as3990: Optional[SteelMemberDesignSettingsAs3990] = None
    # Composed type representation for type SteelMemberDesignSettingsAs4100
    steel_member_design_settings_as4100: Optional[SteelMemberDesignSettingsAs4100] = None
    # Composed type representation for type SteelMemberDesignSettingsBs5950_1990
    steel_member_design_settings_bs5950_1990: Optional[SteelMemberDesignSettingsBs5950_1990] = None
    # Composed type representation for type SteelMemberDesignSettingsBs5950_2000
    steel_member_design_settings_bs5950_2000: Optional[SteelMemberDesignSettingsBs5950_2000] = None
    # Composed type representation for type SteelMemberDesignSettingsEurocode3_2005
    steel_member_design_settings_eurocode3_2005: Optional[SteelMemberDesignSettingsEurocode3_2005] = None
    # Composed type representation for type SteelMemberDesignSettingsHkCp2011
    steel_member_design_settings_hk_cp2011: Optional[SteelMemberDesignSettingsHkCp2011] = None
    # Composed type representation for type SteelMemberDesignSettingsIs800_2007
    steel_member_design_settings_is800_2007: Optional[SteelMemberDesignSettingsIs800_2007] = None
    # Composed type representation for type SteelMemberDesignSettingsNzs3404
    steel_member_design_settings_nzs3404: Optional[SteelMemberDesignSettingsNzs3404] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SettingsGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingsGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SettingsGetResponse()
        if mapping_value and mapping_value.casefold() == "AiscAsd1989".casefold():
            from ......models.steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989

            result.steel_member_design_settings_aisc_asd1989 = SteelMemberDesignSettingsAiscAsd1989()
        elif mapping_value and mapping_value.casefold() == "AiscAsd360".casefold():
            from ......models.steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360

            result.steel_member_design_settings_aisc_asd360 = SteelMemberDesignSettingsAiscAsd360()
        elif mapping_value and mapping_value.casefold() == "AiscLrfd1993".casefold():
            from ......models.steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993

            result.steel_member_design_settings_aisc_lrfd1993 = SteelMemberDesignSettingsAiscLrfd1993()
        elif mapping_value and mapping_value.casefold() == "AiscLrfd360".casefold():
            from ......models.steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360

            result.steel_member_design_settings_aisc_lrfd360 = SteelMemberDesignSettingsAiscLrfd360()
        elif mapping_value and mapping_value.casefold() == "AsNzs4600".casefold():
            from ......models.steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600

            result.steel_member_design_settings_as_nzs4600 = SteelMemberDesignSettingsAsNzs4600()
        elif mapping_value and mapping_value.casefold() == "AsNzs4600DuragalOnly".casefold():
            from ......models.steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly

            result.steel_member_design_settings_as_nzs4600_duragal_only = SteelMemberDesignSettingsAsNzs4600DuragalOnly()
        elif mapping_value and mapping_value.casefold() == "As1250".casefold():
            from ......models.steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250

            result.steel_member_design_settings_as1250 = SteelMemberDesignSettingsAs1250()
        elif mapping_value and mapping_value.casefold() == "As3990".casefold():
            from ......models.steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990

            result.steel_member_design_settings_as3990 = SteelMemberDesignSettingsAs3990()
        elif mapping_value and mapping_value.casefold() == "As4100".casefold():
            from ......models.steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100

            result.steel_member_design_settings_as4100 = SteelMemberDesignSettingsAs4100()
        elif mapping_value and mapping_value.casefold() == "Bs5950_1990".casefold():
            from ......models.steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990

            result.steel_member_design_settings_bs5950_1990 = SteelMemberDesignSettingsBs5950_1990()
        elif mapping_value and mapping_value.casefold() == "Bs5950_2000".casefold():
            from ......models.steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000

            result.steel_member_design_settings_bs5950_2000 = SteelMemberDesignSettingsBs5950_2000()
        elif mapping_value and mapping_value.casefold() == "Eurocode3_2005".casefold():
            from ......models.steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005

            result.steel_member_design_settings_eurocode3_2005 = SteelMemberDesignSettingsEurocode3_2005()
        elif mapping_value and mapping_value.casefold() == "HkCp2011".casefold():
            from ......models.steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011

            result.steel_member_design_settings_hk_cp2011 = SteelMemberDesignSettingsHkCp2011()
        elif mapping_value and mapping_value.casefold() == "Is800_2007".casefold():
            from ......models.steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007

            result.steel_member_design_settings_is800_2007 = SteelMemberDesignSettingsIs800_2007()
        elif mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from ......models.steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

            result.steel_member_design_settings_nzs3404 = SteelMemberDesignSettingsNzs3404()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.steel_member_design_settings_aisc_asd1989 import SteelMemberDesignSettingsAiscAsd1989
        from ......models.steel_member_design_settings_aisc_asd360 import SteelMemberDesignSettingsAiscAsd360
        from ......models.steel_member_design_settings_aisc_lrfd1993 import SteelMemberDesignSettingsAiscLrfd1993
        from ......models.steel_member_design_settings_aisc_lrfd360 import SteelMemberDesignSettingsAiscLrfd360
        from ......models.steel_member_design_settings_as1250 import SteelMemberDesignSettingsAs1250
        from ......models.steel_member_design_settings_as3990 import SteelMemberDesignSettingsAs3990
        from ......models.steel_member_design_settings_as4100 import SteelMemberDesignSettingsAs4100
        from ......models.steel_member_design_settings_as_nzs4600 import SteelMemberDesignSettingsAsNzs4600
        from ......models.steel_member_design_settings_as_nzs4600_duragal_only import SteelMemberDesignSettingsAsNzs4600DuragalOnly
        from ......models.steel_member_design_settings_bs5950_1990 import SteelMemberDesignSettingsBs5950_1990
        from ......models.steel_member_design_settings_bs5950_2000 import SteelMemberDesignSettingsBs5950_2000
        from ......models.steel_member_design_settings_eurocode3_2005 import SteelMemberDesignSettingsEurocode3_2005
        from ......models.steel_member_design_settings_hk_cp2011 import SteelMemberDesignSettingsHkCp2011
        from ......models.steel_member_design_settings_is800_2007 import SteelMemberDesignSettingsIs800_2007
        from ......models.steel_member_design_settings_nzs3404 import SteelMemberDesignSettingsNzs3404

        if self.steel_member_design_settings_aisc_asd1989:
            return self.steel_member_design_settings_aisc_asd1989.get_field_deserializers()
        if self.steel_member_design_settings_aisc_asd360:
            return self.steel_member_design_settings_aisc_asd360.get_field_deserializers()
        if self.steel_member_design_settings_aisc_lrfd1993:
            return self.steel_member_design_settings_aisc_lrfd1993.get_field_deserializers()
        if self.steel_member_design_settings_aisc_lrfd360:
            return self.steel_member_design_settings_aisc_lrfd360.get_field_deserializers()
        if self.steel_member_design_settings_as_nzs4600:
            return self.steel_member_design_settings_as_nzs4600.get_field_deserializers()
        if self.steel_member_design_settings_as_nzs4600_duragal_only:
            return self.steel_member_design_settings_as_nzs4600_duragal_only.get_field_deserializers()
        if self.steel_member_design_settings_as1250:
            return self.steel_member_design_settings_as1250.get_field_deserializers()
        if self.steel_member_design_settings_as3990:
            return self.steel_member_design_settings_as3990.get_field_deserializers()
        if self.steel_member_design_settings_as4100:
            return self.steel_member_design_settings_as4100.get_field_deserializers()
        if self.steel_member_design_settings_bs5950_1990:
            return self.steel_member_design_settings_bs5950_1990.get_field_deserializers()
        if self.steel_member_design_settings_bs5950_2000:
            return self.steel_member_design_settings_bs5950_2000.get_field_deserializers()
        if self.steel_member_design_settings_eurocode3_2005:
            return self.steel_member_design_settings_eurocode3_2005.get_field_deserializers()
        if self.steel_member_design_settings_hk_cp2011:
            return self.steel_member_design_settings_hk_cp2011.get_field_deserializers()
        if self.steel_member_design_settings_is800_2007:
            return self.steel_member_design_settings_is800_2007.get_field_deserializers()
        if self.steel_member_design_settings_nzs3404:
            return self.steel_member_design_settings_nzs3404.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.steel_member_design_settings_aisc_asd1989 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_asd1989)
        elif self.steel_member_design_settings_aisc_asd360 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_asd360)
        elif self.steel_member_design_settings_aisc_lrfd1993 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_lrfd1993)
        elif self.steel_member_design_settings_aisc_lrfd360 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_lrfd360)
        elif self.steel_member_design_settings_as_nzs4600 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as_nzs4600)
        elif self.steel_member_design_settings_as_nzs4600_duragal_only is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as_nzs4600_duragal_only)
        elif self.steel_member_design_settings_as1250 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as1250)
        elif self.steel_member_design_settings_as3990 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as3990)
        elif self.steel_member_design_settings_as4100 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as4100)
        elif self.steel_member_design_settings_bs5950_1990 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_bs5950_1990)
        elif self.steel_member_design_settings_bs5950_2000 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_bs5950_2000)
        elif self.steel_member_design_settings_eurocode3_2005 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_eurocode3_2005)
        elif self.steel_member_design_settings_hk_cp2011 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_hk_cp2011)
        elif self.steel_member_design_settings_is800_2007 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_is800_2007)
        elif self.steel_member_design_settings_nzs3404 is not None:
            writer.write_object_value(None, self.steel_member_design_settings_nzs3404)
    

