from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PlateNodalForce(Parsable):
    """
    Plate nodal force results grouped by load case and plate.Columnar arrays hold force values at each node of the plate element.
    """
    # Load case ID.
    case: Optional[int] = None
    # Force in X at each node. Unit: Force (see GET /job/units).
    fx: Optional[list[float]] = None
    # Force in Y at each node. Unit: Force (see GET /job/units).
    fy: Optional[list[float]] = None
    # Force in Z at each node. Unit: Force (see GET /job/units).
    fz: Optional[list[float]] = None
    # Moment about X at each node. Unit: Moment (see GET /job/units).
    mx: Optional[list[float]] = None
    # Moment about Y at each node. Unit: Moment (see GET /job/units).
    my: Optional[list[float]] = None
    # Moment about Z at each node. Unit: Moment (see GET /job/units).
    mz: Optional[list[float]] = None
    # Node keys at each corner of the plate element.
    node: Optional[list[int]] = None
    # Plate key.
    plate: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateNodalForce:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateNodalForce
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateNodalForce()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "fx": lambda n : setattr(self, 'fx', n.get_collection_of_primitive_values(float)),
            "fy": lambda n : setattr(self, 'fy', n.get_collection_of_primitive_values(float)),
            "fz": lambda n : setattr(self, 'fz', n.get_collection_of_primitive_values(float)),
            "mx": lambda n : setattr(self, 'mx', n.get_collection_of_primitive_values(float)),
            "my": lambda n : setattr(self, 'my', n.get_collection_of_primitive_values(float)),
            "mz": lambda n : setattr(self, 'mz', n.get_collection_of_primitive_values(float)),
            "node": lambda n : setattr(self, 'node', n.get_collection_of_primitive_values(int)),
            "plate": lambda n : setattr(self, 'plate', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("fx", self.fx)
        writer.write_collection_of_primitive_values("fy", self.fy)
        writer.write_collection_of_primitive_values("fz", self.fz)
        writer.write_collection_of_primitive_values("mx", self.mx)
        writer.write_collection_of_primitive_values("my", self.my)
        writer.write_collection_of_primitive_values("mz", self.mz)
        writer.write_collection_of_primitive_values("node", self.node)
        writer.write_int_value("plate", self.plate)
    

