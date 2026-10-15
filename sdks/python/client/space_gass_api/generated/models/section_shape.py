from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .beam_tee_shape import BeamTeeShape
    from .box_girder_shape import BoxGirderShape
    from .cee_back_to_back_shape import CeeBackToBackShape
    from .cee_shape import CeeShape
    from .channel_shape import ChannelShape
    from .circular_bar_shape import CircularBarShape
    from .circular_tube_shape import CircularTubeShape
    from .column_tee_shape import ColumnTeeShape
    from .cruciform_shape import CruciformShape
    from .d_a_long_shape import DALongShape
    from .d_a_short_shape import DAShortShape
    from .d_a_starred_shape import DAStarredShape
    from .equal_angle_shape import EqualAngleShape
    from .equilateral_triangle_shape import EquilateralTriangleShape
    from .fillet_shape import FilletShape
    from .flat_oval_shape import FlatOvalShape
    from .i_shape import IShape
    from .library_shape import LibraryShape
    from .lines_shape import LinesShape
    from .l_shape import LShape
    from .l_s_b_back_to_back_shape import LSBBackToBackShape
    from .l_s_b_shape import LSBShape
    from .not_defined_shape import NotDefinedShape
    from .plate_web_girder_shape import PlateWebGirderShape
    from .points_shape import PointsShape
    from .polygon_shape import PolygonShape
    from .polygon_tube_shape import PolygonTubeShape
    from .rack_shape import RackShape
    from .rectangular_bar_shape import RectangularBarShape
    from .rectangular_tube_shape import RectangularTubeShape
    from .rounded_angle_shape import RoundedAngleShape
    from .schifflerized_angle_shape import SchifflerizedAngleShape
    from .shape_anchor_position import ShapeAnchorPosition
    from .shape_fabrication import ShapeFabrication
    from .shape_mirror import ShapeMirror
    from .slice_shape import SliceShape
    from .square_bar_shape import SquareBarShape
    from .square_tube_shape import SquareTubeShape
    from .steel_strength import SteelStrength
    from .top_hat_shape import TopHatShape
    from .trapezoid_shape import TrapezoidShape
    from .triangle_shape import TriangleShape
    from .unequal_angle_shape import UnequalAngleShape
    from .wedge_shape import WedgeShape
    from .zed_shape import ZedShape

