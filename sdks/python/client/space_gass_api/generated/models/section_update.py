from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SectionUpdate(Parsable):
    """
    DTO for partially updating an existing section. All fields are optional — only fieldspresent on the request are updated.
    """
    # Cross-sectional area.
    a: Optional[float] = None
    # Area modification factor.
    area_factor: Optional[float] = None
    # Shear area in the Y direction.
    ay: Optional[float] = None
    # Shear area in the Z direction.
    az: Optional[float] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Second moment of area about the principal Y axis.
    iy: Optional[float] = None
    # Iy modification factor.
    iy_factor: Optional[float] = None
    # Second moment of area about the principal Z axis.
    iz: Optional[float] = None
    # Iz modification factor.
    iz_factor: Optional[float] = None
    # Torsion constant.
    j: Optional[float] = None
    # Section mark / designation.
    mark: Optional[str] = None
    # Section name.
    name: Optional[str] = None
    # Principal axis rotation angle.
    principal_angle: Optional[float] = None
    # Torsion modification factor.
    torsion_factor: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "a": lambda n : setattr(self, 'a', n.get_float_value()),
            "areaFactor": lambda n : setattr(self, 'area_factor', n.get_float_value()),
            "ay": lambda n : setattr(self, 'ay', n.get_float_value()),
            "az": lambda n : setattr(self, 'az', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "iy": lambda n : setattr(self, 'iy', n.get_float_value()),
            "iyFactor": lambda n : setattr(self, 'iy_factor', n.get_float_value()),
            "iz": lambda n : setattr(self, 'iz', n.get_float_value()),
            "izFactor": lambda n : setattr(self, 'iz_factor', n.get_float_value()),
            "j": lambda n : setattr(self, 'j', n.get_float_value()),
            "mark": lambda n : setattr(self, 'mark', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "principalAngle": lambda n : setattr(self, 'principal_angle', n.get_float_value()),
            "torsionFactor": lambda n : setattr(self, 'torsion_factor', n.get_float_value()),
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
        writer.write_float_value("a", self.a)
        writer.write_float_value("areaFactor", self.area_factor)
        writer.write_float_value("ay", self.ay)
        writer.write_float_value("az", self.az)
        writer.write_int_value("id", self.id)
        writer.write_float_value("iy", self.iy)
        writer.write_float_value("iyFactor", self.iy_factor)
        writer.write_float_value("iz", self.iz)
        writer.write_float_value("izFactor", self.iz_factor)
        writer.write_float_value("j", self.j)
        writer.write_str_value("mark", self.mark)
        writer.write_str_value("name", self.name)
        writer.write_float_value("principalAngle", self.principal_angle)
        writer.write_float_value("torsionFactor", self.torsion_factor)
    

