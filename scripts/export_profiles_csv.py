#!/usr/bin/env python3
"""
Export profile data to CSV for further analysis.
"""
import numpy as np
import csv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.plot_profiles import alcubierre_profile, nataro_gaussian

def export_csv(r_max=3.0, num=500, filename='profile_data.csv'):
    r = np.linspace(0, r_max, num)
    data = {
        'r': r,
        'alcubierre': alcubierre_profile(r),
        'natario': nataro_gaussian(r),
    }
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['r', 'alcubierre', 'natario'])
        for i in range(len(r)):
            writer.writerow([data['r'][i], data['alcubierre'][i], data['natario'][i]])
    print(f"CSV exported to {filename}")

if __name__ == '__main__':
    export_csv()
