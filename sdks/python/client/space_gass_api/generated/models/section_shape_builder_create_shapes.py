from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
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
    from .slice_shape import SliceShape
    from .square_bar_shape import SquareBarShape
    from .square_tube_shape import SquareTubeShape
    from .top_hat_shape import TopHatShape
    from .trapezoid_shape import TrapezoidShape
    from .triangle_shape import TriangleShape
    from .unequal_angle_shape import UnequalAngleShape
    from .wedge_shape import WedgeShape
    from .zed_shape import ZedShape

@dataclass
class SectionShapeBuilderCreate_shapes(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes BeamTeeShape, BoxGirderShape, CeeBackToBackShape, CeeShape, ChannelShape, CircularBarShape, CircularTubeShape, ColumnTeeShape, CruciformShape, DALongShape, DAShortShape, DAStarredShape, EqualAngleShape, EquilateralTriangleShape, FilletShape, FlatOvalShape, IShape, LibraryShape, LinesShape, LSBBackToBackShape, LSBShape, LShape, NotDefinedShape, PlateWebGirderShape, PointsShape, PolygonShape, PolygonTubeShape, RackShape, RectangularBarShape, RectangularTubeShape, RoundedAngleShape, SchifflerizedAngleShape, SliceShape, SquareBarShape, SquareTubeShape, TopHatShape, TrapezoidShape, TriangleShape, UnequalAngleShape, WedgeShape, ZedShape
    """
    # Composed type representation for type BeamTeeShape
    beam_tee_shape: Optional[BeamTeeShape] = None
    # Composed type representation for type BoxGirderShape
    box_girder_shape: Optional[BoxGirderShape] = None
    # Composed type representation for type CeeBackToBackShape
    cee_back_to_back_shape: Optional[CeeBackToBackShape] = None
    # Composed type representation for type CeeShape
    cee_shape: Optional[CeeShape] = None
    # Composed type representation for type ChannelShape
    channel_shape: Optional[ChannelShape] = None
    # Composed type representation for type CircularBarShape
    circular_bar_shape: Optional[CircularBarShape] = None
    # Composed type representation for type CircularTubeShape
    circular_tube_shape: Optional[CircularTubeShape] = None
    # Composed type representation for type ColumnTeeShape
    column_tee_shape: Optional[ColumnTeeShape] = None
    # Composed type representation for type CruciformShape
    cruciform_shape: Optional[CruciformShape] = None
    # Composed type representation for type DALongShape
    d_a_long_shape: Optional[DALongShape] = None
    # Composed type representation for type DAShortShape
    d_a_short_shape: Optional[DAShortShape] = None
    # Composed type representation for type DAStarredShape
    d_a_starred_shape: Optional[DAStarredShape] = None
    # Composed type representation for type EqualAngleShape
    equal_angle_shape: Optional[EqualAngleShape] = None
    # Composed type representation for type EquilateralTriangleShape
    equilateral_triangle_shape: Optional[EquilateralTriangleShape] = None
    # Composed type representation for type FilletShape
    fillet_shape: Optional[FilletShape] = None
    # Composed type representation for type FlatOvalShape
    flat_oval_shape: Optional[FlatOvalShape] = None
    # Composed type representation for type IShape
    i_shape: Optional[IShape] = None
    # Composed type representation for type LSBBackToBackShape
    l_s_b_back_to_back_shape: Optional[LSBBackToBackShape] = None
    # Composed type representation for type LSBShape
    l_s_b_shape: Optional[LSBShape] = None
    # Composed type representation for type LShape
    l_shape: Optional[LShape] = None
    # Composed type representation for type LibraryShape
    library_shape: Optional[LibraryShape] = None
    # Composed type representation for type LinesShape
    lines_shape: Optional[LinesShape] = None
    # Composed type representation for type NotDefinedShape
    not_defined_shape: Optional[NotDefinedShape] = None
    # Composed type representation for type PlateWebGirderShape
    plate_web_girder_shape: Optional[PlateWebGirderShape] = None
    # Composed type representation for type PointsShape
    points_shape: Optional[PointsShape] = None
    # Composed type representation for type PolygonShape
    polygon_shape: Optional[PolygonShape] = None
    # Composed type representation for type PolygonTubeShape
    polygon_tube_shape: Optional[PolygonTubeShape] = None
    # Composed type representation for type RackShape
    rack_shape: Optional[RackShape] = None
    # Composed type representation for type RectangularBarShape
    rectangular_bar_shape: Optional[RectangularBarShape] = None
    # Composed type representation for type RectangularTubeShape
    rectangular_tube_shape: Optional[RectangularTubeShape] = None
    # Composed type representation for type RoundedAngleShape
    rounded_angle_shape: Optional[RoundedAngleShape] = None
    # Composed type representation for type SchifflerizedAngleShape
    schifflerized_angle_shape: Optional[SchifflerizedAngleShape] = None
    # Composed type representation for type SliceShape
    slice_shape: Optional[SliceShape] = None
    # Composed type representation for type SquareBarShape
    square_bar_shape: Optional[SquareBarShape] = None
    # Composed type representation for type SquareTubeShape
    square_tube_shape: Optional[SquareTubeShape] = None
    # Composed type representation for type TopHatShape
    top_hat_shape: Optional[TopHatShape] = None
    # Composed type representation for type TrapezoidShape
    trapezoid_shape: Optional[TrapezoidShape] = None
    # Composed type representation for type TriangleShape
    triangle_shape: Optional[TriangleShape] = None
    # Composed type representation for type UnequalAngleShape
    unequal_angle_shape: Optional[UnequalAngleShape] = None
    # Composed type representation for type WedgeShape
    wedge_shape: Optional[WedgeShape] = None
    # Composed type representation for type ZedShape
    zed_shape: Optional[ZedShape] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionShapeBuilderCreate_shapes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionShapeBuilderCreate_shapes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("shapeType")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SectionShapeBuilderCreate_shapes()
        if mapping_value and mapping_value.casefold() == "BeamTee".casefold():
            from .beam_tee_shape import BeamTeeShape

            result.beam_tee_shape = BeamTeeShape()
        elif mapping_value and mapping_value.casefold() == "BoxGirder".casefold():
            from .box_girder_shape import BoxGirderShape

            result.box_girder_shape = BoxGirderShape()
        elif mapping_value and mapping_value.casefold() == "CeeBackToBack".casefold():
            from .cee_back_to_back_shape import CeeBackToBackShape

            result.cee_back_to_back_shape = CeeBackToBackShape()
        elif mapping_value and mapping_value.casefold() == "Cee".casefold():
            from .cee_shape import CeeShape

            result.cee_shape = CeeShape()
        elif mapping_value and mapping_value.casefold() == "Channel".casefold():
            from .channel_shape import ChannelShape

            result.channel_shape = ChannelShape()
        elif mapping_value and mapping_value.casefold() == "CircularBar".casefold():
            from .circular_bar_shape import CircularBarShape

            result.circular_bar_shape = CircularBarShape()
        elif mapping_value and mapping_value.casefold() == "CircularTube".casefold():
            from .circular_tube_shape import CircularTubeShape

            result.circular_tube_shape = CircularTubeShape()
        elif mapping_value and mapping_value.casefold() == "ColumnTee".casefold():
            from .column_tee_shape import ColumnTeeShape

            result.column_tee_shape = ColumnTeeShape()
        elif mapping_value and mapping_value.casefold() == "Cruciform".casefold():
            from .cruciform_shape import CruciformShape

            result.cruciform_shape = CruciformShape()
        elif mapping_value and mapping_value.casefold() == "DALong".casefold():
            from .d_a_long_shape import DALongShape

            result.d_a_long_shape = DALongShape()
        elif mapping_value and mapping_value.casefold() == "DAShort".casefold():
            from .d_a_short_shape import DAShortShape

            result.d_a_short_shape = DAShortShape()
        elif mapping_value and mapping_value.casefold() == "DAStarred".casefold():
            from .d_a_starred_shape import DAStarredShape

            result.d_a_starred_shape = DAStarredShape()
        elif mapping_value and mapping_value.casefold() == "EqualAngle".casefold():
            from .equal_angle_shape import EqualAngleShape

            result.equal_angle_shape = EqualAngleShape()
        elif mapping_value and mapping_value.casefold() == "EquilateralTriangle".casefold():
            from .equilateral_triangle_shape import EquilateralTriangleShape

            result.equilateral_triangle_shape = EquilateralTriangleShape()
        elif mapping_value and mapping_value.casefold() == "Fillet".casefold():
            from .fillet_shape import FilletShape

            result.fillet_shape = FilletShape()
        elif mapping_value and mapping_value.casefold() == "FlatOval".casefold():
            from .flat_oval_shape import FlatOvalShape

            result.flat_oval_shape = FlatOvalShape()
        elif mapping_value and mapping_value.casefold() == "IShape".casefold():
            from .i_shape import IShape

            result.i_shape = IShape()
        elif mapping_value and mapping_value.casefold() == "LSBBackToBack".casefold():
            from .l_s_b_back_to_back_shape import LSBBackToBackShape

            result.l_s_b_back_to_back_shape = LSBBackToBackShape()
        elif mapping_value and mapping_value.casefold() == "LSB".casefold():
            from .l_s_b_shape import LSBShape

            result.l_s_b_shape = LSBShape()
        elif mapping_value and mapping_value.casefold() == "LShape".casefold():
            from .l_shape import LShape

            result.l_shape = LShape()
        elif mapping_value and mapping_value.casefold() == "Library".casefold():
            from .library_shape import LibraryShape

            result.library_shape = LibraryShape()
        elif mapping_value and mapping_value.casefold() == "LinesShape".casefold():
            from .lines_shape import LinesShape

            result.lines_shape = LinesShape()
        elif mapping_value and mapping_value.casefold() == "NotDefined".casefold():
            from .not_defined_shape import NotDefinedShape

            result.not_defined_shape = NotDefinedShape()
        elif mapping_value and mapping_value.casefold() == "PlateWebGirder".casefold():
            from .plate_web_girder_shape import PlateWebGirderShape

            result.plate_web_girder_shape = PlateWebGirderShape()
        elif mapping_value and mapping_value.casefold() == "PointsShape".casefold():
            from .points_shape import PointsShape

            result.points_shape = PointsShape()
        elif mapping_value and mapping_value.casefold() == "Polygon".casefold():
            from .polygon_shape import PolygonShape

            result.polygon_shape = PolygonShape()
        elif mapping_value and mapping_value.casefold() == "PolygonTube".casefold():
            from .polygon_tube_shape import PolygonTubeShape

            result.polygon_tube_shape = PolygonTubeShape()
        elif mapping_value and mapping_value.casefold() == "Rack".casefold():
            from .rack_shape import RackShape

            result.rack_shape = RackShape()
        elif mapping_value and mapping_value.casefold() == "RectangularBar".casefold():
            from .rectangular_bar_shape import RectangularBarShape

            result.rectangular_bar_shape = RectangularBarShape()
        elif mapping_value and mapping_value.casefold() == "RectangularTube".casefold():
            from .rectangular_tube_shape import RectangularTubeShape

            result.rectangular_tube_shape = RectangularTubeShape()
        elif mapping_value and mapping_value.casefold() == "RoundedAngle".casefold():
            from .rounded_angle_shape import RoundedAngleShape

            result.rounded_angle_shape = RoundedAngleShape()
        elif mapping_value and mapping_value.casefold() == "SchifflerizedAngle".casefold():
            from .schifflerized_angle_shape import SchifflerizedAngleShape

            result.schifflerized_angle_shape = SchifflerizedAngleShape()
        elif mapping_value and mapping_value.casefold() == "Slice".casefold():
            from .slice_shape import SliceShape

            result.slice_shape = SliceShape()
        elif mapping_value and mapping_value.casefold() == "SquareBar".casefold():
            from .square_bar_shape import SquareBarShape

            result.square_bar_shape = SquareBarShape()
        elif mapping_value and mapping_value.casefold() == "SquareTube".casefold():
            from .square_tube_shape import SquareTubeShape

            result.square_tube_shape = SquareTubeShape()
        elif mapping_value and mapping_value.casefold() == "TopHat".casefold():
            from .top_hat_shape import TopHatShape

            result.top_hat_shape = TopHatShape()
        elif mapping_value and mapping_value.casefold() == "Trapezoid".casefold():
            from .trapezoid_shape import TrapezoidShape

            result.trapezoid_shape = TrapezoidShape()
        elif mapping_value and mapping_value.casefold() == "Triangle".casefold():
            from .triangle_shape import TriangleShape

            result.triangle_shape = TriangleShape()
        elif mapping_value and mapping_value.casefold() == "UnequalAngle".casefold():
            from .unequal_angle_shape import UnequalAngleShape

            result.unequal_angle_shape = UnequalAngleShape()
        elif mapping_value and mapping_value.casefold() == "Wedge".casefold():
            from .wedge_shape import WedgeShape

            result.wedge_shape = WedgeShape()
        elif mapping_value and mapping_value.casefold() == "Zed".casefold():
            from .zed_shape import ZedShape

            result.zed_shape = ZedShape()
        return result
    
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
        from .slice_shape import SliceShape
        from .square_bar_shape import SquareBarShape
        from .square_tube_shape import SquareTubeShape
        from .top_hat_shape import TopHatShape
        from .trapezoid_shape import TrapezoidShape
        from .triangle_shape import TriangleShape
        from .unequal_angle_shape import UnequalAngleShape
        from .wedge_shape import WedgeShape
        from .zed_shape import ZedShape

        if self.beam_tee_shape:
            return self.beam_tee_shape.get_field_deserializers()
        if self.box_girder_shape:
            return self.box_girder_shape.get_field_deserializers()
        if self.cee_back_to_back_shape:
            return self.cee_back_to_back_shape.get_field_deserializers()
        if self.cee_shape:
            return self.cee_shape.get_field_deserializers()
        if self.channel_shape:
            return self.channel_shape.get_field_deserializers()
        if self.circular_bar_shape:
            return self.circular_bar_shape.get_field_deserializers()
        if self.circular_tube_shape:
            return self.circular_tube_shape.get_field_deserializers()
        if self.column_tee_shape:
            return self.column_tee_shape.get_field_deserializers()
        if self.cruciform_shape:
            return self.cruciform_shape.get_field_deserializers()
        if self.d_a_long_shape:
            return self.d_a_long_shape.get_field_deserializers()
        if self.d_a_short_shape:
            return self.d_a_short_shape.get_field_deserializers()
        if self.d_a_starred_shape:
            return self.d_a_starred_shape.get_field_deserializers()
        if self.equal_angle_shape:
            return self.equal_angle_shape.get_field_deserializers()
        if self.equilateral_triangle_shape:
            return self.equilateral_triangle_shape.get_field_deserializers()
        if self.fillet_shape:
            return self.fillet_shape.get_field_deserializers()
        if self.flat_oval_shape:
            return self.flat_oval_shape.get_field_deserializers()
        if self.i_shape:
            return self.i_shape.get_field_deserializers()
        if self.l_s_b_back_to_back_shape:
            return self.l_s_b_back_to_back_shape.get_field_deserializers()
        if self.l_s_b_shape:
            return self.l_s_b_shape.get_field_deserializers()
        if self.l_shape:
            return self.l_shape.get_field_deserializers()
        if self.library_shape:
            return self.library_shape.get_field_deserializers()
        if self.lines_shape:
            return self.lines_shape.get_field_deserializers()
        if self.not_defined_shape:
            return self.not_defined_shape.get_field_deserializers()
        if self.plate_web_girder_shape:
            return self.plate_web_girder_shape.get_field_deserializers()
        if self.points_shape:
            return self.points_shape.get_field_deserializers()
        if self.polygon_shape:
            return self.polygon_shape.get_field_deserializers()
        if self.polygon_tube_shape:
            return self.polygon_tube_shape.get_field_deserializers()
        if self.rack_shape:
            return self.rack_shape.get_field_deserializers()
        if self.rectangular_bar_shape:
            return self.rectangular_bar_shape.get_field_deserializers()
        if self.rectangular_tube_shape:
            return self.rectangular_tube_shape.get_field_deserializers()
        if self.rounded_angle_shape:
            return self.rounded_angle_shape.get_field_deserializers()
        if self.schifflerized_angle_shape:
            return self.schifflerized_angle_shape.get_field_deserializers()
        if self.slice_shape:
            return self.slice_shape.get_field_deserializers()
        if self.square_bar_shape:
            return self.square_bar_shape.get_field_deserializers()
        if self.square_tube_shape:
            return self.square_tube_shape.get_field_deserializers()
        if self.top_hat_shape:
            return self.top_hat_shape.get_field_deserializers()
        if self.trapezoid_shape:
            return self.trapezoid_shape.get_field_deserializers()
        if self.triangle_shape:
            return self.triangle_shape.get_field_deserializers()
        if self.unequal_angle_shape:
            return self.unequal_angle_shape.get_field_deserializers()
        if self.wedge_shape:
            return self.wedge_shape.get_field_deserializers()
        if self.zed_shape:
            return self.zed_shape.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.beam_tee_shape is not None:
            writer.write_object_value(None, self.beam_tee_shape)
        elif self.box_girder_shape is not None:
            writer.write_object_value(None, self.box_girder_shape)
        elif self.cee_back_to_back_shape is not None:
            writer.write_object_value(None, self.cee_back_to_back_shape)
        elif self.cee_shape is not None:
            writer.write_object_value(None, self.cee_shape)
        elif self.channel_shape is not None:
            writer.write_object_value(None, self.channel_shape)
        elif self.circular_bar_shape is not None:
            writer.write_object_value(None, self.circular_bar_shape)
        elif self.circular_tube_shape is not None:
            writer.write_object_value(None, self.circular_tube_shape)
        elif self.column_tee_shape is not None:
            writer.write_object_value(None, self.column_tee_shape)
        elif self.cruciform_shape is not None:
            writer.write_object_value(None, self.cruciform_shape)
        elif self.d_a_long_shape is not None:
            writer.write_object_value(None, self.d_a_long_shape)
        elif self.d_a_short_shape is not None:
            writer.write_object_value(None, self.d_a_short_shape)
        elif self.d_a_starred_shape is not None:
            writer.write_object_value(None, self.d_a_starred_shape)
        elif self.equal_angle_shape is not None:
            writer.write_object_value(None, self.equal_angle_shape)
        elif self.equilateral_triangle_shape is not None:
            writer.write_object_value(None, self.equilateral_triangle_shape)
        elif self.fillet_shape is not None:
            writer.write_object_value(None, self.fillet_shape)
        elif self.flat_oval_shape is not None:
            writer.write_object_value(None, self.flat_oval_shape)
        elif self.i_shape is not None:
            writer.write_object_value(None, self.i_shape)
        elif self.l_s_b_back_to_back_shape is not None:
            writer.write_object_value(None, self.l_s_b_back_to_back_shape)
        elif self.l_s_b_shape is not None:
            writer.write_object_value(None, self.l_s_b_shape)
        elif self.l_shape is not None:
            writer.write_object_value(None, self.l_shape)
        elif self.library_shape is not None:
            writer.write_object_value(None, self.library_shape)
        elif self.lines_shape is not None:
            writer.write_object_value(None, self.lines_shape)
        elif self.not_defined_shape is not None:
            writer.write_object_value(None, self.not_defined_shape)
        elif self.plate_web_girder_shape is not None:
            writer.write_object_value(None, self.plate_web_girder_shape)
        elif self.points_shape is not None:
            writer.write_object_value(None, self.points_shape)
        elif self.polygon_shape is not None:
            writer.write_object_value(None, self.polygon_shape)
        elif self.polygon_tube_shape is not None:
            writer.write_object_value(None, self.polygon_tube_shape)
        elif self.rack_shape is not None:
            writer.write_object_value(None, self.rack_shape)
        elif self.rectangular_bar_shape is not None:
            writer.write_object_value(None, self.rectangular_bar_shape)
        elif self.rectangular_tube_shape is not None:
            writer.write_object_value(None, self.rectangular_tube_shape)
        elif self.rounded_angle_shape is not None:
            writer.write_object_value(None, self.rounded_angle_shape)
        elif self.schifflerized_angle_shape is not None:
            writer.write_object_value(None, self.schifflerized_angle_shape)
        elif self.slice_shape is not None:
            writer.write_object_value(None, self.slice_shape)
        elif self.square_bar_shape is not None:
            writer.write_object_value(None, self.square_bar_shape)
        elif self.square_tube_shape is not None:
            writer.write_object_value(None, self.square_tube_shape)
        elif self.top_hat_shape is not None:
            writer.write_object_value(None, self.top_hat_shape)
        elif self.trapezoid_shape is not None:
            writer.write_object_value(None, self.trapezoid_shape)
        elif self.triangle_shape is not None:
            writer.write_object_value(None, self.triangle_shape)
        elif self.unequal_angle_shape is not None:
            writer.write_object_value(None, self.unequal_angle_shape)
        elif self.wedge_shape is not None:
            writer.write_object_value(None, self.wedge_shape)
        elif self.zed_shape is not None:
            writer.write_object_value(None, self.zed_shape)
    

