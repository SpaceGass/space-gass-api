from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .coordinate_system import CoordinateSystem
    from .node_ref import NodeRef
    from .point3_d import Point3D

@dataclass
class MemberGeometry(Parsable):
    """
    Derived geometry of a member — computed from the stored model, no analysis run required.The end positions come in two forms: `nodeA`/`nodeB` are the analytical (node-line)ends — the member's actual nodes — and `pointA`/`pointB` are the physical(offset-adjusted) ends as free points in space. They coincide when the member has no offsets.
    """
    # Physical (offset-adjusted) member length — the distance between `pointA` and`pointB`. The analytical node-line length is the distance between `nodeA`and `nodeB`.
    length: Optional[float] = None
    # A local coordinate system (LCS): an origin plus three local axis unit vectorsexpressed in global coordinates. The axes form a right-handed orthonormal basis —the columns of the element's local-to-global transformation matrix.
    local_axes: Optional[CoordinateSystem] = None
    # The member this geometry belongs to.
    member: Optional[int] = None
    # A lean reference to a node — its Id and coordinates only. Used to embed a node's identityand position in derived-geometry responses without dragging in the node's sub-resourceindicators (restraints/constraints). The `id` matches the node's Id in`GET /job/structure/nodes`.
    node_a: Optional[NodeRef] = None
    # A lean reference to a node — its Id and coordinates only. Used to embed a node's identityand position in derived-geometry responses without dragging in the node's sub-resourceindicators (restraints/constraints). The `id` matches the node's Id in`GET /job/structure/nodes`.
    node_b: Optional[NodeRef] = None
    # A 3D point with X, Y, Z coordinates.
    point_a: Optional[Point3D] = None
    # A 3D point with X, Y, Z coordinates.
    point_b: Optional[Point3D] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberGeometry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberGeometry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberGeometry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .coordinate_system import CoordinateSystem
        from .node_ref import NodeRef
        from .point3_d import Point3D

        from .coordinate_system import CoordinateSystem
        from .node_ref import NodeRef
        from .point3_d import Point3D

        fields: dict[str, Callable[[Any], None]] = {
            "length": lambda n : setattr(self, 'length', n.get_float_value()),
            "localAxes": lambda n : setattr(self, 'local_axes', n.get_object_value(CoordinateSystem)),
            "member": lambda n : setattr(self, 'member', n.get_int_value()),
            "nodeA": lambda n : setattr(self, 'node_a', n.get_object_value(NodeRef)),
            "nodeB": lambda n : setattr(self, 'node_b', n.get_object_value(NodeRef)),
            "pointA": lambda n : setattr(self, 'point_a', n.get_object_value(Point3D)),
            "pointB": lambda n : setattr(self, 'point_b', n.get_object_value(Point3D)),
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
        writer.write_object_value("localAxes", self.local_axes)
        writer.write_int_value("member", self.member)
        writer.write_object_value("nodeA", self.node_a)
        writer.write_object_value("nodeB", self.node_b)
        writer.write_object_value("pointA", self.point_a)
        writer.write_object_value("pointB", self.point_b)
    

