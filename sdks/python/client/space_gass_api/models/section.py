from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .angle_type import AngleType
    from .property_source import PropertySource

@dataclass
class Section(Parsable):
    """
    DTO for reading a section entity.
    """
    # Cross-sectional area.
    a: Optional[float] = None
    # Angle section type for structural sections.Maps to SPACE GASS lookup table "Angle Type".
    angle_type: Optional[AngleType] = None
    # Area modification factor.
    area_factor: Optional[float] = None
    # Shear area in Y direction.
    ay: Optional[float] = None
    # Shear area in Z direction.
    az: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Second moment of area about Y axis.
    iy: Optional[float] = None
    # Iy modification factor.
    iy_factor: Optional[float] = None
    # Second moment of area about Z axis.
    iz: Optional[float] = None
    # Iz modification factor.
    iz_factor: Optional[float] = None
    # Torsion constant.
    j: Optional[float] = None
    # Primary key - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    key: Optional[int] = None
    # Library name. Empty for user-defined sections.
    library: Optional[str] = None
    # Section mark/designation.
    mark: Optional[str] = None
    # Section name.
    name: Optional[str] = None
    # Principal axis rotation angle (degrees).
    principal_angle: Optional[float] = None
    # Number of shapes in the section.
    shapes: Optional[int] = None
    # Indicates whether a section or material was user-defined or imported from a library.
    source: Optional[PropertySource] = None
    # Torsion modification factor.
    torsion_factor: Optional[float] = None
    # Whether the section is transposed.
    transposed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Section:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Section
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Section()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .angle_type import AngleType
        from .property_source import PropertySource

        from .angle_type import AngleType
        from .property_source import PropertySource

        fields: dict[str, Callable[[Any], None]] = {
            "a": lambda n : setattr(self, 'a', n.get_float_value()),
            "angleType": lambda n : setattr(self, 'angle_type', n.get_enum_value(AngleType)),
            "areaFactor": lambda n : setattr(self, 'area_factor', n.get_float_value()),
            "ay": lambda n : setattr(self, 'ay', n.get_float_value()),
            "az": lambda n : setattr(self, 'az', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "iy": lambda n : setattr(self, 'iy', n.get_float_value()),
            "iyFactor": lambda n : setattr(self, 'iy_factor', n.get_float_value()),
            "iz": lambda n : setattr(self, 'iz', n.get_float_value()),
            "izFactor": lambda n : setattr(self, 'iz_factor', n.get_float_value()),
            "j": lambda n : setattr(self, 'j', n.get_float_value()),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "mark": lambda n : setattr(self, 'mark', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "principalAngle": lambda n : setattr(self, 'principal_angle', n.get_float_value()),
            "shapes": lambda n : setattr(self, 'shapes', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(PropertySource)),
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
        writer.write_float_value("a", self.a)
        writer.write_enum_value("angleType", self.angle_type)
        writer.write_float_value("areaFactor", self.area_factor)
        writer.write_float_value("ay", self.ay)
        writer.write_float_value("az", self.az)
        writer.write_str_value("guid", self.guid)
        writer.write_float_value("iy", self.iy)
        writer.write_float_value("iyFactor", self.iy_factor)
        writer.write_float_value("iz", self.iz)
        writer.write_float_value("izFactor", self.iz_factor)
        writer.write_float_value("j", self.j)
        writer.write_int_value("key", self.key)
        writer.write_str_value("library", self.library)
        writer.write_str_value("mark", self.mark)
        writer.write_str_value("name", self.name)
        writer.write_float_value("principalAngle", self.principal_angle)
        writer.write_int_value("shapes", self.shapes)
        writer.write_enum_value("source", self.source)
        writer.write_float_value("torsionFactor", self.torsion_factor)
        writer.write_bool_value("transposed", self.transposed)
    

