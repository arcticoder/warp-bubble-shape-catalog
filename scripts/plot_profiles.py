#!/usr/bin/env python3
"""
Plot warp-bubble shape functions (Alcubierre, Natário) for visualization.
"""
import numpy as np
import matplotlib
# Try different backends for interactive display
try:
    matplotlib.use('Qt5Agg')  # Try Qt backend first
except ImportError:
    try:
        matplotlib.use('TkAgg')  # Fall back to Tk
    except ImportError:
        # Use default backend if neither works
        pass
import matplotlib.pyplot as plt

def alcubierre_profile(r, R=1.0, sigma=10.0):
    return (np.tanh(sigma*(r + R)) - np.tanh(sigma*(r - R))) / (2 * np.tanh(sigma*R))

def nataro_gaussian(r, alpha=1.0):
    return np.exp(-r**2 / alpha**2)

def plot_profiles(r_max=3.0, num=500, save_plot=True, show_plot=False):
    r = np.linspace(0, r_max, num)
    profiles = {
        'Alcubierre (R=1, σ=10)': alcubierre_profile(r, R=1.0, sigma=10.0),
        'Natário Gaussian (α=1)': nataro_gaussian(r, alpha=1.0),
    }
    for label, values in profiles.items():
        plt.plot(r, values, label=label)
    plt.xlabel('r')
    plt.ylabel('f(r)')
    plt.title('Warp-Bubble Shape Functions')
    plt.legend()
    plt.grid(True)
    
    if save_plot:
        import os
        os.makedirs('../data/plots', exist_ok=True)
        plt.savefig('../data/plots/profiles.png', dpi=300, bbox_inches='tight')
        print("Plot saved to data/plots/profiles.png")
    
    if show_plot:
        plt.show()

if __name__ == '__main__':
    import sys
    
    # Command line options
    if len(sys.argv) > 1:
        if '--interactive' in sys.argv or '-i' in sys.argv:
            plot_profiles(show_plot=True, save_plot=False)
        elif '--save-only' in sys.argv or '-s' in sys.argv:
            plot_profiles(show_plot=False, save_plot=True)
        elif '--both' in sys.argv or '-b' in sys.argv:
            plot_profiles(show_plot=True, save_plot=True)
        else:
            print("Usage:")
            print("  python plot_profiles.py           # Interactive + save (default)")
            print("  python plot_profiles.py -i        # Interactive only")
            print("  python plot_profiles.py -s        # Save only")
            print("  python plot_profiles.py -b        # Both interactive + save")
    else:
        # Default: show interactively and save
        plot_profiles(show_plot=True, save_plot=True)
