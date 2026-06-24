# grillage_moving_load

Python port of the C# `Example.GrillageMovingLoad`. Builds a 3-span, 2-lane bridge grillage and runs an AS 5100 style **T44 moving-load** analysis — a worked demonstration of the moving-load API (vehicle library import, travel paths, scenario, generation) on a realistic deck model.

## What it does

1. Creates a new job **from a template** (`GrillageTemplate.sgbase`) via `POST /job/new-from-template` (using the `NewFromTemplateRequest` helper). The template supplies the girder + concrete deck-slab sections, their materials, and a self-weight load case — none of which the API can create yet. The template file itself is never modified.
2. Prints + maps the sections, materials and primary load cases the template provides.
3. Builds the grid (bulk): 5 longitudinal girders × transverse deck strips at 1 m.
4. Restrains the bearing lines (abutment 1 fixed, piers + abutment 2 guided).
5. Applies a superimposed-dead-load (wearing surface) UDL on the deck strips.
6. Rolls the permanent loads into a single **Total Dead Load** combination (self-weight + SDL).
7. Sets up and generates the **T44 moving load** across both lanes (printing the imported wheel layout).
8. Creates selection filters for the grillage member types.
9. Saves, runs a linear static analysis, and reports the peak girder moment from the T44 envelope.

## What the template provides

| | Id | Used for |
|---|---|---|
| Section | 1 — Bridge Girder (steel WB) | longitudinal girders |
| Section | 2 — 1.0 m deck slab strip | interior transverse strips |
| Section | 3 — 0.5 m deck slab strip | end transverse strips |
| Material | 1 — STEEL | girders |
| Material | 2 — Concrete | deck strips |
| Load case | self-weight (first primary case) | the Total Dead Load combination |

## Prerequisites

- SPACE GASS API running locally (default `http://localhost:34560`).
- `Australia` vehicle library installed (for T44).
- `GrillageTemplate.sgbase` in this folder (uploaded via new-from-template).

## Run

```bash
pip install -e ../../client      # once, to resolve the local SDK
python grillage_moving_load.py
```

See the C# [`Example.GrillageMovingLoad`](../../../csharp/examples/Example.GrillageMovingLoad/README.md) for the full design notes (geometry, travel paths on girders 2 & 4, assumptions). This is a direct port.
