from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_axis_range import FilterAxisRange
    from .filter_materials import FilterMaterials
    from .filter_members import FilterMembers
    from .filter_nodes import FilterNodes
    from .filter_plates import FilterPlates
    from .filter_plate_cuts import FilterPlateCuts
    from .filter_plate_strips import FilterPlateStrips
    from .filter_plate_thicknesses import FilterPlateThicknesses
    from .filter_sections import FilterSections
    from .filter_steel_connections import FilterSteelConnections
    from .filter_steel_members import FilterSteelMembers

@dataclass
class Filter(Parsable):
    """
    DTO for a named filter (from Filter - Properties datasheet, FileID=213).A filter is a composite of 13 sub-filters that are AND-combinedwhen applied. Maximum 200 filters per job.
    """
    # Optional GUID (hidden field in SPACEGASS)Some API users find this handy for tracking entities across systems
    guid: Optional[str] = None
    # Primary identifier - must be unique, no duplicates allowed.Range: 1 to int.MaxValue
    id: Optional[int] = None
    # Sub-filter carrying a list of material Ids. No sub-type.Maps to SG `SGFilterType.Materials`.
    materials: Optional[FilterMaterials] = None
    # Sub-filter carrying a list of member Ids and a member-type categorical filter.Maps to SG `SGFilterType.Members`.
    members: Optional[FilterMembers] = None
    # Filter name (the label shown in the SG UI). Persisted on everysub-filter row in the datasheet — a filter with no active sub-filtershas no datasheet rows and effectively does not exist.
    name: Optional[str] = None
    # Sub-filter carrying a list of node Ids and a node-type categorical filter.Maps to SG `SGFilterType.Nodes`.
    nodes: Optional[FilterNodes] = None
    # Sub-filter carrying a list of plate-cut Ids and a cut-typecategorical filter.Maps to SG `SGFilterType.PlateCut`.
    plate_cuts: Optional[FilterPlateCuts] = None
    # Sub-filter carrying a list of plate-strip Ids and a strip-typecategorical filter.Maps to SG `SGFilterType.PlateStrip`.
    plate_strips: Optional[FilterPlateStrips] = None
    # Sub-filter carrying a list of plate-thickness values (not Ids).Maps to SG `SGFilterType.Thicknesses`.
    plate_thicknesses: Optional[FilterPlateThicknesses] = None
    # Sub-filter carrying a list of plate Ids and a plate-type categorical filter.Maps to SG `SGFilterType.Plates`.
    plates: Optional[FilterPlates] = None
    # Sub-filter carrying a list of section Ids. No sub-type — sectionsare filtered by Id alone.Maps to SG `SGFilterType.Sections`.
    sections: Optional[FilterSections] = None
    # Sub-filter carrying a list of steel-connection Ids. No sub-type(the SG-side enum slot is unused; `UpdateFromDatasheetItem` neverreads it back).Maps to SG `SGFilterType.SteelConnections`.
    steel_connections: Optional[FilterSteelConnections] = None
    # Sub-filter carrying a list of steel-member Ids and a design-statecategorical filter.Maps to SG `SGFilterType.SteelMembers`.
    steel_members: Optional[FilterSteelMembers] = None
    # Sub-filter carrying a coordinate-range criterion (one axis).Maps to SG `SGFilterType.XAxis` / `YAxis` / `ZAxis` — three siblingproperties at the parent level use this shape.
    x_axis: Optional[FilterAxisRange] = None
    # Sub-filter carrying a coordinate-range criterion (one axis).Maps to SG `SGFilterType.XAxis` / `YAxis` / `ZAxis` — three siblingproperties at the parent level use this shape.
    y_axis: Optional[FilterAxisRange] = None
    # Sub-filter carrying a coordinate-range criterion (one axis).Maps to SG `SGFilterType.XAxis` / `YAxis` / `ZAxis` — three siblingproperties at the parent level use this shape.
    z_axis: Optional[FilterAxisRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Filter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Filter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Filter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_axis_range import FilterAxisRange
        from .filter_materials import FilterMaterials
        from .filter_members import FilterMembers
        from .filter_nodes import FilterNodes
        from .filter_plates import FilterPlates
        from .filter_plate_cuts import FilterPlateCuts
        from .filter_plate_strips import FilterPlateStrips
        from .filter_plate_thicknesses import FilterPlateThicknesses
        from .filter_sections import FilterSections
        from .filter_steel_connections import FilterSteelConnections
        from .filter_steel_members import FilterSteelMembers

        from .filter_axis_range import FilterAxisRange
        from .filter_materials import FilterMaterials
        from .filter_members import FilterMembers
        from .filter_nodes import FilterNodes
        from .filter_plates import FilterPlates
        from .filter_plate_cuts import FilterPlateCuts
        from .filter_plate_strips import FilterPlateStrips
        from .filter_plate_thicknesses import FilterPlateThicknesses
        from .filter_sections import FilterSections
        from .filter_steel_connections import FilterSteelConnections
        from .filter_steel_members import FilterSteelMembers

        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "materials": lambda n : setattr(self, 'materials', n.get_object_value(FilterMaterials)),
            "members": lambda n : setattr(self, 'members', n.get_object_value(FilterMembers)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodes": lambda n : setattr(self, 'nodes', n.get_object_value(FilterNodes)),
            "plateCuts": lambda n : setattr(self, 'plate_cuts', n.get_object_value(FilterPlateCuts)),
            "plateStrips": lambda n : setattr(self, 'plate_strips', n.get_object_value(FilterPlateStrips)),
            "plateThicknesses": lambda n : setattr(self, 'plate_thicknesses', n.get_object_value(FilterPlateThicknesses)),
            "plates": lambda n : setattr(self, 'plates', n.get_object_value(FilterPlates)),
            "sections": lambda n : setattr(self, 'sections', n.get_object_value(FilterSections)),
            "steelConnections": lambda n : setattr(self, 'steel_connections', n.get_object_value(FilterSteelConnections)),
            "steelMembers": lambda n : setattr(self, 'steel_members', n.get_object_value(FilterSteelMembers)),
            "xAxis": lambda n : setattr(self, 'x_axis', n.get_object_value(FilterAxisRange)),
            "yAxis": lambda n : setattr(self, 'y_axis', n.get_object_value(FilterAxisRange)),
            "zAxis": lambda n : setattr(self, 'z_axis', n.get_object_value(FilterAxisRange)),
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
    

