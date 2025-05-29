# warp-bubble-shape-catalog

**Catalog of candidate warp‐bubble shape functions**  
This repository collects the defining formulas, support sizes, and key free parameters for a variety of warp‐bubble “shape” profiles (e.g. Alcubierre’s tanh‐based profile, Natário’s smooth Gaussian variant, …).

## Contents

- `warp_bubble_shape_catalog.tex`  
  LaTeX source with each shape function’s formula, a note on support size, and free parameters.
- `data/`  
  Supporting data or plots illustrating each profile.

## Usage

1. Clone the repo:  
   ```bash
   git clone https://github.com/arcticoder/warp-bubble-shape-catalog.git
   cd warp-bubble-shape-catalog
   ```
2. Build the PDF:  
   ```bash
   pdflatex warp_bubble_shape_catalog.tex
   ```

## Dependency

This catalog is a dependency for the next repository, which will specify the coordinate system and symmetry assumptions for the metric ansatz:

> “A specification of the chosen coordinate system (e.g. spherical coordinates $(t,r,\theta,\phi)$) plus the symmetry assumptions (e.g. axial symmetry about the $z$–axis, compact support in $r$) that simplify the metric ansatz.”

Include this repo as a submodule or reference in your downstream project’s documentation.
