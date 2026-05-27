from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StructureSummary(Parsable):
    """
    Summary counts of structural entities in the current job — geometry,boundary conditions, and section/material properties.
    """
    # Number of materials defined.
    materials: Optional[int] = None
    # Number of members with rigid end offsets.
    member_offsets: Optional[int] = None
    # Number of members (beam/column elements) in the structure.
    members: Optional[int] = None
    # Number of master-slave node constraint definitions.
    node_constraints: Optional[int] = None
    # Number of nodes with support restraint conditions.
    node_restraints: Optional[int] = None
    # Number of nodes (joints/points) in the structure.
    nodes: Optional[int] = None
    # Number of plate/shell elements in the structure.
    plates: Optional[int] = None
    # Number of cross-section profiles defined.
    sections: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StructureSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StructureSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StructureSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "materials": lambda n : setattr(self, 'materials', n.get_int_value()),
            "memberOffsets": lambda n : setattr(self, 'member_offsets', n.get_int_value()),
            "members": lambda n : setattr(self, 'members', n.get_int_value()),
            "nodeConstraints": lambda n : setattr(self, 'node_constraints', n.get_int_value()),
            "nodeRestraints": lambda n : setattr(self, 'node_restraints', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_int_value()),
            "plates": lambda n : setattr(self, 'plates', n.get_int_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_int_value()),
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
        writer.write_int_value("materials", self.materials)
        writer.write_int_value("memberOffsets", self.member_offsets)
        writer.write_int_value("members", self.members)
        writer.write_int_value("nodeConstraints", self.node_constraints)
        writer.write_int_value("nodeRestraints", self.node_restraints)
        writer.write_int_value("nodes", self.nodes)
        writer.write_int_value("plates", self.plates)
        writer.write_int_value("sections", self.sections)
    

