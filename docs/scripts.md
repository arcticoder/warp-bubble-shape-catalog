---
layout: default
title: Scripts Documentation
date: 2025-05-29
---

# Python Scripts

The `scripts/` folder contains Python utilities for computation, visualization, and data export of warp-bubble shape profiles. All scripts are designed to work independently or as part of a larger analysis pipeline.

## Overview

| Script | Purpose | Output |
|--------|---------|--------|
| `plot_profiles.py` | Visualization and plotting | PNG plots |
| `generate_profile_data.py` | Numeric data generation | NumPy `.npz` files |
| `compute_support_size.py` | Support size analysis | Console output |
| `export_profiles_csv.py` | Data export | CSV files |

---

## plot_profiles.py

**Purpose**: Generate publication-quality plots of warp-bubble shape functions for visualization and analysis.

### Features
- Plots multiple profiles on the same axes for comparison
- Configurable plot parameters (range, resolution, styling)
- Automatic plot saving with high DPI for publications
- **Optional interactive display**: Use command-line flags to control whether plots are displayed interactively, saved to file, or both

### Usage
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

### Functions
- `alcubierre_profile(r, R=1.0, sigma=10.0)`: Compute Alcubierre profile values
- `nataro_gaussian(r, alpha=1.0)`: Compute Natário Gaussian profile values
- `plot_profiles(r_max=3.0, num=500, save_plot=True, show_plot=False)`: Main plotting function

### Default Parameters
- **Range**: $r \in [0, 3]$
- **Resolution**: 500 points
- **Alcubierre**: $R=1.0$, $\sigma=10.0$
- **Natário**: $\alpha=1.0$

### Interactive Display Options
The script supports multiple display modes:
- **Default**: Shows interactive plot window and saves to file
- **Interactive only** (`-i`): Opens plot in interactive window for exploration (zoom, pan, etc.)
- **Save only** (`-s`): Generates plot file without opening display window
- **Both** (`-b`): Explicitly enables both interactive display and file saving

The interactive display uses matplotlib backends (Qt5Agg or TkAgg) and allows you to:
- Zoom and pan the plot
- Examine specific data points
- Export the plot in different formats through the matplotlib interface

### Output
- **File**: `data/plots/profiles.png`
- **Format**: High-resolution PNG (300 DPI)
- **Size**: Optimized for inclusion in documents

---

## generate_profile_data.py

**Purpose**: Generate high-resolution numeric data for all warp-bubble profiles and save in compressed binary format for efficient storage and loading.

### Features
- High-resolution sampling of profile functions
- Compressed NumPy storage format
- Automatic directory creation
- Configurable resolution and range

### Usage
```bash
python scripts/generate_profile_data.py
```

### Functions
- `generate_data(r_max=3.0, num=500, output_dir='data')`: Main data generation function

### Default Parameters
- **Range**: $r \in [0, 3]$
- **Resolution**: 500 points
- **Output**: `data/profiles.npz`

### Output Format
The generated `.npz` file contains:
```python
{
    'r': array([0.0, 0.006, 0.012, ...]),           # r coordinates
    'alcubierre': array([0.0, 0.001, 0.005, ...]), # Alcubierre values
    'natario': array([1.0, 0.999, 0.998, ...])     # Natário values
}
```

### Loading Data
```python
import numpy as np
data = np.load('data/profiles.npz')
r = data['r']
alcubierre = data['alcubierre']
natario = data['natario']
```

---

## compute_support_size.py

**Purpose**: Estimate practical support sizes for each profile function given a specified threshold value.

### Features
- Configurable threshold for support boundary detection
- Multiple profile analysis in single run
- Precise support size estimation
- Console output with clear formatting

### Usage
```bash
python scripts/compute_support_size.py
```

### Functions
- `find_support(r, values, threshold=1e-3)`: Find maximum r where f(r) ≥ threshold
- `main(r_max=5.0, num=1000, threshold=1e-3)`: Analyze all profiles

### Default Parameters
- **Range**: $r \in [0, 5]$
- **Resolution**: 1000 points
- **Threshold**: $10^{-3}$

### Example Output
```
Alcubierre support (f(r) ≥ 0.001): r ≤ 1.842
Natário support (f(r) ≥ 0.001): r ≤ 2.632
```

### Threshold Selection
- **$10^{-3}$**: Conservative practical support
- **$10^{-6}$**: Extended support for high-precision applications
- **$10^{-1}$**: Core support region

---

## export_profiles_csv.py

**Purpose**: Export profile data to human-readable CSV format for analysis in external tools, spreadsheet applications, or other programming languages.

### Features
- Human-readable CSV format
- Automatic directory creation
- Configurable resolution and range
- Standard CSV structure for easy import

### Usage
```bash
python scripts/export_profiles_csv.py
```

### Functions
- `export_csv(r_max=3.0, num=500, filename=None)`: Main export function

### Default Parameters
- **Range**: $r \in [0, 3]$
- **Resolution**: 500 points
- **Output**: `data/profile_data.csv`

### Output Format
```csv
r,alcubierre,natario
0.0,0.0,1.0
0.006012024048096192,0.0001507985844344775,0.9999638529769526
0.012024048096192384,0.0006031690049075105,0.9998554316543844
...
```

### Usage in Other Tools
- **Excel/LibreOffice**: Direct import with comma delimiter
- **MATLAB**: `readtable('data/profile_data.csv')`
- **R**: `read.csv('data/profile_data.csv')`
- **Pandas**: `pd.read_csv('data/profile_data.csv')`

---

## Common Workflow

### 1. Generate Data
```bash
python scripts/generate_profile_data.py
python scripts/export_profiles_csv.py
```

### 2. Analyze Properties
```bash
python scripts/compute_support_size.py
```

### 3. Create Visualizations
```bash
python scripts/plot_profiles.py
```

### 4. Verify Output
Check generated files:
- `data/profiles.npz` (binary data)
- `data/profile_data.csv` (CSV data)
- `data/plots/profiles.png` (visualization)

---

## Customization

### Parameter Modification
To use different parameters, modify the function calls in each script:

```python
# Custom Alcubierre parameters
alcubierre_profile(r, R=2.0, sigma=15.0)

# Custom Natário parameters
nataro_gaussian(r, alpha=1.5)

# Custom range and resolution
plot_profiles(r_max=5.0, num=1000)
```

### Adding New Profiles
To add new profile functions:

1. Define the mathematical function
2. Add it to the profile dictionary in each script
3. Update the CSV headers and NumPy save calls
4. Include in the plotting routine

### Example New Profile
```python
def custom_profile(r, param1=1.0, param2=2.0):
    """Custom warp-bubble profile function."""
    return np.exp(-r/param1) * np.cos(param2*r)**2

# Add to profiles dictionary
profiles['Custom'] = custom_profile(r, param1=1.5, param2=3.0)
```

---

## Dependencies

All scripts require:
- **NumPy**: Numerical computations
- **Matplotlib**: Plotting (plot_profiles.py only)
- **CSV module**: Data export (built-in Python)

Install dependencies:
```bash
pip install numpy matplotlib
```

## Error Handling

Scripts include basic error handling for:
- Directory creation failures
- File I/O errors
- Invalid parameter ranges
- Missing dependencies

For debugging, run scripts with Python's verbose mode:
```bash
python -v scripts/script_name.py
```
