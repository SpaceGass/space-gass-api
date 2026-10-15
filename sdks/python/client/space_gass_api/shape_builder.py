"""
Hand-maintained helpers for shape-builder (built-up) sections — parity with
the C# SDK's ``Utils/SectionShapeExtensions.cs``.

A section's shapes are polymorphic (``shapeType`` discriminator), so the
spec models them as a oneOf and Kiota wraps each list element in a composed
type with one attribute per shape type:

- ``SectionShapeBuilderCreate_shapes`` (request)
- ``Section_shapes`` (response)

Raw usage means ``SectionShapeBuilderCreate_shapes(library_shape=LibraryShape(
shape_type="Library", ...))`` per shape. These helpers let you pass the
shapes directly and read them back typed, with the discriminator filled in::

    from space_gass_api import shape_builder
    import space_gass_api.models as models

    section = await client.job.structure.sections.shape_builder.post(
        models.SectionShapeBuilderCreate(
            name="360UB + plate",
            shapes=shape_builder.shapes(
                models.LibraryShape(library="Aust300", name="360 UB 44.7"),
                models.RectangularBarShape(d=16, b=250, anchor_position=...),
            )))

    for shape in shape_builder.shapes_of(section):   # typed SectionShape
        ...

Lives outside ``generated/`` so it survives Kiota's ``--clean-output``.
"""

from __future__ import annotations

import dataclasses
import re
from typing import Iterable, Optional, Union

from kiota_abstractions.serialization import ComposedTypeWrapper

from .generated.models.section import Section
from .generated.models.section_shape import SectionShape
from .generated.models.section_shape_builder_create import SectionShapeBuilderCreate
from .generated.models.section_shape_builder_create_shapes import SectionShapeBuilderCreate_shapes
from .generated.models.section_shapes import Section_shapes

__all__ = ["DISCRIMINATORS", "shapes", "shapes_of", "unwrap", "wrap"]

#: The ``shapeType`` discriminator for each shape class — mirrors the
#: ``SectionShape`` discriminator mapping in the OpenAPI spec.
DISCRIMINATORS: dict[str, str] = {
    "NotDefinedShape": "NotDefined",
    "CircularBarShape": "CircularBar",
    "SquareBarShape": "SquareBar",
    "RectangularBarShape": "RectangularBar",
    "CircularTubeShape": "CircularTube",
    "SquareTubeShape": "SquareTube",
    "RectangularTubeShape": "RectangularTube",
    "IShape": "IShape",
    "PlateWebGirderShape": "PlateWebGirder",
    "ChannelShape": "Channel",
    "BeamTeeShape": "BeamTee",
    "ColumnTeeShape": "ColumnTee",
    "EqualAngleShape": "EqualAngle",
    "UnequalAngleShape": "UnequalAngle",
    "CruciformShape": "Cruciform",
    "BoxGirderShape": "BoxGirder",
    "WedgeShape": "Wedge",
    "SliceShape": "Slice",
    "FilletShape": "Fillet",
    "PointsShape": "PointsShape",
    "LSBShape": "LSB",
    "LSBBackToBackShape": "LSBBackToBack",
    "LinesShape": "LinesShape",
    "TriangleShape": "Triangle",
    "CeeShape": "Cee",
    "ZedShape": "Zed",
    "TopHatShape": "TopHat",
    "DAShortShape": "DAShort",
    "DALongShape": "DALong",
    "DAStarredShape": "DAStarred",
    "PolygonShape": "Polygon",
    "PolygonTubeShape": "PolygonTube",
    "EquilateralTriangleShape": "EquilateralTriangle",
    "SchifflerizedAngleShape": "SchifflerizedAngle",
    "CeeBackToBackShape": "CeeBackToBack",
    "RoundedAngleShape": "RoundedAngle",
    "RackShape": "Rack",
    "LShape": "LShape",
    "TrapezoidShape": "Trapezoid",
    "FlatOvalShape": "FlatOval",
    "LibraryShape": "Library",
}

_OPTIONAL = re.compile(r"Optional\[(\w+)\]")


def _wrapper_fields(wrapper_cls: type) -> dict[str, str]:
    """Map shape class name -> wrapper attribute name, from the dataclass annotations."""
    out: dict[str, str] = {}
    for f in dataclasses.fields(wrapper_cls):
        m = _OPTIONAL.fullmatch(str(f.type))
        if m and m.group(1) in DISCRIMINATORS:
            out[m.group(1)] = f.name
    return out


def wrap(shape: SectionShape, wrapper_cls: type = SectionShapeBuilderCreate_shapes) -> ComposedTypeWrapper:
    """Wraps a shape in a Kiota composed-type wrapper, filling in ``shape_type`` if unset."""
    name = type(shape).__name__
    if name not in DISCRIMINATORS:
        raise TypeError(f"{name} is not a known SectionShape type")
    if shape.shape_type is None:
        shape.shape_type = DISCRIMINATORS[name]
    attr = _wrapper_fields(wrapper_cls).get(name)
    if attr is None:
        raise TypeError(f"{wrapper_cls.__name__} has no attribute for {name}")
    return wrapper_cls(**{attr: shape})


def unwrap(wrapper: ComposedTypeWrapper) -> Optional[SectionShape]:
    """Returns whichever shape a composed-type wrapper holds, or None if none."""
    for f in dataclasses.fields(wrapper):
        value = getattr(wrapper, f.name, None)
        if isinstance(value, SectionShape):
            return value
    return None


def shapes(*shapes_: SectionShape) -> list[SectionShapeBuilderCreate_shapes]:
    """Builds the ``shapes`` list for a ``SectionShapeBuilderCreate`` from plain shape objects."""
    return [wrap(s, SectionShapeBuilderCreate_shapes) for s in shapes_]


def shapes_of(source: Union[Section, SectionShapeBuilderCreate]) -> list[SectionShape]:
    """The typed shapes of a section (or shape-builder request), in order."""
    wrapped: Optional[Iterable[ComposedTypeWrapper]] = source.shapes
    return [s for s in (unwrap(w) for w in (wrapped or [])) if s is not None]
