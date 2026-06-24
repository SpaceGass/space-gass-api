from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MaterialUpdate(Parsable):
    """
    DTO for updating an existing material.All fields are optional to support partial updates.
    """
    # Concrete compressive strength.
    concrete_strength: Optional[float] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Mass density. Must be greater than zero if provided.
    mass_density: Optional[float] = None
    # Material name.
    name: Optional[str] = None
    # Poisson's ratio (unitless).
    poissons_ratio: Optional[float] = None
    # Thermal expansion coefficient.
    thermal_coeff: Optional[float] = None
    # Young's modulus. Must be greater than zero if provided.
    youngs_modulus: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MaterialUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MaterialUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MaterialUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "concreteStrength": lambda n : setattr(self, 'concrete_strength', n.get_float_value()),
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
        writer.write_int_value("id", self.id)
        writer.write_float_value("massDensity", self.mass_density)
        writer.write_str_value("name", self.name)
        writer.write_float_value("poissonsRatio", self.poissons_ratio)
        writer.write_float_value("thermalCoeff", self.thermal_coeff)
        writer.write_float_value("youngsModulus", self.youngs_modulus)
    

