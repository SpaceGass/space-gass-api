from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lumped_mass_load_key import LumpedMassLoadKey
    from .member_concentrated_load_key import MemberConcentratedLoadKey
    from .member_distributed_load_key import MemberDistributedLoadKey
    from .member_distributed_moment_key import MemberDistributedMomentKey
    from .member_prestress_load_key import MemberPrestressLoadKey
    from .node_load_key import NodeLoadKey
    from .plate_pressure_load_key import PlatePressureLoadKey
    from .prescribed_displacement_key import PrescribedDisplacementKey
    from .thermal_load_element_id import ThermalLoadElementId

@dataclass
class DeleteResult(Parsable):
    """
    Summary of a cascade delete: everything removed when a Node, Member, or Plate was deleted —the entity itself plus every child row that referenced it and any nodes transitively orphanedby the removal. Only entity types that actually had rows removed are present; the rest are omitted.
    """
    # Composite keys (case + node) of lumped mass loads removed.
    lumped_mass_loads: Optional[list[LumpedMassLoadKey]] = None
    # Composite keys (case + member + subLoad) of member concentrated loads removed.
    member_concentrated_loads: Optional[list[MemberConcentratedLoadKey]] = None
    # Composite keys (case + member + subLoad) of member distributed loads removed.
    member_distributed_loads: Optional[list[MemberDistributedLoadKey]] = None
    # Composite keys (case + member + subLoad) of member distributed moments removed.
    member_distributed_moments: Optional[list[MemberDistributedMomentKey]] = None
    # Member Ids whose offset row was removed.
    member_offsets: Optional[list[int]] = None
    # Composite keys (case + member) of member prestress loads removed.
    member_prestress_loads: Optional[list[MemberPrestressLoadKey]] = None
    # Ids of members removed because one of their end nodes was deleted.
    members: Optional[list[int]] = None
    # Ids of surviving members whose direction reference pointed at a deleted node and wastherefore reverted to the default orientation (angle 0). These members were not removed.
    members_direction_reset: Optional[list[int]] = None
    # Slave-node Ids of constraint rows removed (a constraint is dropped if either its slave or master node is deleted).
    node_constraints: Optional[list[int]] = None
    # Composite keys (case + node) of node loads removed.
    node_loads: Optional[list[NodeLoadKey]] = None
    # Node Ids whose restraint row was removed.
    node_restraints: Optional[list[int]] = None
    # Ids of nodes removed (the requested node(s) plus any orphaned by member/plate removal).
    nodes: Optional[list[int]] = None
    # Ids of plate cuts removed (a cut references two plates and two nodes).
    plate_cuts: Optional[list[int]] = None
    # Composite keys (case + plate) of plate pressure loads removed.
    plate_pressure_loads: Optional[list[PlatePressureLoadKey]] = None
    # Ids of plate strips removed (a strip references two plates and two nodes).
    plate_strips: Optional[list[int]] = None
    # Ids of plates removed because one of their corner nodes was deleted.
    plates: Optional[list[int]] = None
    # Ids of surviving plates whose direction reference pointed at a deleted node and wastherefore reverted to the default orientation (angle 0). These plates were not removed.
    plates_direction_reset: Optional[list[int]] = None
    # Composite keys (case + node) of prescribed displacements removed.
    prescribed_displacements: Optional[list[PrescribedDisplacementKey]] = None
    # Composite keys (case + element + elementType) of thermal loads removed.
    thermal_loads: Optional[list[ThermalLoadElementId]] = None
    # Total number of rows removed across all entity types.
    total_removed: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeleteResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeleteResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeleteResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lumped_mass_load_key import LumpedMassLoadKey
        from .member_concentrated_load_key import MemberConcentratedLoadKey
        from .member_distributed_load_key import MemberDistributedLoadKey
        from .member_distributed_moment_key import MemberDistributedMomentKey
        from .member_prestress_load_key import MemberPrestressLoadKey
        from .node_load_key import NodeLoadKey
        from .plate_pressure_load_key import PlatePressureLoadKey
        from .prescribed_displacement_key import PrescribedDisplacementKey
        from .thermal_load_element_id import ThermalLoadElementId

        from .lumped_mass_load_key import LumpedMassLoadKey
        from .member_concentrated_load_key import MemberConcentratedLoadKey
        from .member_distributed_load_key import MemberDistributedLoadKey
        from .member_distributed_moment_key import MemberDistributedMomentKey
        from .member_prestress_load_key import MemberPrestressLoadKey
        from .node_load_key import NodeLoadKey
        from .plate_pressure_load_key import PlatePressureLoadKey
        from .prescribed_displacement_key import PrescribedDisplacementKey
        from .thermal_load_element_id import ThermalLoadElementId

        fields: dict[str, Callable[[Any], None]] = {
            "lumpedMassLoads": lambda n : setattr(self, 'lumped_mass_loads', n.get_collection_of_object_values(LumpedMassLoadKey)),
            "memberConcentratedLoads": lambda n : setattr(self, 'member_concentrated_loads', n.get_collection_of_object_values(MemberConcentratedLoadKey)),
            "memberDistributedLoads": lambda n : setattr(self, 'member_distributed_loads', n.get_collection_of_object_values(MemberDistributedLoadKey)),
            "memberDistributedMoments": lambda n : setattr(self, 'member_distributed_moments', n.get_collection_of_object_values(MemberDistributedMomentKey)),
            "memberOffsets": lambda n : setattr(self, 'member_offsets', n.get_collection_of_primitive_values(int)),
            "memberPrestressLoads": lambda n : setattr(self, 'member_prestress_loads', n.get_collection_of_object_values(MemberPrestressLoadKey)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_primitive_values(int)),
            "membersDirectionReset": lambda n : setattr(self, 'members_direction_reset', n.get_collection_of_primitive_values(int)),
            "nodeConstraints": lambda n : setattr(self, 'node_constraints', n.get_collection_of_primitive_values(int)),
            "nodeLoads": lambda n : setattr(self, 'node_loads', n.get_collection_of_object_values(NodeLoadKey)),
            "nodeRestraints": lambda n : setattr(self, 'node_restraints', n.get_collection_of_primitive_values(int)),
            "nodes": lambda n : setattr(self, 'nodes', n.get_collection_of_primitive_values(int)),
            "plateCuts": lambda n : setattr(self, 'plate_cuts', n.get_collection_of_primitive_values(int)),
            "platePressureLoads": lambda n : setattr(self, 'plate_pressure_loads', n.get_collection_of_object_values(PlatePressureLoadKey)),
            "plateStrips": lambda n : setattr(self, 'plate_strips', n.get_collection_of_primitive_values(int)),
            "plates": lambda n : setattr(self, 'plates', n.get_collection_of_primitive_values(int)),
            "platesDirectionReset": lambda n : setattr(self, 'plates_direction_reset', n.get_collection_of_primitive_values(int)),
            "prescribedDisplacements": lambda n : setattr(self, 'prescribed_displacements', n.get_collection_of_object_values(PrescribedDisplacementKey)),
            "thermalLoads": lambda n : setattr(self, 'thermal_loads', n.get_collection_of_object_values(ThermalLoadElementId)),
            "totalRemoved": lambda n : setattr(self, 'total_removed', n.get_int_value()),
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
        writer.write_collection_of_object_values("lumpedMassLoads", self.lumped_mass_loads)
        writer.write_collection_of_object_values("memberConcentratedLoads", self.member_concentrated_loads)
        writer.write_collection_of_object_values("memberDistributedLoads", self.member_distributed_loads)
        writer.write_collection_of_object_values("memberDistributedMoments", self.member_distributed_moments)
        writer.write_collection_of_primitive_values("memberOffsets", self.member_offsets)
        writer.write_collection_of_object_values("memberPrestressLoads", self.member_prestress_loads)
        writer.write_collection_of_primitive_values("members", self.members)
        writer.write_collection_of_primitive_values("membersDirectionReset", self.members_direction_reset)
        writer.write_collection_of_primitive_values("nodeConstraints", self.node_constraints)
        writer.write_collection_of_object_values("nodeLoads", self.node_loads)
        writer.write_collection_of_primitive_values("nodeRestraints", self.node_restraints)
        writer.write_collection_of_primitive_values("nodes", self.nodes)
        writer.write_collection_of_primitive_values("plateCuts", self.plate_cuts)
        writer.write_collection_of_object_values("platePressureLoads", self.plate_pressure_loads)
        writer.write_collection_of_primitive_values("plateStrips", self.plate_strips)
        writer.write_collection_of_primitive_values("plates", self.plates)
        writer.write_collection_of_primitive_values("platesDirectionReset", self.plates_direction_reset)
        writer.write_collection_of_object_values("prescribedDisplacements", self.prescribed_displacements)
        writer.write_collection_of_object_values("thermalLoads", self.thermal_loads)
        writer.write_int_value("totalRemoved", self.total_removed)
    

