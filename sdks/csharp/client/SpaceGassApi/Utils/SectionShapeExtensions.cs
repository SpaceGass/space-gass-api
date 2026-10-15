using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Microsoft.Kiota.Abstractions.Serialization;
using SpaceGassApi.Models;

// ---------------------------------------------------------------------
// Hand-maintained smoothing over the shape-builder (built-up section)
// surface.
//
// A section's shapes are polymorphic (`shapeType` discriminator), so the
// spec models them as a oneOf and Kiota wraps each list element in a
// composed type with one property per shape type:
//
//   SectionShapeBuilderCreate.SectionShapeBuilderCreate_shapes   (request)
//   Section.Section_shapes                                        (response)
//
// Raw usage means `new SectionShapeBuilderCreate_shapes { LibraryShape =
// new LibraryShape { ShapeType = "Library", ... } }` per shape. The
// implicit conversion below lets callers list the shapes directly, with
// the discriminator filled in:
//
//   await client.Job.Structure.Sections.ShapeBuilder.PostAsync(
//       new SectionShapeBuilderCreate
//       {
//           Name = "360UB + plate",
//           Shapes =
//           [
//               new LibraryShape { Library = "Aust300", Name = "360 UB 44.7" },
//               new RectangularBarShape { D = 16, B = 250, AnchorPosition = ... },
//           ],
//       });
//
//   foreach (var shape in section.GetShapes()) { ... }   // typed SectionShape
//
// Lives in Utils/ so it survives Kiota's --clean-output.
// ---------------------------------------------------------------------

namespace SpaceGassApi.Models
{
    public partial class SectionShapeBuilderCreate
    {
        public partial class SectionShapeBuilderCreate_shapes
        {
            /// <summary>Wraps any <see cref="SectionShape"/> subclass as a shape-builder list element.</summary>
            public static implicit operator SectionShapeBuilderCreate_shapes(SectionShape shape)
                => SectionShapeExtensions.Wrap<SectionShapeBuilderCreate_shapes>(shape);
        }
    }
}

namespace SpaceGassApi
{
    /// <summary>
    /// Helpers for the polymorphic shape lists on shape-builder sections.
    /// </summary>
    public static class SectionShapeExtensions
    {
        /// <summary>
        /// The <c>shapeType</c> discriminator for each shape class — mirrors the
        /// <c>SectionShape</c> discriminator mapping in the OpenAPI spec.
        /// </summary>
        public static readonly IReadOnlyDictionary<Type, string> Discriminators = new Dictionary<Type, string>
        {
            [typeof(NotDefinedShape)] = "NotDefined",
            [typeof(CircularBarShape)] = "CircularBar",
            [typeof(SquareBarShape)] = "SquareBar",
            [typeof(RectangularBarShape)] = "RectangularBar",
            [typeof(CircularTubeShape)] = "CircularTube",
            [typeof(SquareTubeShape)] = "SquareTube",
            [typeof(RectangularTubeShape)] = "RectangularTube",
            [typeof(IShape)] = "IShape",
            [typeof(PlateWebGirderShape)] = "PlateWebGirder",
            [typeof(ChannelShape)] = "Channel",
            [typeof(BeamTeeShape)] = "BeamTee",
            [typeof(ColumnTeeShape)] = "ColumnTee",
            [typeof(EqualAngleShape)] = "EqualAngle",
            [typeof(UnequalAngleShape)] = "UnequalAngle",
            [typeof(CruciformShape)] = "Cruciform",
            [typeof(BoxGirderShape)] = "BoxGirder",
            [typeof(WedgeShape)] = "Wedge",
            [typeof(SliceShape)] = "Slice",
            [typeof(FilletShape)] = "Fillet",
            [typeof(PointsShape)] = "PointsShape",
            [typeof(LSBShape)] = "LSB",
            [typeof(LSBBackToBackShape)] = "LSBBackToBack",
            [typeof(LinesShape)] = "LinesShape",
            [typeof(TriangleShape)] = "Triangle",
            [typeof(CeeShape)] = "Cee",
            [typeof(ZedShape)] = "Zed",
            [typeof(TopHatShape)] = "TopHat",
            [typeof(DAShortShape)] = "DAShort",
            [typeof(DALongShape)] = "DALong",
            [typeof(DAStarredShape)] = "DAStarred",
            [typeof(PolygonShape)] = "Polygon",
            [typeof(PolygonTubeShape)] = "PolygonTube",
            [typeof(EquilateralTriangleShape)] = "EquilateralTriangle",
            [typeof(SchifflerizedAngleShape)] = "SchifflerizedAngle",
            [typeof(CeeBackToBackShape)] = "CeeBackToBack",
            [typeof(RoundedAngleShape)] = "RoundedAngle",
            [typeof(RackShape)] = "Rack",
            [typeof(LShape)] = "LShape",
            [typeof(TrapezoidShape)] = "Trapezoid",
            [typeof(FlatOvalShape)] = "FlatOval",
            [typeof(LibraryShape)] = "Library",
        };

        /// <summary>
        /// Wraps a shape in a Kiota composed-type wrapper. The wrapper's property for
        /// the shape is the one named after the shape's class (Kiota's convention).
        /// Fills in <see cref="SectionShape.ShapeType"/> when the caller didn't.
        /// </summary>
        public static TWrapper Wrap<TWrapper>(SectionShape shape) where TWrapper : IComposedTypeWrapper, new()
        {
            if (shape == null) throw new ArgumentNullException(nameof(shape));
            var type = shape.GetType();
            if (!Discriminators.TryGetValue(type, out var discriminator))
                throw new ArgumentException($"{type.Name} is not a known SectionShape type.", nameof(shape));

            shape.ShapeType ??= discriminator;

            var property = typeof(TWrapper).GetProperty(type.Name, BindingFlags.Public | BindingFlags.Instance)
                ?? throw new InvalidOperationException($"{typeof(TWrapper).Name} has no {type.Name} property.");

            var wrapper = new TWrapper();
            property.SetValue(wrapper, shape);
            return wrapper;
        }

        /// <summary>Returns whichever shape a composed-type wrapper holds, or null if none.</summary>
        public static SectionShape? Unwrap(IComposedTypeWrapper wrapper)
            => wrapper.GetType()
                .GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => typeof(SectionShape).IsAssignableFrom(p.PropertyType))
                .Select(p => p.GetValue(wrapper) as SectionShape)
                .FirstOrDefault(s => s != null);

        /// <summary>The typed shapes of a section, in order (empty when the section has none).</summary>
        public static IEnumerable<SectionShape> GetShapes(this Section section)
            => section.Shapes?.Select(Unwrap).Where(s => s != null).Select(s => s!) ?? Enumerable.Empty<SectionShape>();

        /// <summary>The typed shapes of a shape-builder request, in order.</summary>
        public static IEnumerable<SectionShape> GetShapes(this SectionShapeBuilderCreate request)
            => request.Shapes?.Select(Unwrap).Where(s => s != null).Select(s => s!) ?? Enumerable.Empty<SectionShape>();
    }
}
