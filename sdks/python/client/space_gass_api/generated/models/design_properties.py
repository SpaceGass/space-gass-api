from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .shape_fabrication import ShapeFabrication
    from .steel_strength import SteelStrength

@dataclass
class DesignProperties(Parsable):
    """
    The steel design properties of a geometry-backed section: fabrication method and thenormal/high strength grades. In SPACE GASS these apply across the whole section.
    """
    # Fabrication method of a cross-section shape. Affects residual-stress assumptions insteel design.
    fabrication: Optional[ShapeFabrication] = None
    # Steel strength values for one grade of a shape (yield and ultimate stresses).
    strength_high: Optional[SteelStrength] = None
    # Steel strength values for one grade of a shape (yield and ultimate stresses).
    strength_normal: Optional[SteelStrength] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DesignProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DesignProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DesignProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .shape_fabrication import ShapeFabrication
        from .steel_strength import SteelStrength

        from .shape_fabrication import ShapeFabrication
        from .steel_strength import SteelStrength

        fields: dict[str, Callable[[Any], None]] = {
            "fabrication": lambda n : setattr(self, 'fabrication', n.get_enum_value(ShapeFabrication)),
            "strengthHigh": lambda n : setattr(self, 'strength_high', n.get_object_value(SteelStrength)),
            "strengthNormal": lambda n : setattr(self, 'strength_normal', n.get_object_value(SteelStrength)),
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
        writer.write_enum_value("fabrication", self.fabrication)
        writer.write_object_value("strengthHigh", self.strength_high)
        writer.write_object_value("strengthNormal", self.strength_normal)
    

