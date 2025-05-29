#!/usr/bin/env python3
"""
Plot warp-bubble shape functions (Alcubierre, Natário) for visualization.
"""
import numpy as np
import matplotlib
import sys

# Set backend based on whether interactive display is needed
interactive_backend_available = False
if __name__ == '__main__':
    if len(sys.argv) > 1 and ('--save-only' in sys.argv or '-s' in sys.argv):
        matplotlib.use('Agg')  # Non-interactive backend for save-only mode
    else:
        # Try different backends for interactive display
        for backend in ['TkAgg', 'Qt5Agg']:
            try:
                # Test if we can import the backend
                if backend == 'TkAgg':
                    import tkinter
                elif backend == 'Qt5Agg':
                    import PyQt5
                    
                matplotlib.use(backend)
                interactive_backend_available = True
                break
            except ImportError:
                continue
        
        if not interactive_backend_available:
            matplotlib.use('Agg')
            print("Warning: No interactive backend available. Interactive display disabled.")
            print("Install tkinter (usually included with Python) or PyQt5 for interactive display:")
            print("  pip install PyQt5")

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
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    for label, values in profiles.items():
        plt.plot(r, values, label=label)
    plt.xlabel('r')
    plt.ylabel('f(r)')
    plt.title('Warp-Bubble Shape Functions')
    plt.legend()
    plt.grid(True)
    
    if save_plot:
        import os
        # Save to data/plots for high-resolution visualization
        os.makedirs('../data/plots', exist_ok=True)
        plt.savefig('../data/plots/profiles.png', dpi=300, bbox_inches='tight')
        print("Plot saved to data/plots/profiles.png")
        
        # Also save to docs/assets/images for Jekyll site
        os.makedirs('../docs/assets/images', exist_ok=True)
        plt.savefig('../docs/assets/images/profiles.png', dpi=300, bbox_inches='tight')
        print("Plot also saved to docs/assets/images/profiles.png")
    
    if show_plot:
        if not globals().get('interactive_backend_available', False):
            print("Interactive display not available. Plot saved to file instead.")
            print("To enable interactive display, install: pip install PyQt5")
        else:
            try:
                plt.show()
            except Exception as e:
                print(f"Warning: Could not display plot interactively: {e}")
                print("Plot was still generated successfully.")
    
    plt.close()  # Clean up the figure

if __name__ == '__main__':
    import sys
    
    # Command line options
    if len(sys.argv) > 1:
        if '--interactive' in sys.argv or '-i' in sys.argv:
            if interactive_backend_available:
                plot_profiles(show_plot=True, save_plot=False)
            else:
                print("Interactive display not available. Use --save-only to generate plot file.")
                plot_profiles(show_plot=False, save_plot=True)
        elif '--save-only' in sys.argv or '-s' in sys.argv:
            plot_profiles(show_plot=False, save_plot=True)
        elif '--both' in sys.argv or '-b' in sys.argv:
            show_interactive = interactive_backend_available
            if not show_interactive:
                print("Interactive display not available. Saving plot only.")
            plot_profiles(show_plot=show_interactive, save_plot=True)
        else:
            print("Usage:")
            print("  python plot_profiles.py           # Interactive + save (default)")
            print("  python plot_profiles.py -i        # Interactive only")
            print("  python plot_profiles.py -s        # Save only")
            print("  python plot_profiles.py -b        # Both interactive + save")
    else:
        # Default: show interactively and save (if interactive available)
        show_interactive = interactive_backend_available
        if not show_interactive:
            print("Interactive display not available. Saving plot only.")
            print("Install PyQt5 for interactive display: pip install PyQt5")
        plot_profiles(show_plot=show_interactive, save_plot=True)
