from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
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
class SteelMemberDesignRunDesignRequest_codeSettings(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes SteelMemberDesignSettingsAiscAsd1989Update, SteelMemberDesignSettingsAiscAsd360Update, SteelMemberDesignSettingsAiscLrfd1993Update, SteelMemberDesignSettingsAiscLrfd360Update, SteelMemberDesignSettingsAs1250Update, SteelMemberDesignSettingsAs3990Update, SteelMemberDesignSettingsAs4100Update, SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate, SteelMemberDesignSettingsAsNzs4600Update, SteelMemberDesignSettingsBs5950_1990Update, SteelMemberDesignSettingsBs5950_2000Update, SteelMemberDesignSettingsEurocode3_2005Update, SteelMemberDesignSettingsHkCp2011Update, SteelMemberDesignSettingsIs800_2007Update, SteelMemberDesignSettingsNzs3404Update
    """
    # Composed type representation for type SteelMemberDesignSettingsAiscAsd1989Update
    steel_member_design_settings_aisc_asd1989_update: Optional[SteelMemberDesignSettingsAiscAsd1989Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscAsd360Update
    steel_member_design_settings_aisc_asd360_update: Optional[SteelMemberDesignSettingsAiscAsd360Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscLrfd1993Update
    steel_member_design_settings_aisc_lrfd1993_update: Optional[SteelMemberDesignSettingsAiscLrfd1993Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAiscLrfd360Update
    steel_member_design_settings_aisc_lrfd360_update: Optional[SteelMemberDesignSettingsAiscLrfd360Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate
    steel_member_design_settings_as_nzs4600_duragal_only_update: Optional[SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate] = None
    # Composed type representation for type SteelMemberDesignSettingsAsNzs4600Update
    steel_member_design_settings_as_nzs4600_update: Optional[SteelMemberDesignSettingsAsNzs4600Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAs1250Update
    steel_member_design_settings_as1250_update: Optional[SteelMemberDesignSettingsAs1250Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAs3990Update
    steel_member_design_settings_as3990_update: Optional[SteelMemberDesignSettingsAs3990Update] = None
    # Composed type representation for type SteelMemberDesignSettingsAs4100Update
    steel_member_design_settings_as4100_update: Optional[SteelMemberDesignSettingsAs4100Update] = None
    # Composed type representation for type SteelMemberDesignSettingsBs5950_1990Update
    steel_member_design_settings_bs5950_1990_update: Optional[SteelMemberDesignSettingsBs5950_1990Update] = None
    # Composed type representation for type SteelMemberDesignSettingsBs5950_2000Update
    steel_member_design_settings_bs5950_2000_update: Optional[SteelMemberDesignSettingsBs5950_2000Update] = None
    # Composed type representation for type SteelMemberDesignSettingsEurocode3_2005Update
    steel_member_design_settings_eurocode3_2005_update: Optional[SteelMemberDesignSettingsEurocode3_2005Update] = None
    # Composed type representation for type SteelMemberDesignSettingsHkCp2011Update
    steel_member_design_settings_hk_cp2011_update: Optional[SteelMemberDesignSettingsHkCp2011Update] = None
    # Composed type representation for type SteelMemberDesignSettingsIs800_2007Update
    steel_member_design_settings_is800_2007_update: Optional[SteelMemberDesignSettingsIs800_2007Update] = None
    # Composed type representation for type SteelMemberDesignSettingsNzs3404Update
    steel_member_design_settings_nzs3404_update: Optional[SteelMemberDesignSettingsNzs3404Update] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignRunDesignRequest_codeSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignRunDesignRequest_codeSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("code")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SteelMemberDesignRunDesignRequest_codeSettings()
        if mapping_value and mapping_value.casefold() == "AiscAsd1989".casefold():
            from .steel_member_design_settings_aisc_asd1989_update import SteelMemberDesignSettingsAiscAsd1989Update

            result.steel_member_design_settings_aisc_asd1989_update = SteelMemberDesignSettingsAiscAsd1989Update()
        elif mapping_value and mapping_value.casefold() == "AiscAsd360".casefold():
            from .steel_member_design_settings_aisc_asd360_update import SteelMemberDesignSettingsAiscAsd360Update

            result.steel_member_design_settings_aisc_asd360_update = SteelMemberDesignSettingsAiscAsd360Update()
        elif mapping_value and mapping_value.casefold() == "AiscLrfd1993".casefold():
            from .steel_member_design_settings_aisc_lrfd1993_update import SteelMemberDesignSettingsAiscLrfd1993Update

            result.steel_member_design_settings_aisc_lrfd1993_update = SteelMemberDesignSettingsAiscLrfd1993Update()
        elif mapping_value and mapping_value.casefold() == "AiscLrfd360".casefold():
            from .steel_member_design_settings_aisc_lrfd360_update import SteelMemberDesignSettingsAiscLrfd360Update

            result.steel_member_design_settings_aisc_lrfd360_update = SteelMemberDesignSettingsAiscLrfd360Update()
        elif mapping_value and mapping_value.casefold() == "AsNzs4600DuragalOnly".casefold():
            from .steel_member_design_settings_as_nzs4600_duragal_only_update import SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate

            result.steel_member_design_settings_as_nzs4600_duragal_only_update = SteelMemberDesignSettingsAsNzs4600DuragalOnlyUpdate()
        elif mapping_value and mapping_value.casefold() == "AsNzs4600".casefold():
            from .steel_member_design_settings_as_nzs4600_update import SteelMemberDesignSettingsAsNzs4600Update

            result.steel_member_design_settings_as_nzs4600_update = SteelMemberDesignSettingsAsNzs4600Update()
        elif mapping_value and mapping_value.casefold() == "As1250".casefold():
            from .steel_member_design_settings_as1250_update import SteelMemberDesignSettingsAs1250Update

            result.steel_member_design_settings_as1250_update = SteelMemberDesignSettingsAs1250Update()
        elif mapping_value and mapping_value.casefold() == "As3990".casefold():
            from .steel_member_design_settings_as3990_update import SteelMemberDesignSettingsAs3990Update

            result.steel_member_design_settings_as3990_update = SteelMemberDesignSettingsAs3990Update()
        elif mapping_value and mapping_value.casefold() == "As4100".casefold():
            from .steel_member_design_settings_as4100_update import SteelMemberDesignSettingsAs4100Update

            result.steel_member_design_settings_as4100_update = SteelMemberDesignSettingsAs4100Update()
        elif mapping_value and mapping_value.casefold() == "Bs5950_1990".casefold():
            from .steel_member_design_settings_bs5950_1990_update import SteelMemberDesignSettingsBs5950_1990Update

            result.steel_member_design_settings_bs5950_1990_update = SteelMemberDesignSettingsBs5950_1990Update()
        elif mapping_value and mapping_value.casefold() == "Bs5950_2000".casefold():
            from .steel_member_design_settings_bs5950_2000_update import SteelMemberDesignSettingsBs5950_2000Update

            result.steel_member_design_settings_bs5950_2000_update = SteelMemberDesignSettingsBs5950_2000Update()
        elif mapping_value and mapping_value.casefold() == "Eurocode3_2005".casefold():
            from .steel_member_design_settings_eurocode3_2005_update import SteelMemberDesignSettingsEurocode3_2005Update

            result.steel_member_design_settings_eurocode3_2005_update = SteelMemberDesignSettingsEurocode3_2005Update()
        elif mapping_value and mapping_value.casefold() == "HkCp2011".casefold():
            from .steel_member_design_settings_hk_cp2011_update import SteelMemberDesignSettingsHkCp2011Update

            result.steel_member_design_settings_hk_cp2011_update = SteelMemberDesignSettingsHkCp2011Update()
        elif mapping_value and mapping_value.casefold() == "Is800_2007".casefold():
            from .steel_member_design_settings_is800_2007_update import SteelMemberDesignSettingsIs800_2007Update

            result.steel_member_design_settings_is800_2007_update = SteelMemberDesignSettingsIs800_2007Update()
        elif mapping_value and mapping_value.casefold() == "Nzs3404".casefold():
            from .steel_member_design_settings_nzs3404_update import SteelMemberDesignSettingsNzs3404Update

            result.steel_member_design_settings_nzs3404_update = SteelMemberDesignSettingsNzs3404Update()
        return result
    
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

        if self.steel_member_design_settings_aisc_asd1989_update:
            return self.steel_member_design_settings_aisc_asd1989_update.get_field_deserializers()
        if self.steel_member_design_settings_aisc_asd360_update:
            return self.steel_member_design_settings_aisc_asd360_update.get_field_deserializers()
        if self.steel_member_design_settings_aisc_lrfd1993_update:
            return self.steel_member_design_settings_aisc_lrfd1993_update.get_field_deserializers()
        if self.steel_member_design_settings_aisc_lrfd360_update:
            return self.steel_member_design_settings_aisc_lrfd360_update.get_field_deserializers()
        if self.steel_member_design_settings_as_nzs4600_duragal_only_update:
            return self.steel_member_design_settings_as_nzs4600_duragal_only_update.get_field_deserializers()
        if self.steel_member_design_settings_as_nzs4600_update:
            return self.steel_member_design_settings_as_nzs4600_update.get_field_deserializers()
        if self.steel_member_design_settings_as1250_update:
            return self.steel_member_design_settings_as1250_update.get_field_deserializers()
        if self.steel_member_design_settings_as3990_update:
            return self.steel_member_design_settings_as3990_update.get_field_deserializers()
        if self.steel_member_design_settings_as4100_update:
            return self.steel_member_design_settings_as4100_update.get_field_deserializers()
        if self.steel_member_design_settings_bs5950_1990_update:
            return self.steel_member_design_settings_bs5950_1990_update.get_field_deserializers()
        if self.steel_member_design_settings_bs5950_2000_update:
            return self.steel_member_design_settings_bs5950_2000_update.get_field_deserializers()
        if self.steel_member_design_settings_eurocode3_2005_update:
            return self.steel_member_design_settings_eurocode3_2005_update.get_field_deserializers()
        if self.steel_member_design_settings_hk_cp2011_update:
            return self.steel_member_design_settings_hk_cp2011_update.get_field_deserializers()
        if self.steel_member_design_settings_is800_2007_update:
            return self.steel_member_design_settings_is800_2007_update.get_field_deserializers()
        if self.steel_member_design_settings_nzs3404_update:
            return self.steel_member_design_settings_nzs3404_update.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.steel_member_design_settings_aisc_asd1989_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_asd1989_update)
        elif self.steel_member_design_settings_aisc_asd360_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_asd360_update)
        elif self.steel_member_design_settings_aisc_lrfd1993_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_lrfd1993_update)
        elif self.steel_member_design_settings_aisc_lrfd360_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_aisc_lrfd360_update)
        elif self.steel_member_design_settings_as_nzs4600_duragal_only_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as_nzs4600_duragal_only_update)
        elif self.steel_member_design_settings_as_nzs4600_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as_nzs4600_update)
        elif self.steel_member_design_settings_as1250_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as1250_update)
        elif self.steel_member_design_settings_as3990_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as3990_update)
        elif self.steel_member_design_settings_as4100_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_as4100_update)
        elif self.steel_member_design_settings_bs5950_1990_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_bs5950_1990_update)
        elif self.steel_member_design_settings_bs5950_2000_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_bs5950_2000_update)
        elif self.steel_member_design_settings_eurocode3_2005_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_eurocode3_2005_update)
        elif self.steel_member_design_settings_hk_cp2011_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_hk_cp2011_update)
        elif self.steel_member_design_settings_is800_2007_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_is800_2007_update)
        elif self.steel_member_design_settings_nzs3404_update is not None:
            writer.write_object_value(None, self.steel_member_design_settings_nzs3404_update)
    

