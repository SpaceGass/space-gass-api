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
class PlateGeometry(Parsable):
    """
    Derived geometry of a plate — computed from the stored model, no analysis run required.Corners come in two forms: `nodeCorners` are the analytical corners — the plate'sactual nodes — and `pointCorners` are the physical corners, shifted along the platenormal by the plate offset. They coincide when the plate has no offset. Area and perimeterare invariant to that normal shift, so a single value serves both.
    """
    # Plate surface area.
    area: Optional[float] = None
    # A 3D point with X, Y, Z coordinates.
    centroid: Optional[Point3D] = None
    # A local coordinate system (LCS): an origin plus three local axis unit vectorsexpressed in global coordinates. The axes form a right-handed orthonormal basis —the columns of the element's local-to-global transformation matrix.
    local_axes: Optional[CoordinateSystem] = None
    # The plate's corner nodes in order (A, B, C[, D]) — identity and position. Threeentries for a triangular plate, four for a quadrilateral.
    node_corners: Optional[list[NodeRef]] = None
    # Plate perimeter — the sum of the edge lengths.
    perimeter: Optional[float] = None
    # The plate this geometry belongs to.
    plate: Optional[int] = None
    # Physical (offset-adjusted) corner positions in order (A, B, C[, D]), in globalcoordinates — each corner shifted along the plate normal by the offset.
    point_corners: Optional[list[Point3D]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateGeometry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateGeometry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateGeometry()
    
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
            "area": lambda n : setattr(self, 'area', n.get_float_value()),
            "centroid": lambda n : setattr(self, 'centroid', n.get_object_value(Point3D)),
            "localAxes": lambda n : setattr(self, 'local_axes', n.get_object_value(CoordinateSystem)),
            "nodeCorners": lambda n : setattr(self, 'node_corners', n.get_collection_of_object_values(NodeRef)),
            "perimeter": lambda n : setattr(self, 'perimeter', n.get_float_value()),
            "plate": lambda n : setattr(self, 'plate', n.get_int_value()),
            "pointCorners": lambda n : setattr(self, 'point_corners', n.get_collection_of_object_values(Point3D)),
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
        writer.write_float_value("area", self.area)
        writer.write_object_value("centroid", self.centroid)
        writer.write_object_value("localAxes", self.local_axes)
        writer.write_collection_of_object_values("nodeCorners", self.node_corners)
        writer.write_float_value("perimeter", self.perimeter)
        writer.write_int_value("plate", self.plate)
        writer.write_collection_of_object_values("pointCorners", self.point_corners)
    

