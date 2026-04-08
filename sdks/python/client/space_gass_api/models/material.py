from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .property_source import PropertySource

@dataclass
class Material(Parsable):
    """
    DTO for reading a material entity.
    """
    # Concrete compressive strength.
    concrete_strength: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary key - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    key: Optional[int] = None
    # Library name. Empty for user-defined materials.
    library: Optional[str] = None
    # Mass density.
    mass_density: Optional[float] = None
    # Material name.
    name: Optional[str] = None
    # Poisson's ratio (unitless).
    poissons_ratio: Optional[float] = None
    # Indicates whether a section or material was user-defined or imported from a library.
    source: Optional[PropertySource] = None
    # Thermal expansion coefficient.
    thermal_coeff: Optional[float] = None
    # Young's modulus.
    youngs_modulus: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Material:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Material
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Material()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .property_source import PropertySource

        from .property_source import PropertySource

        fields: dict[str, Callable[[Any], None]] = {
            "concreteStrength": lambda n : setattr(self, 'concrete_strength', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "massDensity": lambda n : setattr(self, 'mass_density', n.get_float_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "poissonsRatio": lambda n : setattr(self, 'poissons_ratio', n.get_float_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(PropertySource)),
            "thermalCoeff": lambda n : setattr(self, 'thermal_coeff', n.get_float_value()),
            "youngsModulus": lambda n : setattr(self, 'youngs_modulus', n.get_float_value()),
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
        writer.write_float_value("concreteStrength", self.concrete_strength)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("key", self.key)
        writer.write_str_value("library", self.library)
        writer.write_float_value("massDensity", self.mass_density)
        writer.write_str_value("name", self.name)
        writer.write_float_value("poissonsRatio", self.poissons_ratio)
        writer.write_enum_value("source", self.source)
        writer.write_float_value("thermalCoeff", self.thermal_coeff)
        writer.write_float_value("youngsModulus", self.youngs_modulus)
    

