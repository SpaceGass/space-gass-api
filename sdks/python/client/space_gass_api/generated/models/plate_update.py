from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .direction_update import DirectionUpdate
    from .plate_theory import PlateTheory

@dataclass
class PlateUpdate(Parsable):
    """
    DTO for updating an existing plate.Only fields included in the request are updated; omit a field to keep its current value.
    """
    # Actual thickness of the plate. Unit: Section Properties (see GET /job/units).
    actual_thickness: Optional[float] = None
    # Bending thickness of the plate. Unit: Section Properties (see GET /job/units).
    bending_thickness: Optional[float] = None
    # DTO for updating the direction on a member or plate (partial-update semantics).
    direction: Optional[DirectionUpdate] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Material number assigned to this plate.
    material: Optional[int] = None
    # Membrane thickness of the plate. Unit: Section Properties (see GET /job/units).
    membrane_thickness: Optional[float] = None
    # Node at corner A of the plate.
    node_a: Optional[int] = None
    # Node at corner B of the plate.
    node_b: Optional[int] = None
    # Node at corner C of the plate.
    node_c: Optional[int] = None
    # Node at corner D of the plate. Set to 0 for a triangular (3-node) plate.
    node_d: Optional[int] = None
    # Plate offset. Unit: Length (see GET /job/units).
    offset: Optional[float] = None
    # Shear thickness of the plate. Unit: Section Properties (see GET /job/units).
    shear_thickness: Optional[float] = None
    # Plate theory type for finite element analysis.Maps to SPACE GASS lookup table "Plate Theory".
    theory: Optional[PlateTheory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlateUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlateUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlateUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .direction_update import DirectionUpdate
        from .plate_theory import PlateTheory

        from .direction_update import DirectionUpdate
        from .plate_theory import PlateTheory

        fields: dict[str, Callable[[Any], None]] = {
            "actualThickness": lambda n : setattr(self, 'actual_thickness', n.get_float_value()),
            "bendingThickness": lambda n : setattr(self, 'bending_thickness', n.get_float_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_object_value(DirectionUpdate)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "material": lambda n : setattr(self, 'material', n.get_int_value()),
            "membraneThickness": lambda n : setattr(self, 'membrane_thickness', n.get_float_value()),
            "nodeA": lambda n : setattr(self, 'node_a', n.get_int_value()),
            "nodeB": lambda n : setattr(self, 'node_b', n.get_int_value()),
            "nodeC": lambda n : setattr(self, 'node_c', n.get_int_value()),
            "nodeD": lambda n : setattr(self, 'node_d', n.get_int_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_float_value()),
            "shearThickness": lambda n : setattr(self, 'shear_thickness', n.get_float_value()),
            "theory": lambda n : setattr(self, 'theory', n.get_enum_value(PlateTheory)),
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
        writer.write_float_value("actualThickness", self.actual_thickness)
        writer.write_float_value("bendingThickness", self.bending_thickness)
        writer.write_object_value("direction", self.direction)
        writer.write_int_value("id", self.id)
        writer.write_int_value("material", self.material)
        writer.write_float_value("membraneThickness", self.membrane_thickness)
        writer.write_int_value("nodeA", self.node_a)
        writer.write_int_value("nodeB", self.node_b)
        writer.write_int_value("nodeC", self.node_c)
        writer.write_int_value("nodeD", self.node_d)
        writer.write_float_value("offset", self.offset)
        writer.write_float_value("shearThickness", self.shear_thickness)
        writer.write_enum_value("theory", self.theory)
    

