from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlateElementForce(Parsable):
    """
    Plate element force result for a specific load case (FileId 207).
    """
    # Membrane force in X. Unit: Force/Length (see GET /job/units).
    fx: Optional[float] = None
    # Membrane shear force. Unit: Force/Length (see GET /job/units).
    fxy: Optional[float] = None
    # Membrane force in Y. Unit: Force/Length (see GET /job/units).
    fy: Optional[float] = None
    # Load case ID.
    load_case: Optional[int] = None
    # Bending moment about X. Unit: Moment/Length (see GET /job/units).
    mx: Optional[float] = None
    # Bending moment about X at bottom surface. Unit: Moment/Length (see GET /job/units).
    mx_btm: Optional[float] = None
    # Bending moment about X at top surface. Unit: Moment/Length (see GET /job/units).
    mx_top: Optional[float] = None
    # Twisting moment. Unit: Moment/Length (see GET /job/units).
    mxy: Optional[float] = None
    # Bending moment about Y. Unit: Moment/Length (see GET /job/units).
    my: Optional[float] = None
    # Bending moment about Y at bottom surface. Unit: Moment/Length (see GET /job/units).
    my_btm: Optional[float] = None
    # Bending moment about Y at top surface. Unit: Moment/Length (see GET /job/units).
    my_top: Optional[float] = None
    # Plate key.
    plate: Optional[int] = None
    # Transverse shear in XZ. Unit: Force/Length (see GET /job/units).
    vxz: Optional[float] = None
    # Transverse shear in YZ. Unit: Force/Length (see GET /job/units).
    vyz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateElementForce:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateElementForce
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateElementForce()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fxy": lambda n : setattr(self, 'fxy', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "mxBtm": lambda n : setattr(self, 'mx_btm', n.get_float_value()),
            "mxTop": lambda n : setattr(self, 'mx_top', n.get_float_value()),
            "mxy": lambda n : setattr(self, 'mxy', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "myBtm": lambda n : setattr(self, 'my_btm', n.get_float_value()),
            "myTop": lambda n : setattr(self, 'my_top', n.get_float_value()),
            "plate": lambda n : setattr(self, 'plate', n.get_int_value()),
            "vxz": lambda n : setattr(self, 'vxz', n.get_float_value()),
            "vyz": lambda n : setattr(self, 'vyz', n.get_float_value()),
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
        writer.write_float_value("fx", self.fx)
        writer.write_float_value("fxy", self.fxy)
        writer.write_float_value("fy", self.fy)
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("mxBtm", self.mx_btm)
        writer.write_float_value("mxTop", self.mx_top)
        writer.write_float_value("mxy", self.mxy)
        writer.write_float_value("my", self.my)
        writer.write_float_value("myBtm", self.my_btm)
        writer.write_float_value("myTop", self.my_top)
        writer.write_int_value("plate", self.plate)
        writer.write_float_value("vxz", self.vxz)
        writer.write_float_value("vyz", self.vyz)
    

