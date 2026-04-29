from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .direction_axis import DirectionAxis
    from .member_offset import MemberOffset
    from .member_release import MemberRelease
    from .member_type import MemberType

@dataclass
class Member(Parsable):
    """
    DTO for reading a member entity.Releases (fixity/stiffness at each end) are intrinsic member data and are always populated.Offsets (rigid end zones) are a linked sub-resource and are hydrated only when `?expand=all`.
    """
    # Cable length (for Cable type members). Unit: Length (see GET /job/units).
    cable_length: Optional[float] = None
    # Direction angle for member orientation.
    dir_angle: Optional[float] = None
    # Direction axis for member orientation.Maps to SPACE GASS lookup table "Direction Axis".
    dir_axis: Optional[DirectionAxis] = None
    # Direction node for member orientation.
    dir_node: Optional[int] = None
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
    # True when this member has an explicit offsets row defined (rigid end zones at A/B).False means the member has no offsets (end rigid zones zero).Use `?expand=all` to include the full `offsets` object.
    has_offsets: Optional[bool] = None
    # Primary identifier - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    id: Optional[int] = None
    # Material number assigned to this member.
    material: Optional[int] = None
    # Node at end A of the member.
    node_a: Optional[int] = None
    # Node at end B of the member.
    node_b: Optional[int] = None
    # DTO for reading member offset data.Offsets define rigid end zones at each end of a member.This is a sub-resource of Member, not a standalone entity.
    offsets: Optional[MemberOffset] = None
    # DTO for reading member release data.Releases define fixity codes and spring stiffness at each end of a member.Always present on every member, so the owning member Idis not duplicated here — the parent MemberDto's `id` is authoritative whenreturned inline, and the route parameter is authoritative on the standalone endpoint.
    releases: Optional[MemberRelease] = None
    # Section number assigned to this member.
    section: Optional[int] = None
    # Member element type. Determines the structural behavior of the member.Maps to SPACE GASS lookup table "Member Type".
    type: Optional[MemberType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Member:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Member
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Member()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .direction_axis import DirectionAxis
        from .member_offset import MemberOffset
        from .member_release import MemberRelease
        from .member_type import MemberType

        from .direction_axis import DirectionAxis
        from .member_offset import MemberOffset
        from .member_release import MemberRelease
        from .member_type import MemberType

        fields: dict[str, Callable[[Any], None]] = {
            "cableLength": lambda n : setattr(self, 'cable_length', n.get_float_value()),
            "dirAngle": lambda n : setattr(self, 'dir_angle', n.get_float_value()),
            "dirAxis": lambda n : setattr(self, 'dir_axis', n.get_enum_value(DirectionAxis)),
            "dirNode": lambda n : setattr(self, 'dir_node', n.get_int_value()),
            "fuseCompressionLimit": lambda n : setattr(self, 'fuse_compression_limit', n.get_float_value()),
            "fuseTensionLimit": lambda n : setattr(self, 'fuse_tension_limit', n.get_float_value()),
            "gapCompressionLimit": lambda n : setattr(self, 'gap_compression_limit', n.get_float_value()),
            "gapTensionLimit": lambda n : setattr(self, 'gap_tension_limit', n.get_float_value()),
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "hasOffsets": lambda n : setattr(self, 'has_offsets', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "material": lambda n : setattr(self, 'material', n.get_int_value()),
            "nodeA": lambda n : setattr(self, 'node_a', n.get_int_value()),
            "nodeB": lambda n : setattr(self, 'node_b', n.get_int_value()),
            "offsets": lambda n : setattr(self, 'offsets', n.get_object_value(MemberOffset)),
            "releases": lambda n : setattr(self, 'releases', n.get_object_value(MemberRelease)),
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
        writer.write_float_value("dirAngle", self.dir_angle)
        writer.write_enum_value("dirAxis", self.dir_axis)
        writer.write_int_value("dirNode", self.dir_node)
        writer.write_float_value("fuseCompressionLimit", self.fuse_compression_limit)
        writer.write_float_value("fuseTensionLimit", self.fuse_tension_limit)
        writer.write_float_value("gapCompressionLimit", self.gap_compression_limit)
        writer.write_float_value("gapTensionLimit", self.gap_tension_limit)
        writer.write_str_value("guid", self.guid)
        writer.write_bool_value("hasOffsets", self.has_offsets)
        writer.write_int_value("id", self.id)
        writer.write_int_value("material", self.material)
        writer.write_int_value("nodeA", self.node_a)
        writer.write_int_value("nodeB", self.node_b)
        writer.write_object_value("offsets", self.offsets)
        writer.write_object_value("releases", self.releases)
        writer.write_int_value("section", self.section)
        writer.write_enum_value("type", self.type)
    

