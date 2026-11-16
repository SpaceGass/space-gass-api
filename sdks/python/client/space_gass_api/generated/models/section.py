from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .angle_type import AngleType
    from .design_properties import DesignProperties
    from .property_source import PropertySource
    from .section_shapes import Section_shapes

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
    # Shear area in the Y direction.
    ay: Optional[float] = None
    # Shear area in the Z direction.
    az: Optional[float] = None
    # The steel design properties of a geometry-backed section: fabrication method and thenormal/high strength grades. In SPACE GASS these apply across the whole section.
    design_properties: Optional[DesignProperties] = None
    # Whether the section has shape geometry (a shape-builder or library section).
    has_shapes: Optional[bool] = None
    # Primary identifier - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
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
    # Library name.
    library: Optional[str] = None
    # Section mark / designation.
    mark: Optional[str] = None
    # Section name.
    name: Optional[str] = None
    # Principal axis rotation angle.
    principal_angle: Optional[float] = None
    # Number of shapes composited into the section.
    shape_count: Optional[int] = None
    # The shapes composited into the section, in order.
    shapes: Optional[list[Section_shapes]] = None
    # Indicates whether a section or material was user-defined or imported from a library.
    source: Optional[PropertySource] = None
    # Torsion modification factor.
    torsion_factor: Optional[float] = None
    # Whether the section's principal axes are swapped (transposed shape).
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
        from .design_properties import DesignProperties
        from .property_source import PropertySource
        from .section_shapes import Section_shapes

        from .angle_type import AngleType
        from .design_properties import DesignProperties
        from .property_source import PropertySource
        from .section_shapes import Section_shapes

        fields: dict[str, Callable[[Any], None]] = {
            "a": lambda n : setattr(self, 'a', n.get_float_value()),
            "angleType": lambda n : setattr(self, 'angle_type', n.get_enum_value(AngleType)),
            "areaFactor": lambda n : setattr(self, 'area_factor', n.get_float_value()),
            "ay": lambda n : setattr(self, 'ay', n.get_float_value()),
            "az": lambda n : setattr(self, 'az', n.get_float_value()),
            "designProperties": lambda n : setattr(self, 'design_properties', n.get_object_value(DesignProperties)),
            "hasShapes": lambda n : setattr(self, 'has_shapes', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "iy": lambda n : setattr(self, 'iy', n.get_float_value()),
            "iyFactor": lambda n : setattr(self, 'iy_factor', n.get_float_value()),
            "iz": lambda n : setattr(self, 'iz', n.get_float_value()),
            "izFactor": lambda n : setattr(self, 'iz_factor', n.get_float_value()),
            "j": lambda n : setattr(self, 'j', n.get_float_value()),
            "library": lambda n : setattr(self, 'library', n.get_str_value()),
            "mark": lambda n : setattr(self, 'mark', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "principalAngle": lambda n : setattr(self, 'principal_angle', n.get_float_value()),
            "shapeCount": lambda n : setattr(self, 'shape_count', n.get_int_value()),
            "shapes": lambda n : setattr(self, 'shapes', n.get_collection_of_object_values(Section_shapes)),
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
        writer.write_object_value("designProperties", self.design_properties)
        writer.write_bool_value("hasShapes", self.has_shapes)
        writer.write_int_value("id", self.id)
        writer.write_float_value("iy", self.iy)
        writer.write_float_value("iyFactor", self.iy_factor)
        writer.write_float_value("iz", self.iz)
        writer.write_float_value("izFactor", self.iz_factor)
        writer.write_float_value("j", self.j)
        writer.write_str_value("library", self.library)
        writer.write_str_value("mark", self.mark)
        writer.write_str_value("name", self.name)
        writer.write_float_value("principalAngle", self.principal_angle)
        writer.write_int_value("shapeCount", self.shape_count)
        writer.write_collection_of_object_values("shapes", self.shapes)
        writer.write_enum_value("source", self.source)
        writer.write_float_value("torsionFactor", self.torsion_factor)
        writer.write_bool_value("transposed", self.transposed)
    