@dataclass
class SectionShape(AdditionalDataHolder, Parsable):
    """
    A cross-section shape. Serialised polymorphically: the `shapeType` discriminatorselects the concrete record, and each record carries only the dimensions that apply tothat shape type. Dimension, translation and point values are in the section-propertiesunit; strengths are in the material-strength unit; rotation is in degrees (seeGET /job/units).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Positions a shape by snapping one of its reference points onto a reference point of anearlier shape. Input only: it sets the shape's `translateZ` / `translateY`, whichare returned in its place.
    anchor_position: Optional[ShapeAnchorPosition] = None
    # Fabrication method of a cross-section shape. Affects residual-stress assumptions insteel design.
    fabrication: Optional[ShapeFabrication] = None
    # One-based position of the shape within the section.
    id: Optional[int] = None
    # Mirroring applied to a cross-section shape about its local axes.
    mirror: Optional[ShapeMirror] = None
    # Whether the shape is a void (hole) cut out of its parent shape.
    negative: Optional[bool] = None
    # One-based id of the parent shape this void is cut from.
    parent_shape: Optional[int] = None
    # Rotation applied to the shape.
    rotation: Optional[float] = None
    # Shape name (usually matches the section name for single-shape sections).
    shape_name: Optional[str] = None
    # The shapeType property
    shape_type: Optional[str] = None
    # Steel strength values for one grade of a shape (yield and ultimate stresses).
    strength_high: Optional[SteelStrength] = None
    # Steel strength values for one grade of a shape (yield and ultimate stresses).
    strength_normal: Optional[SteelStrength] = None
    # Translation of the shape along the section's local Y axis. Set it directly, or supply`anchorPosition` to have it computed, in which case a value given here is ignored.
    translate_y: Optional[float] = None
    # Translation of the shape along the section's local Z axis. Set it directly, or supply`anchorPosition` to have it computed, in which case a value given here is ignored.
    translate_z: Optional[float] = None
    # Whether the shape's principal axes are swapped.
    transposed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionShape:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionShape
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("shapeType")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "BeamTee".casefold():
            from .beam_tee_shape import BeamTeeShape

            return BeamTeeShape()
        if mapping_value and mapping_value.casefold() == "BoxGirder".casefold():
            from .box_girder_shape import BoxGirderShape

            return BoxGirderShape()
        if mapping_value and mapping_value.casefold() == "Cee".casefold():
            from .cee_shape import CeeShape

            return CeeShape()
        if mapping_value and mapping_value.casefold() == "CeeBackToBack".casefold():
            from .cee_back_to_back_shape import CeeBackToBackShape

            return CeeBackToBackShape()
        if mapping_value and mapping_value.casefold() == "Channel".casefold():
            from .channel_shape import ChannelShape

            return ChannelShape()
        if mapping_value and mapping_value.casefold() == "CircularBar".casefold():
            from .circular_bar_shape import CircularBarShape

            return CircularBarShape()
        if mapping_value and mapping_value.casefold() == "CircularTube".casefold():
            from .circular_tube_shape import CircularTubeShape

            return CircularTubeShape()
        if mapping_value and mapping_value.casefold() == "ColumnTee".casefold():
            from .column_tee_shape import ColumnTeeShape

            return ColumnTeeShape()
        if mapping_value and mapping_value.casefold() == "Cruciform".casefold():
            from .cruciform_shape import CruciformShape

            return CruciformShape()
        if mapping_value and mapping_value.casefold() == "DALong".casefold():
            from .d_a_long_shape import DALongShape

            return DALongShape()
        if mapping_value and mapping_value.casefold() == "DAShort".casefold():
            from .d_a_short_shape import DAShortShape

            return DAShortShape()
        if mapping_value and mapping_value.casefold() == "DAStarred".casefold():
            from .d_a_starred_shape import DAStarredShape

            return DAStarredShape()
        if mapping_value and mapping_value.casefold() == "EqualAngle".casefold():
            from .equal_angle_shape import EqualAngleShape

            return EqualAngleShape()
        if mapping_value and mapping_value.casefold() == "EquilateralTriangle".casefold():
            from .equilateral_triangle_shape import EquilateralTriangleShape

            return EquilateralTriangleShape()
        if mapping_value and mapping_value.casefold() == "Fillet".casefold():
            from .fillet_shape import FilletShape

            return FilletShape()
        if mapping_value and mapping_value.casefold() == "FlatOval".casefold():
            from .flat_oval_shape import FlatOvalShape

            return FlatOvalShape()
        if mapping_value and mapping_value.casefold() == "IShape".casefold():
            from .i_shape import IShape

            return IShape()
        if mapping_value and mapping_value.casefold() == "Library".casefold():
            from .library_shape import LibraryShape

            return LibraryShape()
        if mapping_value and mapping_value.casefold() == "LinesShape".casefold():
            from .lines_shape import LinesShape

            return LinesShape()
        if mapping_value and mapping_value.casefold() == "LSB".casefold():
            from .l_s_b_shape import LSBShape

            return LSBShape()
        if mapping_value and mapping_value.casefold() == "LSBBackToBack".casefold():
            from .l_s_b_back_to_back_shape import LSBBackToBackShape

            return LSBBackToBackShape()
        if mapping_value and mapping_value.casefold() == "LShape".casefold():
            from .l_shape import LShape

            return LShape()
        if mapping_value and mapping_value.casefold() == "NotDefined".casefold():
            from .not_defined_shape import NotDefinedShape

            return NotDefinedShape()
        if mapping_value and mapping_value.casefold() == "PlateWebGirder".casefold():
            from .plate_web_girder_shape import PlateWebGirderShape

            return PlateWebGirderShape()
        if mapping_value and mapping_value.casefold() == "PointsShape".casefold():
            from .points_shape import PointsShape

            return PointsShape()
        if mapping_value and mapping_value.casefold() == "Polygon".casefold():
            from .polygon_shape import PolygonShape

            return PolygonShape()
        if mapping_value and mapping_value.casefold() == "PolygonTube".casefold():
            from .polygon_tube_shape import PolygonTubeShape

            return PolygonTubeShape()
        if mapping_value and mapping_value.casefold() == "Rack".casefold():
            from .rack_shape import RackShape

            return RackShape()
        if mapping_value and mapping_value.casefold() == "RectangularBar".casefold():
            from .rectangular_bar_shape import RectangularBarShape

            return RectangularBarShape()
        if mapping_value and mapping_value.casefold() == "RectangularTube".casefold():
            from .rectangular_tube_shape import RectangularTubeShape

            return RectangularTubeShape()
        if mapping_value and mapping_value.casefold() == "RoundedAngle".casefold():
            from .rounded_angle_shape import RoundedAngleShape

            return RoundedAngleShape()
        if mapping_value and mapping_value.casefold() == "SchifflerizedAngle".casefold():
            from .schifflerized_angle_shape import SchifflerizedAngleShape

            return SchifflerizedAngleShape()
        if mapping_value and mapping_value.casefold() == "Slice".casefold():
            from .slice_shape import SliceShape

            return SliceShape()
        if mapping_value and mapping_value.casefold() == "SquareBar".casefold():
            from .square_bar_shape import SquareBarShape

            return SquareBarShape()
        if mapping_value and mapping_value.casefold() == "SquareTube".casefold():
            from .square_tube_shape import SquareTubeShape

            return SquareTubeShape()
        if mapping_value and mapping_value.casefold() == "TopHat".casefold():
            from .top_hat_shape import TopHatShape

            return TopHatShape()
        if mapping_value and mapping_value.casefold() == "Trapezoid".casefold():
            from .trapezoid_shape import TrapezoidShape

            return TrapezoidShape()
        if mapping_value and mapping_value.casefold() == "Triangle".casefold():
            from .triangle_shape import TriangleShape

            return TriangleShape()
        if mapping_value and mapping_value.casefold() == "UnequalAngle".casefold():
            from .unequal_angle_shape import UnequalAngleShape

            return UnequalAngleShape()
        if mapping_value and mapping_value.casefold() == "Wedge".casefold():
            from .wedge_shape import WedgeShape

            return WedgeShape()
        if mapping_value and mapping_value.casefold() == "Zed".casefold():
            from .zed_shape import ZedShape

            return ZedShape()
        return SectionShape()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .beam_tee_shape import BeamTeeShape
        from .box_girder_shape import BoxGirderShape
        from .cee_back_to_back_shape import CeeBackToBackShape
        from .cee_shape import CeeShape
        from .channel_shape import ChannelShape
        from .circular_bar_shape import CircularBarShape
        from .circular_tube_shape import CircularTubeShape
        from .column_tee_shape import ColumnTeeShape
        from .cruciform_shape import CruciformShape
        from .d_a_long_shape import DALongShape
        from .d_a_short_shape import DAShortShape
        from .d_a_starred_shape import DAStarredShape
        from .equal_angle_shape import EqualAngleShape
        from .equilateral_triangle_shape import EquilateralTriangleShape
        from .fillet_shape import FilletShape
        from .flat_oval_shape import FlatOvalShape
        from .i_shape import IShape
        from .library_shape import LibraryShape
        from .lines_shape import LinesShape
        from .l_shape import LShape
        from .l_s_b_back_to_back_shape import LSBBackToBackShape
        from .l_s_b_shape import LSBShape
        from .not_defined_shape import NotDefinedShape
        from .plate_web_girder_shape import PlateWebGirderShape
        from .points_shape import PointsShape
        from .polygon_shape import PolygonShape
        from .polygon_tube_shape import PolygonTubeShape
        from .rack_shape import RackShape
        from .rectangular_bar_shape import RectangularBarShape
        from .rectangular_tube_shape import RectangularTubeShape
        from .rounded_angle_shape import RoundedAngleShape
        from .schifflerized_angle_shape import SchifflerizedAngleShape
        from .shape_anchor_position import ShapeAnchorPosition
        from .shape_fabrication import ShapeFabrication
        from .shape_mirror import ShapeMirror
        from .slice_shape import SliceShape
        from .square_bar_shape import SquareBarShape
        from .square_tube_shape import SquareTubeShape
        from .steel_strength import SteelStrength
        from .top_hat_shape import TopHatShape
        from .trapezoid_shape import TrapezoidShape
        from .triangle_shape import TriangleShape
        from .unequal_angle_shape import UnequalAngleShape
        from .wedge_shape import WedgeShape
        from .zed_shape import ZedShape

        from .beam_tee_shape import BeamTeeShape
        from .box_girder_shape import BoxGirderShape
        from .cee_back_to_back_shape import CeeBackToBackShape
        from .cee_shape import CeeShape
        from .channel_shape import ChannelShape
        from .circular_bar_shape import CircularBarShape
        from .circular_tube_shape import CircularTubeShape
        from .column_tee_shape import ColumnTeeShape
        from .cruciform_shape import CruciformShape
        from .d_a_long_shape import DALongShape
        from .d_a_short_shape import DAShortShape
        from .d_a_starred_shape import DAStarredShape
        from .equal_angle_shape import EqualAngleShape
        from .equilateral_triangle_shape import EquilateralTriangleShape
        from .fillet_shape import FilletShape
        from .flat_oval_shape import FlatOvalShape
        from .i_shape import IShape
        from .library_shape import LibraryShape
        from .lines_shape import LinesShape
        from .l_shape import LShape
        from .l_s_b_back_to_back_shape import LSBBackToBackShape
        from .l_s_b_shape import LSBShape
        from .not_defined_shape import NotDefinedShape
        from .plate_web_girder_shape import PlateWebGirderShape
        from .points_shape import PointsShape
        from .polygon_shape import PolygonShape
        from .polygon_tube_shape import PolygonTubeShape
        from .rack_shape import RackShape
        from .rectangular_bar_shape import RectangularBarShape
        from .rectangular_tube_shape import RectangularTubeShape
        from .rounded_angle_shape import RoundedAngleShape
        from .schifflerized_angle_shape import SchifflerizedAngleShape
        from .shape_anchor_position import ShapeAnchorPosition
        from .shape_fabrication import ShapeFabrication
        from .shape_mirror import ShapeMirror
        from .slice_shape import SliceShape
        from .square_bar_shape import SquareBarShape
        from .square_tube_shape import SquareTubeShape
        from .steel_strength import SteelStrength
        from .top_hat_shape import TopHatShape
        from .trapezoid_shape import TrapezoidShape
        from .triangle_shape import TriangleShape
        from .unequal_angle_shape import UnequalAngleShape
        from .wedge_shape import WedgeShape
        from .zed_shape import ZedShape

        fields: dict[str, Callable[[Any], None]] = {
            "anchorPosition": lambda n : setattr(self, 'anchor_position', n.get_object_value(ShapeAnchorPosition)),
            "fabrication": lambda n : setattr(self, 'fabrication', n.get_enum_value(ShapeFabrication)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mirror": lambda n : setattr(self, 'mirror', n.get_enum_value(ShapeMirror)),
            "negative": lambda n : setattr(self, 'negative', n.get_bool_value()),
            "parentShape": lambda n : setattr(self, 'parent_shape', n.get_int_value()),
            "rotation": lambda n : setattr(self, 'rotation', n.get_float_value()),
            "shapeName": lambda n : setattr(self, 'shape_name', n.get_str_value()),
            "shapeType": lambda n : setattr(self, 'shape_type', n.get_str_value()),
            "strengthHigh": lambda n : setattr(self, 'strength_high', n.get_object_value(SteelStrength)),
            "strengthNormal": lambda n : setattr(self, 'strength_normal', n.get_object_value(SteelStrength)),
            "translateY": lambda n : setattr(self, 'translate_y', n.get_float_value()),
            "translateZ": lambda n : setattr(self, 'translate_z', n.get_float_value()),
            "transposed": lambda n : setattr(self, 'transposed', n.get_bool_value()),
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
        writer.write_object_value("anchorPosition", self.anchor_position)
        writer.write_enum_value("fabrication", self.fabrication)
        writer.write_int_value("id", self.id)
        writer.write_enum_value("mirror", self.mirror)
        writer.write_bool_value("negative", self.negative)
        writer.write_int_value("parentShape", self.parent_shape)
        writer.write_float_value("rotation", self.rotation)
        writer.write_str_value("shapeName", self.shape_name)
        writer.write_str_value("shapeType", self.shape_type)
        writer.write_object_value("strengthHigh", self.strength_high)
        writer.write_object_value("strengthNormal", self.strength_normal)
        writer.write_float_value("translateY", self.translate_y)
        writer.write_float_value("translateZ", self.translate_z)
        writer.write_bool_value("transposed", self.transposed)
        writer.write_additional_data_value(self.additional_data)
    

