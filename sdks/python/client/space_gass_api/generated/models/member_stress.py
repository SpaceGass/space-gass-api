from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class MemberStress(Parsable):
    """
    Member stress results grouped by load case and member.Columnar arrays hold stress values at each station along the member.
    """
    # Load case ID.
    case: Optional[int] = None
    # Member key.
    member: Optional[int] = None
    # Torsion stress at each station. Unit: Stress (see GET /job/units).
    mx: Optional[list[float]] = None
    # Bending stress about Y (bottom fibre) at each station. Unit: Stress (see GET /job/units).
    my_btm: Optional[list[float]] = None
    # Bending stress about Y (top fibre) at each station. Unit: Stress (see GET /job/units).
    my_top: Optional[list[float]] = None
    # Bending stress about Z (bottom fibre) at each station. Unit: Stress (see GET /job/units).
    mz_btm: Optional[list[float]] = None
    # Bending stress about Z (top fibre) at each station. Unit: Stress (see GET /job/units).
    mz_top: Optional[list[float]] = None
    # Axial stress at each station. Unit: Stress (see GET /job/units).
    n: Optional[list[float]] = None
    # Combined axial + My stress (bottom fibre) at each station. Unit: Stress (see GET /job/units).
    n_my_btm: Optional[list[float]] = None
    # Combined axial + My stress (top fibre) at each station. Unit: Stress (see GET /job/units).
    n_my_top: Optional[list[float]] = None
    # Combined axial + Mz stress (bottom fibre) at each station. Unit: Stress (see GET /job/units).
    n_mz_btm: Optional[list[float]] = None
    # Combined axial + Mz stress (top fibre) at each station. Unit: Stress (see GET /job/units).
    n_mz_top: Optional[list[float]] = None
    # Fractional position along member (0.0 to 1.0).
    position: Optional[list[float]] = None
    # Station index at each output point.
    station: Optional[list[int]] = None
    # Shear stress in Y at each station. Unit: Stress (see GET /job/units).
    vy: Optional[list[float]] = None
    # Shear stress in Z at each station. Unit: Stress (see GET /job/units).
    vz: Optional[list[float]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberStress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberStress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberStress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_collection_of_primitive_values(float)),
            "myBtm": lambda n : setattr(self, 'my_btm', n.get_collection_of_primitive_values(float)),
            "myTop": lambda n : setattr(self, 'my_top', n.get_collection_of_primitive_values(float)),
            "mzBtm": lambda n : setattr(self, 'mz_btm', n.get_collection_of_primitive_values(float)),
            "mzTop": lambda n : setattr(self, 'mz_top', n.get_collection_of_primitive_values(float)),
            "n": lambda n : setattr(self, 'n', n.get_collection_of_primitive_values(float)),
            "nMyBtm": lambda n : setattr(self, 'n_my_btm', n.get_collection_of_primitive_values(float)),
            "nMyTop": lambda n : setattr(self, 'n_my_top', n.get_collection_of_primitive_values(float)),
            "nMzBtm": lambda n : setattr(self, 'n_mz_btm', n.get_collection_of_primitive_values(float)),
            "nMzTop": lambda n : setattr(self, 'n_mz_top', n.get_collection_of_primitive_values(float)),
            "position": lambda n : setattr(self, 'position', n.get_collection_of_primitive_values(float)),
            "station": lambda n : setattr(self, 'station', n.get_collection_of_primitive_values(int)),
            "vy": lambda n : setattr(self, 'vy', n.get_collection_of_primitive_values(float)),
            "vz": lambda n : setattr(self, 'vz', n.get_collection_of_primitive_values(float)),
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
        writer.write_int_value("case", self.case)
        writer.write_int_value("member", self.member)
        writer.write_collection_of_primitive_values("mx", self.mx)
        writer.write_collection_of_primitive_values("myBtm", self.my_btm)
        writer.write_collection_of_primitive_values("myTop", self.my_top)
        writer.write_collection_of_primitive_values("mzBtm", self.mz_btm)
        writer.write_collection_of_primitive_values("mzTop", self.mz_top)
        writer.write_collection_of_primitive_values("n", self.n)
        writer.write_collection_of_primitive_values("nMyBtm", self.n_my_btm)
        writer.write_collection_of_primitive_values("nMyTop", self.n_my_top)
        writer.write_collection_of_primitive_values("nMzBtm", self.n_mz_btm)
        writer.write_collection_of_primitive_values("nMzTop", self.n_mz_top)
        writer.write_collection_of_primitive_values("position", self.position)
        writer.write_collection_of_primitive_values("station", self.station)
        writer.write_collection_of_primitive_values("vy", self.vy)
        writer.write_collection_of_primitive_values("vz", self.vz)
    

