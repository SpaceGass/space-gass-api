from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PrescribedDisplacementCreate(Parsable):
    """
    DTO for creating a new prescribed displacement.
    """
    # The load case number to create this load in.
    case: Optional[int] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # The node number to apply this displacement to.
    node: Optional[int] = None
    # Prescribed rotation about the global X axis.
    rx: Optional[float] = None
    # Prescribed rotation about the global Y axis.
    ry: Optional[float] = None
    # Prescribed rotation about the global Z axis.
    rz: Optional[float] = None
    # Prescribed translation in the global X direction.
    tx: Optional[float] = None
    # Prescribed translation in the global Y direction.
    ty: Optional[float] = None
    # Prescribed translation in the global Z direction.
    tz: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrescribedDisplacementCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrescribedDisplacementCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrescribedDisplacementCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
            "rx": lambda n : setattr(self, 'rx', n.get_float_value()),
            "ry": lambda n : setattr(self, 'ry', n.get_float_value()),
            "rz": lambda n : setattr(self, 'rz', n.get_float_value()),
            "tx": lambda n : setattr(self, 'tx', n.get_float_value()),
            "ty": lambda n : setattr(self, 'ty', n.get_float_value()),
            "tz": lambda n : setattr(self, 'tz', n.get_float_value()),
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
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_int_value("node", self.node)
        writer.write_float_value("rx", self.rx)
        writer.write_float_value("ry", self.ry)
        writer.write_float_value("rz", self.rz)
        writer.write_float_value("tx", self.tx)
        writer.write_float_value("ty", self.ty)
        writer.write_float_value("tz", self.tz)
    

