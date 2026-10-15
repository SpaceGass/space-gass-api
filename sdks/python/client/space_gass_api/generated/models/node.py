from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .node_constraint import NodeConstraint
    from .node_restraint import NodeRestraint

@dataclass
class Node(Parsable):
    """
    DTO for a single node in the structureOnly includes non-hidden fields from the SPACEGASS node definition
    """
    # DTO for reading a node constraint (master-slave constraint).Defines a kinematic relationship between a slave node and a master node.The slave node's degrees of freedom are tied to the master node according to the constraint code.Top-level entity attribute keyed on the slave node — each node can be a slave in at most one constraint.
    constraint: Optional[NodeConstraint] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # True when this node is the slave side of a master-slave constraint.A node can be the slave of at most one constraint.Use `?expand=all` to include the full `constraint` object.
    has_constraint: Optional[bool] = None
    # True when this node has an explicit restraint row defined.False means the node uses default restraints (all DOFs free, no spring stiffness).
    has_restraint: Optional[bool] = None
    # Primary identifier - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    id: Optional[int] = None
    # DTO for reading a node restraint. Restraints define boundary conditionsat nodes (fixed, released, spring, etc.) using a 6-character restraint code (FRSVPN).Top-level entity attribute keyed on the parent node.
    restraint: Optional[NodeRestraint] = None
    # X coordinate. Unit: Length (see GET /job/units).
    x: Optional[float] = None
    # Y coordinate. Unit: Length (see GET /job/units).
    y: Optional[float] = None
    # Z coordinate. Unit: Length (see GET /job/units).
    z: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Node:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Node
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Node()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .node_constraint import NodeConstraint
        from .node_restraint import NodeRestraint

        from .node_constraint import NodeConstraint
        from .node_restraint import NodeRestraint

        fields: dict[str, Callable[[Any], None]] = {
            "constraint": lambda n : setattr(self, 'constraint', n.get_object_value(NodeConstraint)),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "hasConstraint": lambda n : setattr(self, 'has_constraint', n.get_bool_value()),
            "hasRestraint": lambda n : setattr(self, 'has_restraint', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "restraint": lambda n : setattr(self, 'restraint', n.get_object_value(NodeRestraint)),
            "x": lambda n : setattr(self, 'x', n.get_float_value()),
            "y": lambda n : setattr(self, 'y', n.get_float_value()),
            "z": lambda n : setattr(self, 'z', n.get_float_value()),
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
        writer.write_object_value("constraint", self.constraint)
        writer.write_str_value("guid", self.guid)
        writer.write_bool_value("hasConstraint", self.has_constraint)
        writer.write_bool_value("hasRestraint", self.has_restraint)
        writer.write_int_value("id", self.id)
        writer.write_object_value("restraint", self.restraint)
        writer.write_float_value("x", self.x)
        writer.write_float_value("y", self.y)
        writer.write_float_value("z", self.z)
    

