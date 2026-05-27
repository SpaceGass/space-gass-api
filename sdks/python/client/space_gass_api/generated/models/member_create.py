from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .direction_update import DirectionUpdate
    from .member_release_update import MemberReleaseUpdate
    from .member_type import MemberType

@dataclass
class MemberCreate(Parsable):
    """
    DTO for creating a new member.NodeA and NodeB are required; all other fields are optional.
    """
    # Cable length (for Cable type members). Unit: Length (see GET /job/units).
    cable_length: Optional[float] = None
    # DTO for updating the direction on a member or plate (partial-update semantics).
    direction: Optional[DirectionUpdate] = None
    # Fuse compression limit (for Fuse type members). Unit: Force (see GET /job/units).
    fuse_compression_limit: Optional[float] = None
    # Fuse tension limit (for Fuse type members). Unit: Force (see GET /job/units).
    fuse_tension_limit: Optional[float] = None
    # Gap compression limit (for Gap type members). Unit: Force (see GET /job/units).
    gap_compression_limit: Optional[float] = None
    # Gap tension limit (for Gap type members). Unit: Force (see GET /job/units).
    gap_tension_limit: Optional[float] = None
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Optional - will be auto-assigned to next available number if not provided.If provided, must not already exist in the model.
    id: Optional[int] = None
    # Material number assigned to this member.
    material: Optional[int] = None
    # Node at end A of the member.
    node_a: Optional[int] = None
    # Node at end B of the member.
    node_b: Optional[int] = None
    # DTO for partial updates to a member release.Only fields included in the request are updated; omit a field to keep its current value.
    releases: Optional[MemberReleaseUpdate] = None
    # Section number assigned to this member.
    section: Optional[int] = None
    # Member element type. Determines the structural behavior of the member.Maps to SPACE GASS lookup table "Member Type".
    type: Optional[MemberType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberCreate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberCreate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberCreate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .direction_update import DirectionUpdate
        from .member_release_update import MemberReleaseUpdate
        from .member_type import MemberType

        from .direction_update import DirectionUpdate
        from .member_release_update import MemberReleaseUpdate
        from .member_type import MemberType

        fields: dict[str, Callable[[Any], None]] = {
            "cableLength": lambda n : setattr(self, 'cable_length', n.get_float_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_object_value(DirectionUpdate)),
            "fuseCompressionLimit": lambda n : setattr(self, 'fuse_compression_limit', n.get_float_value()),
            "fuseTensionLimit": lambda n : setattr(self, 'fuse_tension_limit', n.get_float_value()),
            "gapCompressionLimit": lambda n : setattr(self, 'gap_compression_limit', n.get_float_value()),
            "gapTensionLimit": lambda n : setattr(self, 'gap_tension_limit', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "material": lambda n : setattr(self, 'material', n.get_int_value()),
            "nodeA": lambda n : setattr(self, 'node_a', n.get_int_value()),
            "nodeB": lambda n : setattr(self, 'node_b', n.get_int_value()),
            "releases": lambda n : setattr(self, 'releases', n.get_object_value(MemberReleaseUpdate)),
            "section": lambda n : setattr(self, 'section', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(MemberType)),
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
        writer.write_float_value("cableLength", self.cable_length)
        writer.write_object_value("direction", self.direction)
        writer.write_float_value("fuseCompressionLimit", self.fuse_compression_limit)
        writer.write_float_value("fuseTensionLimit", self.fuse_tension_limit)
        writer.write_float_value("gapCompressionLimit", self.gap_compression_limit)
        writer.write_float_value("gapTensionLimit", self.gap_tension_limit)
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_int_value("material", self.material)
        writer.write_int_value("nodeA", self.node_a)
        writer.write_int_value("nodeB", self.node_b)
        writer.write_object_value("releases", self.releases)
        writer.write_int_value("section", self.section)
        writer.write_enum_value("type", self.type)
    

