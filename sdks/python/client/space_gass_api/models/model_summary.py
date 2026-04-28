from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ModelSummary(Parsable):
    """
    Summary counts of all model entities in the current job.
    """
    # Number of combination load cases.
    combination_load_cases: Optional[int] = None
    # Number of multi-point constraint definitions.
    constraints: Optional[int] = None
    # Number of load case groups.
    load_case_groups: Optional[int] = None
    # Number of primary load cases defined.
    load_cases: Optional[int] = None
    # Number of load categories (e.g. dead, live, wind).
    load_categories: Optional[int] = None
    # Number of lumped mass definitions for dynamic analysis.
    lumped_mass_loads: Optional[int] = None
    # Number of materials defined.
    materials: Optional[int] = None
    # Number of concentrated (point) loads applied to members.
    member_concentrated_loads: Optional[int] = None
    # Number of distributed (UDL/trapezoidal) loads applied to members.
    member_distributed_loads: Optional[int] = None
    # Number of members with rigid end offsets.
    member_offsets: Optional[int] = None
    # Number of prestress loads applied to members.
    member_prestress_loads: Optional[int] = None
    # Number of torsion loads applied to members.
    member_torsion_loads: Optional[int] = None
    # Number of members (beam/column elements) in the structure.
    members: Optional[int] = None
    # Number of point loads applied to nodes.
    node_loads: Optional[int] = None
    # Number of nodes with support restraint conditions.
    node_restraints: Optional[int] = None
    # Number of nodes (joints/points) in the structure.
    nodes: Optional[int] = None
    # Number of pressure/distributed loads applied to plates.
    plate_loads: Optional[int] = None
    # Number of plate/shell elements in the structure.
    plates: Optional[int] = None
    # Number of prescribed displacement constraints.
    prescribed_displacements: Optional[int] = None
    # Number of cross-section profiles defined.
    sections: Optional[int] = None
    # Number of self-weight load definitions.
    self_weight_loads: Optional[int] = None
    # Number of thermal (temperature) load definitions.
    thermal_loads: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "combinationLoadCases": lambda n : setattr(self, 'combination_load_cases', n.get_int_value()),
            "constraints": lambda n : setattr(self, 'constraints', n.get_int_value()),
            "loadCaseGroups": lambda n : setattr(self, 'load_case_groups', n.get_int_value()),
            "loadCases": lambda n : setattr(self, 'load_cases', n.get_int_value()),
            "loadCategories": lambda n : setattr(self, 'load_categories', n.get_int_value()),
            "lumpedMassLoads": lambda n : setattr(self, 'lumped_mass_loads', n.get_int_value()),
            "materials": lambda n : setattr(self, 'materials', n.get_int_value()),
            "memberConcentratedLoads": lambda n : setattr(self, 'member_concentrated_loads', n.get_int_value()),
            "memberDistributedLoads": lambda n : setattr(self, 'member_distributed_loads', n.get_int_value()),
            "memberOffsets": lambda n : setattr(self, 'member_offsets', n.get_int_value()),
            "memberPrestressLoads": lambda n : setattr(self, 'member_prestress_loads', n.get_int_value()),
            "memberTorsionLoads": lambda n : setattr(self, 'member_torsion_loads', n.get_int_value()),
            "members": lambda n : setattr(self, 'members', n.get_int_value()),
            "nodeLoads": lambda n : setattr(self, 'node_loads', n.get_int_value()),
            "nodeRestraints": lambda n : setattr(self, 'node_restraints', n.get_int_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_int_value()),
            "plateLoads": lambda n : setattr(self, 'plate_loads', n.get_int_value()),
            "plates": lambda n : setattr(self, 'plates', n.get_int_value()),
            "prescribedDisplacements": lambda n : setattr(self, 'prescribed_displacements', n.get_int_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_int_value()),
            "selfWeightLoads": lambda n : setattr(self, 'self_weight_loads', n.get_int_value()),
            "thermalLoads": lambda n : setattr(self, 'thermal_loads', n.get_int_value()),
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
        writer.write_int_value("combinationLoadCases", self.combination_load_cases)
        writer.write_int_value("constraints", self.constraints)
        writer.write_int_value("loadCaseGroups", self.load_case_groups)
        writer.write_int_value("loadCases", self.load_cases)
        writer.write_int_value("loadCategories", self.load_categories)
        writer.write_int_value("lumpedMassLoads", self.lumped_mass_loads)
        writer.write_int_value("materials", self.materials)
        writer.write_int_value("memberConcentratedLoads", self.member_concentrated_loads)
        writer.write_int_value("memberDistributedLoads", self.member_distributed_loads)
        writer.write_int_value("memberOffsets", self.member_offsets)
        writer.write_int_value("memberPrestressLoads", self.member_prestress_loads)
        writer.write_int_value("memberTorsionLoads", self.member_torsion_loads)
        writer.write_int_value("members", self.members)
        writer.write_int_value("nodeLoads", self.node_loads)
        writer.write_int_value("nodeRestraints", self.node_restraints)
        writer.write_int_value("nodes", self.nodes)
        writer.write_int_value("plateLoads", self.plate_loads)
        writer.write_int_value("plates", self.plates)
        writer.write_int_value("prescribedDisplacements", self.prescribed_displacements)
        writer.write_int_value("sections", self.sections)
        writer.write_int_value("selfWeightLoads", self.self_weight_loads)
        writer.write_int_value("thermalLoads", self.thermal_loads)
    

