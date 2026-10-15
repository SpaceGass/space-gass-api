using SpaceGassApi;
using SpaceGassApi.Models;


// ---------------------------------------------------------------
// Example: Create a Built-up Section with the Shape Builder
//
// Builds a compound section — a 360 UB 44.7 with a 250 x 16 cover
// plate welded to its top flange — and applies it to a simply-supported
// beam:
//   1.  Create the client and a new project
//   2.  Nodes, restraints and material for a 6 m beam
//   3.  Preview the bare UB to see its numbered reference points
//   4.  Define the plate, anchored onto the UB's top-centre point
//   5.  Preview the compound section (nothing is written yet)
//   6.  Create the section — SPACE GASS computes A, J, Iy, Iz
//   7.  Compare with the plain library UB
//   8.  Create the beam member on the built-up section
//   9.  Read the section back and list its shapes
//   10. Save and close
//
// Shape-builder sections hold up to 20 shapes. A shape is either drawn
// from dimensions (IShape, RectangularBar, Channel, ...) or taken from
// a section library (LibraryShape). Dimensions and translations are in
// the job's section-properties unit (mm by default); see GET /job/units.
//
// Prerequisites:
//   - SPACE GASS API running locally (default: http://localhost:34560)
//   - The "Aust300" section library installed (default in SPACE GASS)
// ---------------------------------------------------------------

// -- Configuration ------------------------------------------------
var saveFilePath = Path.Combine(
    Environment.GetFolderPath(Environment.SpecialFolder.Desktop),
    "SpaceGass Examples",
    "BuiltUpSection.sg");

var client = SpaceGassApiClient.CreateClient("http://localhost:34560");

