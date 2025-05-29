# warp-bubble-shape-catalog

**Catalog of candidate warp‐bubble shape functions**  
This repository collects the defining formulas, support sizes, and key free parameters for a variety of warp‐bubble “shape” profiles (e.g. Alcubierre’s tanh‐based profile, Natário’s smooth Gaussian variant, …).

## Contents

- `warp_bubble_shape_catalog.tex`  
  LaTeX source with each shape function’s formula, a note on support size, and free parameters.
- `scripts/`  
  Python scripts for plotting profiles, generating numeric data, computing support sizes, and exporting CSV.
- `data/`  
  Supporting data or plots illustrating each profile.
## Scripts

All Python scripts reside in the `scripts/` folder:

- **plot_profiles.py**  
  Plot warp-bubble shape functions (Alcubierre, Natário) for visualization. Saves plots to `data/plots/profiles.png`.
- **generate_profile_data.py**  
  Generate numeric data for warp-bubble profiles and save to compressed NumPy files.
- **compute_support_size.py**  
  Estimate practical support sizes for profiles given a threshold.
- **export_profiles_csv.py**  
  Export profile data to CSV in the `data/` folder for further analysis.

### Usage Examples

1. **Plot profiles**  
   ```bash
   python scripts/plot_profiles.py
   ```
   This will save a plot to `data/plots/profiles.png` and display it interactively.

2. **Generate data**  
   ```bash
   python scripts/generate_profile_data.py
   ```

3. **Compute support sizes**  
   ```bash
   python scripts/compute_support_size.py
   ```

4. **Export to CSV**  
   ```bash
   python scripts/export_profiles_csv.py
   ```
   This will create `data/profile_data.csv`.

## Building the LaTeX Catalog

After cloning the repo, build the PDF:

```bash
pdflatex warp_bubble_shape_catalog.tex
```

## Dependency

This catalog is a dependency for the next repository, which will specify the coordinate system and symmetry assumptions for the metric ansatz:

> “A specification of the chosen coordinate system (e.g. spherical coordinates $(t,r,\theta,\phi)$) plus the symmetry assumptions (e.g. axial symmetry about the $z$–axis, compact support in $r$) that simplify the metric ansatz.”

Include this repo as a submodule or reference in your downstream project’s documentation.
