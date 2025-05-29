#!/usr/bin/env python3
"""
Generate numeric data for warp-bubble profiles and save to NumPy files.
"""
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.plot_profiles import alcubierre_profile, nataro_gaussian

def generate_data(r_max=3.0, num=500, output_dir='data'):
    os.makedirs(output_dir, exist_ok=True)
    r = np.linspace(0, r_max, num)
    profiles = {
        'alcubierre': alcubierre_profile(r),
        'natario': nataro_gaussian(r),
    }
    np.savez_compressed(os.path.join(output_dir, 'profiles.npz'), r=r, **profiles)
    print(f"Data saved to {output_dir}/profiles.npz")

if __name__ == '__main__':
    generate_data()
