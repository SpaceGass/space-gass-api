from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .point3_d import Point3D

@dataclass
class NodeMatchRequest(Parsable):
    """
    Positions to match against the nodes in the job.
    """
    # The positions to match, in order.
    positions: Optional[list[Point3D]] = None
    # Distance within which a position matches a node: a node matches when it is closer than this.
    tolerance: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NodeMatchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NodeMatchRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NodeMatchRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .point3_d import Point3D

        from .point3_d import Point3D

        fields: dict[str, Callable[[Any], None]] = {
            "positions": lambda n : setattr(self, 'positions', n.get_collection_of_object_values(Point3D)),
            "tolerance": lambda n : setattr(self, 'tolerance', n.get_float_value()),
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
        writer.write_collection_of_object_values("positions", self.positions)
        writer.write_float_value("tolerance", self.tolerance)
    

