from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MovingLoadPressureCreate(Parsable):
    """
    Creates a new moving-load pressure.
    """
    # Patch length, along the travel path. 0 means stationary, full-length.
    length: Optional[float] = None
    # Spacing between discretised load points within the patch.
    load_spacing: Optional[float] = None
    # The pressure name. Must be unique across all pressures.
    name: Optional[str] = None
    # Pressure component along global X.
    px: Optional[float] = None
    # Pressure component along global Y.
    py: Optional[float] = None
    # Pressure component along global Z.
    pz: Optional[float] = None
    # Patch width, perpendicular to the travel path.
    width: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MovingLoadPressureCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MovingLoadPressureCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MovingLoadPressureCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "length": lambda n : setattr(self, 'length', n.get_float_value()),
            "loadSpacing": lambda n : setattr(self, 'load_spacing', n.get_float_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "px": lambda n : setattr(self, 'px', n.get_float_value()),
            "py": lambda n : setattr(self, 'py', n.get_float_value()),
            "pz": lambda n : setattr(self, 'pz', n.get_float_value()),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
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
        writer.write_float_value("length", self.length)
        writer.write_float_value("loadSpacing", self.load_spacing)
        writer.write_str_value("name", self.name)
        writer.write_float_value("px", self.px)
        writer.write_float_value("py", self.py)
        writer.write_float_value("pz", self.pz)
        writer.write_float_value("width", self.width)
    

