from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NodeLoad(Parsable):
    """
    DTO for reading a node load entity.Represents concentrated forces and moments applied at a node.
    """
    # The load case number this load belongs to.
    case: Optional[int] = None
    # Force in the global X direction.
    fx: Optional[float] = None
    # Force in the global Y direction.
    fy: Optional[float] = None
    # Force in the global Z direction.
    fz: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Load category for grouping/organization.
    load_category: Optional[int] = None
    # Moment about the global X axis.
    mx: Optional[float] = None
    # Moment about the global Y axis.
    my: Optional[float] = None
    # Moment about the global Z axis.
    mz: Optional[float] = None
    # The node number this load is applied to.
    node: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeLoad:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeLoad
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeLoad()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "case": lambda n : setattr(self, 'case', n.get_int_value()),
            "fx": lambda n : setattr(self, 'fx', n.get_float_value()),
            "fy": lambda n : setattr(self, 'fy', n.get_float_value()),
            "fz": lambda n : setattr(self, 'fz', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "loadCategory": lambda n : setattr(self, 'load_category', n.get_int_value()),
            "mx": lambda n : setattr(self, 'mx', n.get_float_value()),
            "my": lambda n : setattr(self, 'my', n.get_float_value()),
            "mz": lambda n : setattr(self, 'mz', n.get_float_value()),
            "node": lambda n : setattr(self, 'node', n.get_int_value()),
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
        writer.write_float_value("fx", self.fx)
        writer.write_float_value("fy", self.fy)
        writer.write_float_value("fz", self.fz)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("loadCategory", self.load_category)
        writer.write_float_value("mx", self.mx)
        writer.write_float_value("my", self.my)
        writer.write_float_value("mz", self.mz)
        writer.write_int_value("node", self.node)
    

