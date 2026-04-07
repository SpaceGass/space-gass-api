using SpaceGassApi.Models;
using SpaceGassApi.Examples.Common;

// ---------------------------------------------------------------
// Example: Manage Sections and Materials
//
// Demonstrates how to:
//   1. Create a new blank SPACE GASS project
//   2. Create a user-defined material (structural steel)
//   3. Create a user-defined section (rectangular hollow section)
//   4. List all sections and materials
//   5. Update a section's properties
//   6. Create a member that uses the section and material
//   7. Delete a section
//
// Prerequisites:
//   - SPACE GASS API running locally (default: https://localhost:53483)
//   - A valid API key
// ---------------------------------------------------------------

var client = ApiClientFactory.Create();

try
{
    // -- Create a new blank project --------------------------------
    Console.WriteLine("Creating new blank project...");
    await client.Job.File.New.PostAsync();
    Console.WriteLine("New project created.");
    Console.WriteLine();

    // == MATERIALS =================================================

    // -- Create a structural steel material ------------------------
    Console.WriteLine("Creating materials...");

    var steel = await client.Job.Structure.Materials.PostAsync(
        new MaterialCreate
        {
            Name = "350 Grade Steel",
            YoungsModulus = 200000.0,    // MPa
            PoissonsRatio = 0.3,
            MassDensity = 7850.0,        // kg/m^3
            ThermalCoeff = 1.17e-5       // per degree C
        });
    Console.WriteLine($"  Material {steel?.Key}: {steel?.Name}");
    Console.WriteLine($"    Young's Modulus:  {steel?.YoungsModulus} MPa");
    Console.WriteLine($"    Poisson's Ratio:  {steel?.PoissonsRatio}");
    Console.WriteLine($"    Mass Density:     {steel?.MassDensity} kg/m^3");
    Console.WriteLine($"    Thermal Coeff:    {steel?.ThermalCoeff}");
    Console.WriteLine($"    Source:           {steel?.Source}");
    Console.WriteLine();

    // -- Create a concrete material --------------------------------
    var concrete = await client.Job.Structure.Materials.PostAsync(
        new MaterialCreate
        {
            Name = "40 MPa Concrete",
            YoungsModulus = 32800.0,     // MPa
            PoissonsRatio = 0.2,
            MassDensity = 2400.0,        // kg/m^3
            ThermalCoeff = 1.0e-5,
            ConcreteStrength = 40.0      // MPa
        });
    Console.WriteLine($"  Material {concrete?.Key}: {concrete?.Name}");
    Console.WriteLine($"    Concrete Strength: {concrete?.ConcreteStrength} MPa");
    Console.WriteLine();

    // == SECTIONS ==================================================

    // -- Create a rectangular hollow section (RHS) -----------------
    Console.WriteLine("Creating sections...");

    var rhs = await client.Job.Structure.Sections.PostAsync(
        new SectionCreate
        {
            Name = "200x100x6 RHS",
            Mark = "RHS",
            A = 3360.0,       // mm^2  - cross-sectional area
            J = 22.5e6,       // mm^4  - torsion constant
            Iy = 27.0e6,      // mm^4  - second moment of area (Y)
            Iz = 9.6e6,       // mm^4  - second moment of area (Z)
            Ay = 2400.0,      // mm^2  - shear area (Y)
            Az = 1200.0       // mm^2  - shear area (Z)
        });
    Console.WriteLine($"  Section {rhs?.Key}: {rhs?.Name}");
    Console.WriteLine($"    A  = {rhs?.A} mm^2");
    Console.WriteLine($"    Iy = {rhs?.Iy} mm^4");
    Console.WriteLine($"    Iz = {rhs?.Iz} mm^4");
    Console.WriteLine($"    Source: {rhs?.Source}");
    Console.WriteLine();

    // -- Create a second section (circular hollow) -----------------
    var chs = await client.Job.Structure.Sections.PostAsync(
        new SectionCreate
        {
            Name = "168.3x6 CHS",
            Mark = "CHS",
            A = 3060.0,       // mm^2
            J = 13.5e6,       // mm^4
            Iy = 6.75e6,      // mm^4
            Iz = 6.75e6,      // mm^4
            Ay = 1530.0,      // mm^2
            Az = 1530.0       // mm^2
        });
    Console.WriteLine($"  Section {chs?.Key}: {chs?.Name}");
    Console.WriteLine();

    // == LIST ======================================================

    // -- List all materials ----------------------------------------
    Console.WriteLine("Listing all materials...");
    var materials = await client.Job.Structure.Materials.GetAsync();
    foreach (var mat in materials!)
    {
        Console.WriteLine($"  [{mat.Key}] {mat.Name} (E={mat.YoungsModulus}, Source={mat.Source})");
    }
    Console.WriteLine();

    // -- List all sections -----------------------------------------
    Console.WriteLine("Listing all sections...");
    var sections = await client.Job.Structure.Sections.GetAsync();
    foreach (var sec in sections!)
    {
        Console.WriteLine($"  [{sec.Key}] {sec.Name} (A={sec.A}, Iy={sec.Iy}, Source={sec.Source})");
    }
    Console.WriteLine();

    // == UPDATE ====================================================

    // -- Update the RHS section's area (partial update) ------------
    Console.WriteLine($"Updating section {rhs?.Key} area...");
    var updated = await client.Job.Structure.Sections[rhs!.Key!.Value].PatchAsync(
        new SectionUpdate
        {
            A = 3500.0,       // Increased area
            Name = "200x100x6.3 RHS"
        });
    Console.WriteLine($"  Section {updated?.Key}: {updated?.Name}");
    Console.WriteLine($"    A  = {updated?.A} mm^2 (was {rhs.A})");
    Console.WriteLine();

    // == CREATE MEMBER USING SECTION & MATERIAL ====================

    // -- Create nodes and a member that references our properties --
    Console.WriteLine("Creating a beam using the new section and material...");

    var nodeA = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 0.0, Y = 0.0, Z = 0.0 });
    var nodeB = await client.Job.Structure.Nodes.PostAsync(
        new NodeCreate { X = 5.0, Y = 0.0, Z = 0.0 });

    var member = await client.Job.Structure.Members.PostAsync(
        new MemberCreate
        {
            NodeA = nodeA!.Key!.Value,
            NodeB = nodeB!.Key!.Value,
            Section = rhs.Key.Value,
            Material = steel!.Key!.Value
        });
    Console.WriteLine($"  Member {member?.Key}: Node {member?.NodeA} -> Node {member?.NodeB}");
    Console.WriteLine($"    Section:  {member?.Section}");
    Console.WriteLine($"    Material: {member?.Material}");
    Console.WriteLine();

    // == DELETE =====================================================

    // -- Delete the unused CHS section -----------------------------
    Console.WriteLine($"Deleting unused section {chs?.Key} ({chs?.Name})...");
    await client.Job.Structure.Sections[chs!.Key!.Value].DeleteAsync();
    Console.WriteLine("  Deleted.");
    Console.WriteLine();

    // -- Verify deletion -------------------------------------------
    Console.WriteLine("Remaining sections:");
    var remaining = await client.Job.Structure.Sections.GetAsync();
    foreach (var sec in remaining!)
    {
        Console.WriteLine($"  [{sec.Key}] {sec.Name}");
    }
    Console.WriteLine();

    // == SUMMARY ===================================================
    Console.WriteLine("Example completed successfully!");
    Console.WriteLine($"  Materials created: {steel.Key} ({steel.Name}), {concrete?.Key} ({concrete?.Name})");
    Console.WriteLine($"  Sections created:  {rhs.Key} ({updated?.Name})");
    Console.WriteLine($"  Members created:   {member?.Key}");

    // -- Close without saving (example only) -----------------------
    Console.WriteLine();
    Console.WriteLine("Closing project (not saving)...");
    await client.Job.Close.PostAsync();
    Console.WriteLine("Done.");
}
catch (Exception ex)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.Error.WriteLine($"Error: {ex.Message}");
    Console.ResetColor();
    return 1;
}

return 0;
