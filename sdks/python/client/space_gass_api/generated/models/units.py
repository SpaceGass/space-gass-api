from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .acceleration_unit import AccelerationUnit
    from .force_unit import ForceUnit
    from .length_unit import LengthUnit
    from .mass_density_unit import MassDensityUnit
    from .mass_unit import MassUnit
    from .material_strength_unit import MaterialStrengthUnit
    from .moment_unit import MomentUnit
    from .section_properties_unit import SectionPropertiesUnit
    from .stress_unit import StressUnit
    from .temperature_unit import TemperatureUnit
    from .translation_unit import TranslationUnit

@dataclass
class Units(Parsable):
    """
    Unit settings for the current job.
    """
    # Acceleration unit. Members mirror SPACE GASS `SgAcceleration`.
    acceleration: Optional[AccelerationUnit] = None
    # Force unit. Members mirror SPACE GASS `SgForce`.
    force: Optional[ForceUnit] = None
    # Length unit. Members mirror SPACE GASS `SGLength`(`NetCommon/CommonEnums.vb`); integer values and identifiers must stay inlock-step with it. The System.ComponentModel.DescriptionAttribute carries the displaylabel (mirrors `gcUNITS_LABEL_*`).
    length: Optional[LengthUnit] = None
    # Mass unit. Members mirror SPACE GASS `SgMass`.
    mass: Optional[MassUnit] = None
    # Mass density unit. Members mirror SPACE GASS `SgMassDensity`.
    mass_density: Optional[MassDensityUnit] = None
    # Material strength unit (yield stress, ultimate stress, etc.). Members mirrorSPACE GASS `SgMaterialStrength`.
    material_strength: Optional[MaterialStrengthUnit] = None
    # Moment unit. Members mirror SPACE GASS `SgMoment`.
    moment: Optional[MomentUnit] = None
    # Unit for section properties (area, moment of inertia, etc.). Members mirrorSPACE GASS `SgSectionProperties` (`NetCommon/CommonEnums.vb`).
    section_properties: Optional[SectionPropertiesUnit] = None
    # Stress unit. Members mirror SPACE GASS `SgStress`.
    stress: Optional[StressUnit] = None
    # Temperature unit. Members mirror SPACE GASS `SgTemperature`.
    temperature: Optional[TemperatureUnit] = None
    # Translation (displacement) unit. Members mirror SPACE GASS `SgTranslation`.SG uses `inch` here (not `in`) to dodge the VB reserved word; we mirrorthat so the wire token stays `"inch"`.
    translation: Optional[TranslationUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Units:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Units
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Units()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .acceleration_unit import AccelerationUnit
        from .force_unit import ForceUnit
        from .length_unit import LengthUnit
        from .mass_density_unit import MassDensityUnit
        from .mass_unit import MassUnit
        from .material_strength_unit import MaterialStrengthUnit
        from .moment_unit import MomentUnit
        from .section_properties_unit import SectionPropertiesUnit
        from .stress_unit import StressUnit
        from .temperature_unit import TemperatureUnit
        from .translation_unit import TranslationUnit

        from .acceleration_unit import AccelerationUnit
        from .force_unit import ForceUnit
        from .length_unit import LengthUnit
        from .mass_density_unit import MassDensityUnit
        from .mass_unit import MassUnit
        from .material_strength_unit import MaterialStrengthUnit
        from .moment_unit import MomentUnit
        from .section_properties_unit import SectionPropertiesUnit
        from .stress_unit import StressUnit
        from .temperature_unit import TemperatureUnit
        from .translation_unit import TranslationUnit

        fields: dict[str, Callable[[Any], None]] = {
            "acceleration": lambda n : setattr(self, 'acceleration', n.get_enum_value(AccelerationUnit)),
            "force": lambda n : setattr(self, 'force', n.get_enum_value(ForceUnit)),
            "length": lambda n : setattr(self, 'length', n.get_enum_value(LengthUnit)),
            "mass": lambda n : setattr(self, 'mass', n.get_enum_value(MassUnit)),
            "massDensity": lambda n : setattr(self, 'mass_density', n.get_enum_value(MassDensityUnit)),
            "materialStrength": lambda n : setattr(self, 'material_strength', n.get_enum_value(MaterialStrengthUnit)),
            "moment": lambda n : setattr(self, 'moment', n.get_enum_value(MomentUnit)),
            "sectionProperties": lambda n : setattr(self, 'section_properties', n.get_enum_value(SectionPropertiesUnit)),
            "stress": lambda n : setattr(self, 'stress', n.get_enum_value(StressUnit)),
            "temperature": lambda n : setattr(self, 'temperature', n.get_enum_value(TemperatureUnit)),
            "translation": lambda n : setattr(self, 'translation', n.get_enum_value(TranslationUnit)),
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
        writer.write_enum_value("acceleration", self.acceleration)
        writer.write_enum_value("force", self.force)
        writer.write_enum_value("length", self.length)
        writer.write_enum_value("mass", self.mass)
        writer.write_enum_value("massDensity", self.mass_density)
        writer.write_enum_value("materialStrength", self.material_strength)
        writer.write_enum_value("moment", self.moment)
        writer.write_enum_value("sectionProperties", self.section_properties)
        writer.write_enum_value("stress", self.stress)
        writer.write_enum_value("temperature", self.temperature)
        writer.write_enum_value("translation", self.translation)
    

