#!/usr/bin/env python3
"""
Estimate practical support sizes for profiles given a threshold.
"""
import numpy as np
from scripts.plot_profiles import alcubierre_profile, nataro_gaussian

def find_support(r, values, threshold=1e-3):
    mask = values >= threshold
    if not mask.any():
        return 0.0
    return r[mask].max()

def main(r_max=5.0, num=1000, threshold=1e-3):
    r = np.linspace(0, r_max, num)
    profiles = {
        'Alcubierre': alcubierre_profile(r),
        'Natário': nataro_gaussian(r),
    }
    for name, values in profiles.items():
        support = find_support(r, values, threshold)
        print(f"{name} support (f(r) ≥ {threshold}): r ≤ {support:.3f}")

if __name__ == '__main__':
    main()
