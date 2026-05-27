from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_axis_range_update import FilterAxisRangeUpdate
    from .filter_materials_update import FilterMaterialsUpdate
    from .filter_members_update import FilterMembersUpdate
    from .filter_nodes_update import FilterNodesUpdate
    from .filter_plates_update import FilterPlatesUpdate
    from .filter_plate_cuts_update import FilterPlateCutsUpdate
    from .filter_plate_strips_update import FilterPlateStripsUpdate
    from .filter_plate_thicknesses_update import FilterPlateThicknessesUpdate
    from .filter_sections_update import FilterSectionsUpdate
    from .filter_steel_connections_update import FilterSteelConnectionsUpdate
    from .filter_steel_members_update import FilterSteelMembersUpdate

@dataclass
class FilterUpdate(Parsable):
    """
    DTO for updating an existing filter.All properties are nullable — omitted fields keep their current value.Sub-filters are nullable: `null` means "don't touch thissub-filter at all"; an empty `{}` means "the sub-filter was supplied butno fields changed".
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # Partial update for the Materials sub-filter.
    materials: Optional[FilterMaterialsUpdate] = None
    # Partial update for the Members sub-filter.
    members: Optional[FilterMembersUpdate] = None
    # Filter name. Null to keep the current name.
    name: Optional[str] = None
    # Partial update for the Nodes sub-filter.
    nodes: Optional[FilterNodesUpdate] = None
    # Partial update for the Plate Cuts sub-filter.
    plate_cuts: Optional[FilterPlateCutsUpdate] = None
    # Partial update for the Plate Strips sub-filter.
    plate_strips: Optional[FilterPlateStripsUpdate] = None
    # Partial update for the Plate Thicknesses sub-filter.
    plate_thicknesses: Optional[FilterPlateThicknessesUpdate] = None
    # Partial update for the Plates sub-filter.
    plates: Optional[FilterPlatesUpdate] = None
    # Partial update for the Sections sub-filter.
    sections: Optional[FilterSectionsUpdate] = None
    # Partial update for the Steel Connections sub-filter.
    steel_connections: Optional[FilterSteelConnectionsUpdate] = None
    # Partial update for the Steel Members sub-filter.
    steel_members: Optional[FilterSteelMembersUpdate] = None
    # Partial update for an axis-range sub-filter (X, Y or Z).
    x_axis: Optional[FilterAxisRangeUpdate] = None
    # Partial update for an axis-range sub-filter (X, Y or Z).
    y_axis: Optional[FilterAxisRangeUpdate] = None
    # Partial update for an axis-range sub-filter (X, Y or Z).
    z_axis: Optional[FilterAxisRangeUpdate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_axis_range_update import FilterAxisRangeUpdate
        from .filter_materials_update import FilterMaterialsUpdate
        from .filter_members_update import FilterMembersUpdate
        from .filter_nodes_update import FilterNodesUpdate
        from .filter_plates_update import FilterPlatesUpdate
        from .filter_plate_cuts_update import FilterPlateCutsUpdate
        from .filter_plate_strips_update import FilterPlateStripsUpdate
        from .filter_plate_thicknesses_update import FilterPlateThicknessesUpdate
        from .filter_sections_update import FilterSectionsUpdate
        from .filter_steel_connections_update import FilterSteelConnectionsUpdate
        from .filter_steel_members_update import FilterSteelMembersUpdate

        from .filter_axis_range_update import FilterAxisRangeUpdate
        from .filter_materials_update import FilterMaterialsUpdate
        from .filter_members_update import FilterMembersUpdate
        from .filter_nodes_update import FilterNodesUpdate
        from .filter_plates_update import FilterPlatesUpdate
        from .filter_plate_cuts_update import FilterPlateCutsUpdate
        from .filter_plate_strips_update import FilterPlateStripsUpdate
        from .filter_plate_thicknesses_update import FilterPlateThicknessesUpdate
        from .filter_sections_update import FilterSectionsUpdate
        from .filter_steel_connections_update import FilterSteelConnectionsUpdate
        from .filter_steel_members_update import FilterSteelMembersUpdate

        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "materials": lambda n : setattr(self, 'materials', n.get_object_value(FilterMaterialsUpdate)),
            "members": lambda n : setattr(self, 'members', n.get_object_value(FilterMembersUpdate)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_object_value(FilterNodesUpdate)),
            "plateCuts": lambda n : setattr(self, 'plate_cuts', n.get_object_value(FilterPlateCutsUpdate)),
            "plateStrips": lambda n : setattr(self, 'plate_strips', n.get_object_value(FilterPlateStripsUpdate)),
            "plateThicknesses": lambda n : setattr(self, 'plate_thicknesses', n.get_object_value(FilterPlateThicknessesUpdate)),
            "plates": lambda n : setattr(self, 'plates', n.get_object_value(FilterPlatesUpdate)),
            "sections": lambda n : setattr(self, 'sections', n.get_object_value(FilterSectionsUpdate)),
            "steelConnections": lambda n : setattr(self, 'steel_connections', n.get_object_value(FilterSteelConnectionsUpdate)),
            "steelMembers": lambda n : setattr(self, 'steel_members', n.get_object_value(FilterSteelMembersUpdate)),
            "xAxis": lambda n : setattr(self, 'x_axis', n.get_object_value(FilterAxisRangeUpdate)),
            "yAxis": lambda n : setattr(self, 'y_axis', n.get_object_value(FilterAxisRangeUpdate)),
            "zAxis": lambda n : setattr(self, 'z_axis', n.get_object_value(FilterAxisRangeUpdate)),
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
        writer.write_str_value("guid", self.guid)
        writer.write_int_value("id", self.id)
        writer.write_object_value("materials", self.materials)
        writer.write_object_value("members", self.members)
        writer.write_str_value("name", self.name)
        writer.write_object_value("nodes", self.nodes)
        writer.write_object_value("plateCuts", self.plate_cuts)
        writer.write_object_value("plateStrips", self.plate_strips)
        writer.write_object_value("plateThicknesses", self.plate_thicknesses)
        writer.write_object_value("plates", self.plates)
        writer.write_object_value("sections", self.sections)
        writer.write_object_value("steelConnections", self.steel_connections)
        writer.write_object_value("steelMembers", self.steel_members)
        writer.write_object_value("xAxis", self.x_axis)
        writer.write_object_value("yAxis", self.y_axis)
        writer.write_object_value("zAxis", self.z_axis)
    

