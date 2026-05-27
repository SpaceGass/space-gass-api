from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MaterialCreate(Parsable):
    """
    DTO for creating a new user-defined material.
    """
    # Concrete compressive strength.
    concrete_strength: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # Mass density. Must be greater than zero.
    mass_density: Optional[float] = None
    # Material name.
    name: Optional[str] = None
    # Poisson's ratio (unitless).
    poissons_ratio: Optional[float] = None
    # Thermal expansion coefficient.
    thermal_coeff: Optional[float] = None
    # Young's modulus. Must be greater than zero.
    youngs_modulus: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MaterialCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MaterialCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MaterialCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "concreteStrength": lambda n : setattr(self, 'concrete_strength', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "massDensity": lambda n : setattr(self, 'mass_density', n.get_float_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "poissonsRatio": lambda n : setattr(self, 'poissons_ratio', n.get_float_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_float_value("massDensity", self.mass_density)
        writer.write_str_value("name", self.name)
        writer.write_float_value("poissonsRatio", self.poissons_ratio)
        writer.write_float_value("thermalCoeff", self.thermal_coeff)
        writer.write_float_value("youngsModulus", self.youngs_modulus)
    

