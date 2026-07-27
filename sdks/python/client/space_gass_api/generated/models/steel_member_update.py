from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .angle_type import AngleType
    from .is800_seismic_classification import Is800SeismicClassification
    from .length_unit_basis import LengthUnitBasis
    from .load_height_position import LoadHeightPosition
    from .nzs3404_seismic_classification import Nzs3404SeismicClassification
    from .steel_design_criteria import SteelDesignCriteria
    from .steel_member_end_connection import SteelMemberEndConnection
    from .steel_member_type import SteelMemberType
    from .steel_strength_grade import SteelStrengthGrade

@dataclass
class SteelMemberUpdate(Parsable):
    """
    DTO for updating an existing steel member design data entity (design group).All fields are nullable to support partial updates — omit a field to keep its current value.
    """
    # Angle section type for structural sections.Maps to SPACE GASS lookup table "Angle Type".
    angle_type: Optional[AngleType] = None
    # Bolt diameter, used in net-section checks.
    bolt_diameter: Optional[float] = None
    # Positions of intermediate bottom flange restraints along the design group, in SG list format.
    btm_flange_intermediate_restraint_positions: Optional[str] = None
    # Bottom flange restraint type codes: the end restraints plus one code per intermediate restraint position.
    btm_flange_restraint_types: Optional[str] = None
    # Whether the lateral-torsional buckling length (Lb) is calculated from the flange restraints.
    calculate_lb_from_flange_restraints: Optional[bool] = None
    # Whether the major axis effective length (Lc-Major) is calculated from a buckling analysis.
    calculate_lc_major_from_buckling: Optional[bool] = None
    # Whether the minor axis effective length (Lc-Minor) is calculated from a buckling analysis.
    calculate_lc_minor_from_buckling: Optional[bool] = None
    # Whether eccentric connection effects are considered.
    consider_eccentric_effects: Optional[bool] = None
    # Optional description of the design group.
    description: Optional[str] = None
    # Optimisation criteria used when a steel member design run selects a new sectionfor a design group.Maps to SPACE GASS lookup table "Design Criteria".
    design_criteria: Optional[SteelDesignCriteria] = None
    # End connection configuration for a steel member design group,used in eccentric connection and net-section checks.Maps to SPACE GASS lookup table "End Connection".
    end_connection: Optional[SteelMemberEndConnection] = None
    # Primary identifier of the entity to update.Optional for single updates (Id comes from route), required for bulk updates.
    id: Optional[int] = None
    # IS800 seismic frame classification for a steel member design group.Setting a braced or moment frame type activates the seismic checks when the IS800 design code is used.Maps to SPACE GASS lookup table "IS Seismic Class".
    is800_seismic_classification: Optional[Is800SeismicClassification] = None
    # Lateral-torsional buckling length (Lb) for negative bending.
    lb_negative_bending: Optional[float] = None
    # Lateral-torsional buckling length (Lb) for positive bending.
    lb_positive_bending: Optional[float] = None
    # Effective length for major axis buckling (Lc-Major).
    lc_major: Optional[float] = None
    # Effective length for minor axis buckling (Lc-Minor).
    lc_minor: Optional[float] = None
    # Whether a length-style value is given as an actual length (in the job's length unit)or as a dimensionless ratio of a reference length.
    length_unit_basis: Optional[LengthUnitBasis] = None
    # Position on the cross-section at which transverse loads are applied,used in lateral-torsional buckling checks.Maps to SPACE GASS lookup table "Load Height".
    load_height_position: Optional[LoadHeightPosition] = None
    # Whether the group ends are braced in position for major axis buckling.
    major_axis_braced_at_ends: Optional[bool] = None
    # Maximum number of bolts in the cross-section, used in net-section checks.
    max_bolts_in_cross_section: Optional[int] = None
    # Member classification for a steel member design group.Determines which IS800 or NZS3404 seismic checks are done for the various member types.Maps to SPACE GASS lookup table "Member Class".
    member_type: Optional[SteelMemberType] = None
    # Members that make up the design group, as a plain comma-separated list of member Ids — e.g. `"1,2,3"` (ranges are not supported).
    members: Optional[str] = None
    # Whether the group ends are braced in position for minor axis buckling.
    minor_axis_braced_at_ends: Optional[bool] = None
    # NZS3404 seismic member category for a steel member design group.Setting category 1 to 4 activates the seismic checks when the NZS3404 design code is used.Maps to SPACE GASS lookup table "NZ Seismic Class".
    nzs3404_seismic_classification: Optional[Nzs3404SeismicClassification] = None
    # Scan code letters that group compatible sections for member selection during a design run.
    scan_code: Optional[str] = None
    # Steel strength grade for a steel member design group.Maps to SPACE GASS lookup table "Strength Grade".
    strength_grade: Optional[SteelStrengthGrade] = None
    # Positions of intermediate top flange restraints along the design group, in SG list format.
    top_flange_intermediate_restraint_positions: Optional[str] = None
    # Top flange restraint type codes: the end restraints plus one code per intermediate restraint position.
    top_flange_restraint_types: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SteelMemberUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SteelMemberUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SteelMemberUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .angle_type import AngleType
        from .is800_seismic_classification import Is800SeismicClassification
        from .length_unit_basis import LengthUnitBasis
        from .load_height_position import LoadHeightPosition
        from .nzs3404_seismic_classification import Nzs3404SeismicClassification
        from .steel_design_criteria import SteelDesignCriteria
        from .steel_member_end_connection import SteelMemberEndConnection
        from .steel_member_type import SteelMemberType
        from .steel_strength_grade import SteelStrengthGrade

        from .angle_type import AngleType
        from .is800_seismic_classification import Is800SeismicClassification
        from .length_unit_basis import LengthUnitBasis
        from .load_height_position import LoadHeightPosition
        from .nzs3404_seismic_classification import Nzs3404SeismicClassification
        from .steel_design_criteria import SteelDesignCriteria
        from .steel_member_end_connection import SteelMemberEndConnection
        from .steel_member_type import SteelMemberType
        from .steel_strength_grade import SteelStrengthGrade

        fields: dict[str, Callable[[Any], None]] = {
            "angleType": lambda n : setattr(self, 'angle_type', n.get_enum_value(AngleType)),
            "boltDiameter": lambda n : setattr(self, 'bolt_diameter', n.get_float_value()),
            "btmFlangeIntermediateRestraintPositions": lambda n : setattr(self, 'btm_flange_intermediate_restraint_positions', n.get_str_value()),
            "btmFlangeRestraintTypes": lambda n : setattr(self, 'btm_flange_restraint_types', n.get_str_value()),
            "calculateLbFromFlangeRestraints": lambda n : setattr(self, 'calculate_lb_from_flange_restraints', n.get_bool_value()),
            "calculateLcMajorFromBuckling": lambda n : setattr(self, 'calculate_lc_major_from_buckling', n.get_bool_value()),
            "calculateLcMinorFromBuckling": lambda n : setattr(self, 'calculate_lc_minor_from_buckling', n.get_bool_value()),
            "considerEccentricEffects": lambda n : setattr(self, 'consider_eccentric_effects', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "designCriteria": lambda n : setattr(self, 'design_criteria', n.get_enum_value(SteelDesignCriteria)),
            "endConnection": lambda n : setattr(self, 'end_connection', n.get_enum_value(SteelMemberEndConnection)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "is800SeismicClassification": lambda n : setattr(self, 'is800_seismic_classification', n.get_enum_value(Is800SeismicClassification)),
            "lbNegativeBending": lambda n : setattr(self, 'lb_negative_bending', n.get_float_value()),
            "lbPositiveBending": lambda n : setattr(self, 'lb_positive_bending', n.get_float_value()),
            "lcMajor": lambda n : setattr(self, 'lc_major', n.get_float_value()),
            "lcMinor": lambda n : setattr(self, 'lc_minor', n.get_float_value()),
            "lengthUnitBasis": lambda n : setattr(self, 'length_unit_basis', n.get_enum_value(LengthUnitBasis)),
            "loadHeightPosition": lambda n : setattr(self, 'load_height_position', n.get_enum_value(LoadHeightPosition)),
            "majorAxisBracedAtEnds": lambda n : setattr(self, 'major_axis_braced_at_ends', n.get_bool_value()),
            "maxBoltsInCrossSection": lambda n : setattr(self, 'max_bolts_in_cross_section', n.get_int_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_enum_value(SteelMemberType)),
            "members": lambda n : setattr(self, 'members', n.get_str_value()),
            "minorAxisBracedAtEnds": lambda n : setattr(self, 'minor_axis_braced_at_ends', n.get_bool_value()),
            "nzs3404SeismicClassification": lambda n : setattr(self, 'nzs3404_seismic_classification', n.get_enum_value(Nzs3404SeismicClassification)),
            "scanCode": lambda n : setattr(self, 'scan_code', n.get_str_value()),
            "strengthGrade": lambda n : setattr(self, 'strength_grade', n.get_enum_value(SteelStrengthGrade)),
            "topFlangeIntermediateRestraintPositions": lambda n : setattr(self, 'top_flange_intermediate_restraint_positions', n.get_str_value()),
            "topFlangeRestraintTypes": lambda n : setattr(self, 'top_flange_restraint_types', n.get_str_value()),
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
        writer.write_enum_value("angleType", self.angle_type)
        writer.write_float_value("boltDiameter", self.bolt_diameter)
        writer.write_str_value("btmFlangeIntermediateRestraintPositions", self.btm_flange_intermediate_restraint_positions)
        writer.write_str_value("btmFlangeRestraintTypes", self.btm_flange_restraint_types)
        writer.write_bool_value("calculateLbFromFlangeRestraints", self.calculate_lb_from_flange_restraints)
        writer.write_bool_value("calculateLcMajorFromBuckling", self.calculate_lc_major_from_buckling)
        writer.write_bool_value("calculateLcMinorFromBuckling", self.calculate_lc_minor_from_buckling)
        writer.write_bool_value("considerEccentricEffects", self.consider_eccentric_effects)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("designCriteria", self.design_criteria)
        writer.write_enum_value("endConnection", self.end_connection)
        writer.write_int_value("id", self.id)
        writer.write_enum_value("is800SeismicClassification", self.is800_seismic_classification)
        writer.write_float_value("lbNegativeBending", self.lb_negative_bending)
        writer.write_float_value("lbPositiveBending", self.lb_positive_bending)
        writer.write_float_value("lcMajor", self.lc_major)
        writer.write_float_value("lcMinor", self.lc_minor)
        writer.write_enum_value("lengthUnitBasis", self.length_unit_basis)
        writer.write_enum_value("loadHeightPosition", self.load_height_position)
        writer.write_bool_value("majorAxisBracedAtEnds", self.major_axis_braced_at_ends)
        writer.write_int_value("maxBoltsInCrossSection", self.max_bolts_in_cross_section)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_str_value("members", self.members)
        writer.write_bool_value("minorAxisBracedAtEnds", self.minor_axis_braced_at_ends)
        writer.write_enum_value("nzs3404SeismicClassification", self.nzs3404_seismic_classification)
        writer.write_str_value("scanCode", self.scan_code)
        writer.write_enum_value("strengthGrade", self.strength_grade)
        writer.write_str_value("topFlangeIntermediateRestraintPositions", self.top_flange_intermediate_restraint_positions)
        writer.write_str_value("topFlangeRestraintTypes", self.top_flange_restraint_types)
    

