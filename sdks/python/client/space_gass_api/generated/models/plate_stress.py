from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlateStress(Parsable):
    """
    Plate stress result for a specific load case (FileId 208).
    """
    # Load case ID.
    load_case: Optional[int] = None
    # Principal angle at bottom surface. Unit: Rotation (see GET /job/units).
    pa_btm: Optional[float] = None
    # Principal angle at top surface. Unit: Rotation (see GET /job/units).
    pa_top: Optional[float] = None
    # Plate key.
    plate: Optional[int] = None
    # Von Mises stress at bottom surface. Unit: Stress (see GET /job/units).
    svm_btm: Optional[float] = None
    # Von Mises stress at top surface. Unit: Stress (see GET /job/units).
    svm_top: Optional[float] = None
    # Normal stress in X at bottom surface. Unit: Stress (see GET /job/units).
    sx_btm: Optional[float] = None
    # Normal stress in X at top surface. Unit: Stress (see GET /job/units).
    sx_top: Optional[float] = None
    # Principal stress in X at bottom surface. Unit: Stress (see GET /job/units).
    sxp_btm: Optional[float] = None
    # Principal stress in X at top surface. Unit: Stress (see GET /job/units).
    sxp_top: Optional[float] = None
    # Normal stress in Y at bottom surface. Unit: Stress (see GET /job/units).
    sy_btm: Optional[float] = None
    # Normal stress in Y at top surface. Unit: Stress (see GET /job/units).
    sy_top: Optional[float] = None
    # Principal stress in Y at bottom surface. Unit: Stress (see GET /job/units).
    syp_btm: Optional[float] = None
    # Principal stress in Y at top surface. Unit: Stress (see GET /job/units).
    syp_top: Optional[float] = None
    # Maximum shear stress at bottom surface. Unit: Stress (see GET /job/units).
    tmax_btm: Optional[float] = None
    # Maximum shear stress at top surface. Unit: Stress (see GET /job/units).
    tmax_top: Optional[float] = None
    # Shear stress XY at bottom surface. Unit: Stress (see GET /job/units).
    txy_btm: Optional[float] = None
    # Shear stress XY at top surface. Unit: Stress (see GET /job/units).
    txy_top: Optional[float] = None
    # Transverse shear stress in XZ. Unit: Stress (see GET /job/units).
    txz: Optional[float] = None
    # Transverse shear stress in YZ. Unit: Stress (see GET /job/units).
    tyz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateStress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateStress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateStress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "loadCase": lambda n : setattr(self, 'load_case', n.get_int_value()),
            "paBtm": lambda n : setattr(self, 'pa_btm', n.get_float_value()),
            "paTop": lambda n : setattr(self, 'pa_top', n.get_float_value()),
            "plate": lambda n : setattr(self, 'plate', n.get_int_value()),
            "svmBtm": lambda n : setattr(self, 'svm_btm', n.get_float_value()),
            "svmTop": lambda n : setattr(self, 'svm_top', n.get_float_value()),
            "sxBtm": lambda n : setattr(self, 'sx_btm', n.get_float_value()),
            "sxTop": lambda n : setattr(self, 'sx_top', n.get_float_value()),
            "sxpBtm": lambda n : setattr(self, 'sxp_btm', n.get_float_value()),
            "sxpTop": lambda n : setattr(self, 'sxp_top', n.get_float_value()),
            "syBtm": lambda n : setattr(self, 'sy_btm', n.get_float_value()),
            "syTop": lambda n : setattr(self, 'sy_top', n.get_float_value()),
            "sypBtm": lambda n : setattr(self, 'syp_btm', n.get_float_value()),
            "sypTop": lambda n : setattr(self, 'syp_top', n.get_float_value()),
            "tmaxBtm": lambda n : setattr(self, 'tmax_btm', n.get_float_value()),
            "tmaxTop": lambda n : setattr(self, 'tmax_top', n.get_float_value()),
            "txyBtm": lambda n : setattr(self, 'txy_btm', n.get_float_value()),
            "txyTop": lambda n : setattr(self, 'txy_top', n.get_float_value()),
            "txz": lambda n : setattr(self, 'txz', n.get_float_value()),
            "tyz": lambda n : setattr(self, 'tyz', n.get_float_value()),
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
        writer.write_int_value("loadCase", self.load_case)
        writer.write_float_value("paBtm", self.pa_btm)
        writer.write_float_value("paTop", self.pa_top)
        writer.write_int_value("plate", self.plate)
        writer.write_float_value("svmBtm", self.svm_btm)
        writer.write_float_value("svmTop", self.svm_top)
        writer.write_float_value("sxBtm", self.sx_btm)
        writer.write_float_value("sxTop", self.sx_top)
        writer.write_float_value("sxpBtm", self.sxp_btm)
        writer.write_float_value("sxpTop", self.sxp_top)
        writer.write_float_value("syBtm", self.sy_btm)
        writer.write_float_value("syTop", self.sy_top)
        writer.write_float_value("sypBtm", self.syp_btm)
        writer.write_float_value("sypTop", self.syp_top)
        writer.write_float_value("tmaxBtm", self.tmax_btm)
        writer.write_float_value("tmaxTop", self.tmax_top)
        writer.write_float_value("txyBtm", self.txy_btm)
        writer.write_float_value("txyTop", self.txy_top)
        writer.write_float_value("txz", self.txz)
        writer.write_float_value("tyz", self.tyz)
    

