# Example.GrillageMovingLoad

Builds a 3-span, 2-lane bridge grillage and runs an AS 5100 style **T44 moving-load** analysis — a worked demonstration of the moving-load API (vehicle library import, travel paths, scenario, generation) on a realistic deck model.

## What it does

1. Creates a new job **from a template** (`GrillageTemplate.sgbase`) via `POST /job/new-from-template`. The template supplies the girder + concrete deck-slab sections, their materials, and a self-weight load case — none of which the API can create yet. The template file itself is never modified.
2. Prints + maps the sections, materials and primary load cases the template provides.
3. Builds the grid (bulk): 5 longitudinal girders × transverse deck strips at 1 m.
4. Restrains the bearing lines (abutment 1 fixed, piers + abutment 2 guided).
5. Applies a superimposed-dead-load (wearing surface) UDL on the deck strips.
6. Rolls the permanent loads into a single **Total Dead Load** combination (self-weight + SDL) — the moving-load scenario combines with this one case.
7. Sets up and generates the **T44 moving load** across both lanes.
8. Creates selection filters for the grillage member types.
9. Saves, runs a linear static analysis, and reports the peak girder moment from the T44 envelope.

## What the template provides

| | Id | Used for |
|---|---|---|
| Section | 1 — Bridge Girder (steel WB) | longitudinal girders |
| Section | 2 — 1.0 m deck slab strip | interior transverse strips |
| Section | 3 — 0.5 m deck slab strip | end transverse strips (first/last lines) |
| Material | 1 — STEEL | girders |
| Material | 2 — Concrete | deck strips |
| Load case | self-weight (first primary case) | the permanent `G` combination |

The example references these by Id (pinned as constants at the top of `Program.cs`) — everything else (grid, members, supports, SDL, moving loads, filters) is built through the API.

## Geometry

| | |
|---|---|
| Spans | 3 × 20 m (60 m total) |
| Girders | 5 @ 1.75 m c/c → 7.0 m deck (two 3.5 m lanes) |
| Deck strips | transverse, every 1.0 m |
| Travel paths | along girder 2 (Z = 1.75 m) and girder 4 (Z = 5.25 m) — one per lane |

All geometry is parameterised at the top of `Program.cs` — change the spans, girder layout or strip spacing in one place.

## Selection filters created

- **Girders (WB)** — section 1
- **Deck slab strips** — sections 2 & 3
- **Bridge supports** — the restrained bearing nodes

## Prerequisites

- SPACE GASS API running locally (default `http://localhost:34560`).
- `Australia` vehicle library installed (for T44).
- `GrillageTemplate.sgbase` next to the built exe — the `.csproj` copies it from this folder automatically.

## Assumptions you may need to adjust

These are pinned in `Program.cs` with comments; the console printout on first run shows the actual template contents to check against:

- **Template Ids** — sections 1/2/3 = girder / 1 m strip / 0.5 m strip, materials 1/2 = STEEL / Concrete, self-weight = first primary case.
- **Vehicle name** — `T44-3` is imported from `Australia`; the item name must exist in that library (the OpenAPI spec documents `T44`).
- **Load factors** — `1.2 G + 1.5 live`, dynamic load allowance `1.3`, lane factor `1.0`. Set these per AS 5100 for real work.

## Run

```bash
dotnet run --project Example.GrillageMovingLoad
```