try
{
    // == Step 1 — Create a new blank project =======================
    Console.WriteLine("Creating new blank project...");
    await client.Job.New.PostAsync();

    var units = await client.Job.Units.GetAsync();
    Console.WriteLine($"  Section dimensions are in {units!.SectionProperties}.");
    Console.WriteLine();

    // == Step 2 — Nodes, restraints and material ===================
    Console.WriteLine("Creating nodes, restraints and material...");

    var node1 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    var node2 = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 6.0, Y = 0.0, Z = 0.0 });

    await client.Job.Structure.NodeRestraints.PostAsync(
        new NodeRestraintCreate { Node = node1!.Id, RestraintCode = "FFFFFF" });
    await client.Job.Structure.NodeRestraints.PostAsync(
        new NodeRestraintCreate { Node = node2!.Id, RestraintCode = "FFFRRR" });

    var steel = await client.Job.Structure.Materials.Library.PostAsync(
        new MaterialLibraryCreate { Library = "Aust", Name = "STEEL" });
    Console.WriteLine();

    // == Step 3 — Preview the bare UB ==============================
    // The preview endpoint computes the geometry a shape-builder body
    // would produce without writing anything. Each shape comes back
    // with its extent and numbered reference points — the points an
    // AnchorPosition refers to when snapping shapes together.
    //
    // The SDK's SectionShapeExtensions let you list SectionShape objects
    // directly in Shapes; Kiota's per-shape wrapper and the ShapeType
    // discriminator are handled for you.
    Console.WriteLine("Previewing the bare 360 UB 44.7...");
    var ub = new LibraryShape { Library = "Aust300", Name = "360 UB 44.7" };

    var ubPreview = await client.Job.Structure.Sections.ShapeBuilder.Preview.PostAsync(
        new SectionShapeBuilderCreate { Name = "UB only", Shapes = [ub] });

    var ubGeometry = ubPreview!.Shapes!.First();
    Console.WriteLine($"  Depth {ubGeometry.Bounds!.MinY} .. {ubGeometry.Bounds.MaxY}, " +
                      $"width {ubGeometry.Bounds.MinZ} .. {ubGeometry.Bounds.MaxZ}");
    Console.WriteLine("  Reference points (point: y, z):");
    foreach (var p in ubGeometry.ReferencePoints!.Take(5))
    {
        Console.WriteLine($"    {p.Point}: {p.Y}, {p.Z}");
    }
    Console.WriteLine("    ...");

    // Point 1 is the centroid; points 2-5 are the top, right, bottom and
    // left mid-edges. Pick the top-centre point by its geometry rather
    // than assuming a number.
    var ubTopCentre = ubGeometry.ReferencePoints!
        .Where(p => p.Z == 0)
        .OrderByDescending(p => p.Y)
        .First();
    Console.WriteLine($"  Top-centre of the UB is reference point {ubTopCentre.Point}.");
    Console.WriteLine();

    // == Step 4 — Define the cover plate ===========================
    // A 250 wide x 16 thick plate. Its bottom-centre point (4) snaps
    // onto the UB's top-centre point, so it sits flush on the flange.
    // AnchorPosition is input-only: the API converts it to
    // TranslateY / TranslateZ, which is what you get back.
    Console.WriteLine("Defining the 250 x 16 cover plate...");
    var plate = new RectangularBarShape
    {
        D = 16.0,
        B = 250.0,
        Fabrication = ShapeFabrication.Heavily_Welded,
        AnchorPosition = new ShapeAnchorPosition
        {
            AnchorShape = 1,                      // the UB (one-based position in Shapes)
            AnchorPoint = ubTopCentre.Point,      // ... its top-centre point
            ShapePoint = 4,                       // the plate's bottom-centre point
        },
    };
    Console.WriteLine();

    // == Step 5 — Preview the compound section =====================
    var request = new SectionShapeBuilderCreate
    {
        Name = "360 UB 44.7 + 250x16 plate",
        Mark = "B1",
        Shapes = [ub, plate],
    };

    Console.WriteLine("Previewing the compound section...");
    var preview = await client.Job.Structure.Sections.ShapeBuilder.Preview.PostAsync(request);
    Console.WriteLine($"  Overall depth {preview!.Bounds!.MaxY - preview.Bounds.MinY}, " +
                      $"width {preview.Bounds.MaxZ - preview.Bounds.MinZ}");
    foreach (var s in preview.Shapes!)
    {
        Console.WriteLine($"  Shape {s.Shape}: y {s.Bounds!.MinY:F1} .. {s.Bounds.MaxY:F1}");
    }
    Console.WriteLine();

    // == Step 6 — Create the section ===============================
    // Same body as the preview. SPACE GASS computes the structural
    // properties from the shapes — the caller never supplies them.
    Console.WriteLine("Creating the built-up section...");
    var builtUp = await client.Job.Structure.Sections.ShapeBuilder.PostAsync(request);
    Console.WriteLine($"  Section {builtUp!.Id}: {builtUp.Name} ({builtUp.ShapeCount} shapes)");
    Console.WriteLine();

    // == Step 7 — Compare with the plain UB ========================
    var plainUb = await client.Job.Structure.Sections.Library.PostAsync(
        new SectionLibraryCreate { Library = "Aust300", Name = "360 UB 44.7", Mark = "B0" });

    Console.WriteLine($"  {"Property",-10} {"360 UB 44.7",14} {"UB + plate",14}");
    Console.WriteLine($"  {"A",-10} {plainUb!.A,14:F0} {builtUp.A,14:F0}");
    Console.WriteLine($"  {"Iy",-10} {plainUb.Iy,14:E3} {builtUp.Iy,14:E3}");
    Console.WriteLine($"  {"Iz",-10} {plainUb.Iz,14:E3} {builtUp.Iz,14:E3}");
    Console.WriteLine($"  {"J",-10} {plainUb.J,14:E3} {builtUp.J,14:E3}");
    Console.WriteLine();

    // == Step 8 — Create the beam member ===========================
    Console.WriteLine("Creating beam member on the built-up section...");
    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = node1.Id,
            NodeB = node2.Id,
            Section = builtUp.Id,
            Material = steel!.Id,
        });
    Console.WriteLine($"  Member {member!.Id}: section {member.Section}");
    Console.WriteLine();

    // == Step 9 — Read the section back ============================
    // GET /sections/{id} expands the shapes by default. GetShapes()
    // unwraps them to typed SectionShape objects.
    Console.WriteLine("Reading the section back...");
    var saved = await client.Job.Structure.Sections[builtUp.Id!.Value].GetAsync();
    foreach (var shape in saved!.GetShapes())
    {
        // A LibraryShape is resolved on create: it comes back as the
        // concrete shape (here an IShape) carrying the library item's name.
        var detail = shape switch
        {
            IShape i => $"{i.D} deep x {i.Bt} wide",
            RectangularBarShape bar => $"{bar.B} x {bar.D}",
            _ => "",
        };
        Console.WriteLine($"  Shape {shape.Id}: {shape.ShapeType,-15} {shape.ShapeName,-14} {detail,-20} " +
                          $"translateY={shape.TranslateY} translateZ={shape.TranslateZ}");
    }
    Console.WriteLine();

    // == Step 10 — Save and close ==================================
    Console.WriteLine($"Saving model to: {saveFilePath}");
    await client.Job.Save.PostAsync(new SaveJobRequest { FilePath = saveFilePath });
    Console.WriteLine("Project saved.");
}
catch (ErrorResponse err)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"API error {err.Status}: {err.Title}");
    if (!string.IsNullOrWhiteSpace(err.Detail))
        Console.Error.WriteLine($"  {err.Detail}");
    if (!string.IsNullOrWhiteSpace(err.ErrorCode))
        Console.Error.WriteLine($"  Code: {err.ErrorCode}");
    foreach (var ve in err.Errors ?? [])
        Console.Error.WriteLine($"  [{ve.Field}] {ve.Message}");
    Console.ResetColor();
    return 1;
}
catch (Exception ex)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"Error: {ex.Message}");
    Console.ResetColor();
    return 1;
}
finally
{
    // Always close the active job so the next run starts clean.
    try
    {
        Console.WriteLine("Closing project...");
        await client.Job.Close.PostAsync();
        Console.WriteLine("Project closed.");
    }
    catch (Exception closeEx)
    {
        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.Error.WriteLine($"Warning: failed to close job: {closeEx.Message}");
        Console.ResetColor();
    }
}

return 0;
