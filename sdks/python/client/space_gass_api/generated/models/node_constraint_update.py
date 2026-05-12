from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .constraint_axes import ConstraintAxes

@dataclass
class NodeConstraintUpdate(Parsable):
    """
    DTO for partially updating an existing node constraint.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # Coordinate axis system used for master-slave constraint equations.Maps to SPACE GASS lookup table "Constraint Axes".
    axes: Optional[ConstraintAxes] = None
    # A 6-character string defining which degrees of freedom are constrained.Each character position maps to a DOF: UX, UY, UZ, RX, RY, RZ (left to right).'F' = Fixed (tied to master), 'R' = Released (free).
    constraint_code: Optional[str] = None
    # Optional GUID for this constraint record.
    guid: Optional[str] = None
    # The master node number.
    master_node: Optional[int] = None
    # The slave node number that identifies which constraint to update.Required for bulk PATCH; ignored for single-node PATCH (route value wins).
    slave_node: Optional[int] = None
    # X component of the constraint axis direction vector.
    x_vector: Optional[float] = None
    # Y component of the constraint axis direction vector.
    y_vector: Optional[float] = None
    # Z component of the constraint axis direction vector.
    z_vector: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeConstraintUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeConstraintUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeConstraintUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .constraint_axes import ConstraintAxes

        from .constraint_axes import ConstraintAxes

        fields: dict[str, Callable[[Any], None]] = {
            "axes": lambda n : setattr(self, 'axes', n.get_enum_value(ConstraintAxes)),
            "constraintCode": lambda n : setattr(self, 'constraint_code', n.get_str_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "masterNode": lambda n : setattr(self, 'master_node', n.get_int_value()),
            "slaveNode": lambda n : setattr(self, 'slave_node', n.get_int_value()),
            "xVector": lambda n : setattr(self, 'x_vector', n.get_float_value()),
            "yVector": lambda n : setattr(self, 'y_vector', n.get_float_value()),
            "zVector": lambda n : setattr(self, 'z_vector', n.get_float_value()),
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
        writer.write_enum_value("axes", self.axes)
        writer.write_str_value("constraintCode", self.constraint_code)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("masterNode", self.master_node)
        writer.write_int_value("slaveNode", self.slave_node)
        writer.write_float_value("xVector", self.x_vector)
        writer.write_float_value("yVector", self.y_vector)
        writer.write_float_value("zVector", self.z_vector)
    

