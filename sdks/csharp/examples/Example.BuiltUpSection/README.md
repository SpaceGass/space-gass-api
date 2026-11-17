# Example.BuiltUpSection

Backs the [Create a shape builder section recipe](https://api.spacegass.com/docs/examples/create-shape-builder-section). Creates a built-up (shape-builder) section — a 360 UB 44.7 with a 250 x 16 cover plate welded to its top flange — and applies it to a simply-supported beam. Shows the preview endpoint (geometry and numbered reference points without writing anything), anchoring one shape onto another, the computed section properties against the plain UB, and reading the shapes back.

Shapes are plain objects in a list (`Shapes = [new LibraryShape { ... }, new RectangularBarShape { ... }]`) and come back as their own classes.

## Run it

1. Start the SPACE GASS API service.
2. From this folder:
   ```
   dotnet run
   ```

The example saves the model to `Desktop/SpaceGass Examples/BuiltUpSection.sg` so you can open it in SPACE GASS Desktop and view the section.
