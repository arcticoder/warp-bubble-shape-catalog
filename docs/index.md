---
layout: default
title: Home
date: 2025-05-29
---

# Warp-Bubble Shape Catalog

**Catalog of candidate warp‐bubble shape functions**

*Created: May 29, 2025*

This repository collects the defining formulas, support sizes, and key free parameters for 2 warp‐bubble "shape" profiles, Alcubierre's tanh‐based profile and Natário's smooth Gaussian variant.

## Overview

This catalog serves as a reference repository documenting various mathematical functions used to define warp-bubble geometries in theoretical physics. Each profile is characterized by:

- **Defining Formula**: The mathematical expression that describes the shape function
- **Support Size**: The spatial extent over which the function is non-negligible
- **Free Parameters**: Adjustable parameters that control the shape characteristics

## Contents

This site is organized into the following sections:

- **[Profiles](profiles.md)**: Detailed mathematical descriptions of each warp-bubble shape function
- **[Scripts](scripts.md)**: Python utilities for computation, visualization, and data export
- **[Visuals](visuals.md)**: Generated plots and visualizations of the profile functions

## Purpose

This catalog is designed as a dependency for downstream projects that will specify:

- Coordinate system choices (e.g., spherical coordinates $(t,r,\theta,\phi)$)
- Symmetry assumptions (e.g., axial symmetry about the $z$–axis, compact support in $r$)
- Metric ansatz simplifications

## Data Availability

Numeric data for all profiles is available in multiple formats:

- **NumPy format**: `data/profiles.npz` (compressed binary)
- **CSV format**: `data/profile_data.csv` (human-readable)

These datasets contain discretized $(r, f(r))$ values for each profile function, generated using the provided Python scripts.

## Repository Structure

```
├── _config.yml          # Jekyll configuration
├── index.md             # This overview page
├── profiles.md          # Mathematical profile descriptions
├── scripts.md           # Script documentation
├── visuals.md           # Plots and visualizations
├── data/                # Generated data and plots
│   ├── profiles.npz     # NumPy data file
│   ├── profile_data.csv # CSV export
│   └── plots/           # Generated visualizations
└── scripts/             # Python computation scripts
    ├── plot_profiles.py
    ├── generate_profile_data.py
    ├── compute_support_size.py
    └── export_profiles_csv.py
```

## Getting Started

1. Browse the [Profiles](profiles.md) to understand the mathematical definitions
2. Check the [Visuals](visuals.md) for graphical representations
3. Use the [Scripts](scripts.md) to generate your own data or modifications
4. Include this repository as a submodule or reference in your downstream projects
