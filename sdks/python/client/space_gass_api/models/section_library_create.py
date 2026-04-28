from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .angle_type import AngleType

@dataclass
class SectionLibraryCreate(Parsable):
    """
    DTO for creating a library-sourced section. Structural properties (A, J, Iy, Iz, etc.)and cross-section shape data are resolved from the SPACE GASS section library by(name, library).
    """
    # Angle section type for structural sections.Maps to SPACE GASS lookup table "Angle Type".
    angle_type: Optional[AngleType] = None
    # Area modification factor.
    area_factor: Optional[float] = None
    # Shear area in the Y direction.
    ay: Optional[float] = None
    # Shear area in the Z direction.
    az: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # Iy modification factor.
    iy_factor: Optional[float] = None
    # Iz modification factor.
    iz_factor: Optional[float] = None
    # Library name.
    library: Optional[str] = None
    # Section mark / designation.
    mark: Optional[str] = None
    # Section item name within the library.
    name: Optional[str] = None
    # Torsion modification factor.
    torsion_factor: Optional[float] = None
    # Whether the section's principal axes are swapped (transposed shape).
    transposed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionLibraryCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionLibraryCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionLibraryCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .angle_type import AngleType

        from .angle_type import AngleType

        fields: dict[str, Callable[[Any], None]] = {
            "angleType": lambda n : setattr(self, 'angle_type', n.get_enum_value(AngleType)),
            "areaFactor": lambda n : setattr(self, 'area_factor', n.get_float_value()),
            "ay": lambda n : setattr(self, 'ay', n.get_float_value()),
            "az": lambda n : setattr(self, 'az', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "iyFactor": lambda n : setattr(self, 'iy_factor', n.get_float_value()),
            "izFactor": lambda n : setattr(self, 'iz_factor', n.get_float_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "mark": lambda n : setattr(self, 'mark', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "torsionFactor": lambda n : setattr(self, 'torsion_factor', n.get_float_value()),
            "transposed": lambda n : setattr(self, 'transposed', n.get_bool_value()),
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
        writer.write_enum_value("angleType", self.angle_type)
        writer.write_float_value("areaFactor", self.area_factor)
        writer.write_float_value("ay", self.ay)
        writer.write_float_value("az", self.az)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_float_value("iyFactor", self.iy_factor)
        writer.write_float_value("izFactor", self.iz_factor)
        writer.write_str_value("library", self.library)
        writer.write_str_value("mark", self.mark)
        writer.write_str_value("name", self.name)
        writer.write_float_value("torsionFactor", self.torsion_factor)
        writer.write_bool_value("transposed", self.transposed)
    

