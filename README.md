# warp-- `warp_bubble_shape_catalog.tex`  
  LaTeX source with each shape function's formula, a note on support size, and free parameters.
- `scripts/`  
  Python scripts for plotting profiles, generating numeric data, computing support sizes, and exporting CSV.
- `data/`  
  Supporting data or plots illustrating each profile.
- `docs/`  
  Jekyll documentation site with detailed mathematical descriptions, script documentation, and visualizations.

## Documentation

A comprehensive Jekyll documentation site is available at:  
**https://arcticoder.github.io/warp-bubble-shape-catalog/**

The documentation includes:
- **Profiles**: Detailed mathematical descriptions of each warp-bubble shape function
- **Scripts**: Complete documentation of all Python utilities with usage examples
- **Visuals**: Generated plots and visualizations of the profile functions

*Created: May 29, 2025*

## Scriptsshape-catalog

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
  Generate publication-quality plots of warp-bubble shape functions for visualization and analysis. Features configurable plot parameters, automatic high-DPI saving, and optional interactive display with command-line flags.
- **generate_profile_data.py**  
  Generate high-resolution numeric data for all warp-bubble profiles and save in compressed binary format for efficient storage and loading.
- **compute_support_size.py**  
  Estimate practical support sizes for each profile function given a specified threshold value. Provides console output with clear formatting.
- **export_profiles_csv.py**  
  Export profile data to human-readable CSV format for analysis in external tools, spreadsheet applications, or other programming languages.

### Usage Examples

1. **Plot profiles with interactive display**  
   ```bash
   # Default: Interactive display + save plot
   python scripts/plot_profiles.py
   
   # Interactive display only (no file saved)
   python scripts/plot_profiles.py --interactive
   python scripts/plot_profiles.py -i
   
   # Save plot only (no interactive display)
   python scripts/plot_profiles.py --save-only
   python scripts/plot_profiles.py -s
   
   # Both interactive display and save plot
   python scripts/plot_profiles.py --both
   python scripts/plot_profiles.py -b
   ```
   The interactive display allows you to zoom, pan, and explore the plot data. Saved plots go to `data/plots/profiles.png` in high-resolution PNG format (300 DPI).

2. **Generate numeric data**  
   ```bash
   python scripts/generate_profile_data.py
   ```
   Creates `data/profiles.npz` with high-resolution $(r, f(r))$ values for all profiles.

3. **Compute support sizes**  
   ```bash
   python scripts/compute_support_size.py
   ```
   Analyzes where each profile function falls below a threshold (default: $10^{-3}$) and reports practical support sizes.

4. **Export to CSV**  
   ```bash
   python scripts/export_profiles_csv.py
   ```
   Creates `data/profile_data.csv` in human-readable format for use in Excel, MATLAB, R, or other analysis tools.

## Dependencies

All scripts require:
- **NumPy**: Numerical computations
- **Matplotlib**: Plotting (plot_profiles.py only)

Install dependencies:
```bash
pip install numpy matplotlib
```

## Common Workflow

1. **Generate all data and visualizations:**
   ```bash
   python scripts/generate_profile_data.py
   python scripts/export_profiles_csv.py
   python scripts/plot_profiles.py
   ```

2. **Analyze profile properties:**
   ```bash
   python scripts/compute_support_size.py
   ```

3. **Verify output files:**
   - `data/profiles.npz` (binary data)
   - `data/profile_data.csv` (CSV data)  
   - `data/plots/profiles.png` (visualization)

## Building the LaTeX Catalog

After cloning the repo, build the PDF:

```bash
pdflatex warp_bubble_shape_catalog.tex
```

## Dependency

This catalog is a dependency for the next repository, which will specify the coordinate system and symmetry assumptions for the metric ansatz:

> “A specification of the chosen coordinate system (e.g. spherical coordinates $(t,r,\theta,\phi)$) plus the symmetry assumptions (e.g. axial symmetry about the $z$–axis, compact support in $r$) that simplify the metric ansatz.”

Include this repo as a submodule or reference in your downstream project’s documentation.
