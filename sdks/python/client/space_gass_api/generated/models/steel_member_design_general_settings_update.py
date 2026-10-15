from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SteelMemberDesignGeneralSettingsUpdate(Parsable):
    """
    Update request for the general steel member design settings.Only fields included in the request are updated; omit a field to keep its current value.Used by PATCH /job/design/steel-design/settings and the settings overrides on the run endpoints.
    """
    # The adjustLcyForSpecificShapes property
    adjust_lcy_for_specific_shapes: Optional[bool] = None
    # The adjustLcyFromFlangeRestraints property
    adjust_lcy_from_flange_restraints: Optional[bool] = None
    # The compressionEffectiveLengthRatioLimit property
    compression_effective_length_ratio_limit: Optional[float] = None
    # The equalizeDesignSizes property
    equalize_design_sizes: Optional[bool] = None
    # The filterId property
    filter_id: Optional[int] = None
    # The groups property
    groups: Optional[str] = None
    # The loadCases property
    load_cases: Optional[str] = None
    # The loadFactorLimit property
    load_factor_limit: Optional[float] = None
    # The sectionAvailabilityCommon property
    section_availability_common: Optional[bool] = None
    # The sectionAvailabilityLegacy property
    section_availability_legacy: Optional[bool] = None
    # The sectionAvailabilityObsolete property
    section_availability_obsolete: Optional[bool] = None
    # The sectionAvailabilitySpecial property
    section_availability_special: Optional[bool] = None
    # The sections property
    sections: Optional[str] = None
    # The stations property
    stations: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberDesignGeneralSettingsUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberDesignGeneralSettingsUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberDesignGeneralSettingsUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "adjustLcyForSpecificShapes": lambda n : setattr(self, 'adjust_lcy_for_specific_shapes', n.get_bool_value()),
            "adjustLcyFromFlangeRestraints": lambda n : setattr(self, 'adjust_lcy_from_flange_restraints', n.get_bool_value()),
            "compressionEffectiveLengthRatioLimit": lambda n : setattr(self, 'compression_effective_length_ratio_limit', n.get_float_value()),
            "equalizeDesignSizes": lambda n : setattr(self, 'equalize_design_sizes', n.get_bool_value()),
            "filterId": lambda n : setattr(self, 'filter_id', n.get_int_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_str_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_str_value()),
            "loadFactorLimit": lambda n : setattr(self, 'load_factor_limit', n.get_float_value()),
            "sectionAvailabilityCommon": lambda n : setattr(self, 'section_availability_common', n.get_bool_value()),
            "sectionAvailabilityLegacy": lambda n : setattr(self, 'section_availability_legacy', n.get_bool_value()),
            "sectionAvailabilityObsolete": lambda n : setattr(self, 'section_availability_obsolete', n.get_bool_value()),
            "sectionAvailabilitySpecial": lambda n : setattr(self, 'section_availability_special', n.get_bool_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_str_value()),
            "stations": lambda n : setattr(self, 'stations', n.get_int_value()),
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
        writer.write_bool_value("adjustLcyForSpecificShapes", self.adjust_lcy_for_specific_shapes)
        writer.write_bool_value("adjustLcyFromFlangeRestraints", self.adjust_lcy_from_flange_restraints)
        writer.write_float_value("compressionEffectiveLengthRatioLimit", self.compression_effective_length_ratio_limit)
        writer.write_bool_value("equalizeDesignSizes", self.equalize_design_sizes)
        writer.write_int_value("filterId", self.filter_id)
        writer.write_str_value("groups", self.groups)
        writer.write_str_value("loadCases", self.load_cases)
        writer.write_float_value("loadFactorLimit", self.load_factor_limit)
        writer.write_bool_value("sectionAvailabilityCommon", self.section_availability_common)
        writer.write_bool_value("sectionAvailabilityLegacy", self.section_availability_legacy)
        writer.write_bool_value("sectionAvailabilityObsolete", self.section_availability_obsolete)
        writer.write_bool_value("sectionAvailabilitySpecial", self.section_availability_special)
        writer.write_str_value("sections", self.sections)
        writer.write_int_value("stations", self.stations)
    

