#!/usr/bin/env python3
"""
Plot warp-bubble shape functions (Alcubierre, Natário) for visualization.
"""
import numpy as np
import matplotlib.pyplot as plt

def alcubierre_profile(r, R=1.0, sigma=10.0):
    return (np.tanh(sigma*(r + R)) - np.tanh(sigma*(r - R))) / (2 * np.tanh(sigma*R))

def nataro_gaussian(r, alpha=1.0):
    return np.exp(-r**2 / alpha**2)

def plot_profiles(r_max=3.0, num=500):
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
    plt.show()

if __name__ == '__main__':
    plot_profiles()
