---
layout: default
title: Warp-Bubble Profiles
---

# Warp-Bubble Shape Profiles

This page catalogs the mathematical definitions of various warp-bubble shape functions, each with their defining formulas, support characteristics, and adjustable parameters.

## Alcubierre Profile

### Defining Formula

The Alcubierre profile uses hyperbolic tangent functions to create a smooth transition region:

$$f(r) = \frac{\tanh\bigl(\sigma (r + R)\bigr) - \tanh\bigl(\sigma (r - R)\bigr)}{2\,\tanh(\sigma R)}$$

### Support Size

This profile exhibits **compact support** approximately within the region $r \in [R - \Delta,\, R + \Delta]$, where the width $\Delta$ is inversely related to the steepness parameter $\sigma$.

For practical purposes:
- Higher $\sigma$ values create sharper transitions and more compact support
- The effective support width scales as $\Delta \propto 1/\sigma$

### Free Parameters

| Parameter | Symbol | Description | Typical Range |
|-----------|--------|-------------|---------------|
| Bubble radius | $R$ | Central radius of the warp bubble | $R > 0$ |
| Steepness | $\sigma$ | Controls transition sharpness | $\sigma \gg 1$ |

### Characteristics

- **Smooth transitions**: The tanh functions ensure $C^∞$ smoothness
- **Controllable width**: The $\sigma$ parameter allows precise control over the transition region
- **Normalized**: The denominator ensures proper scaling relative to the bubble size

---

## Natário Gaussian Variant

### Defining Formula

The Natário profile uses a Gaussian form for smooth, bell-shaped distributions:

$$f(r) = \exp\!\bigl(-r^2 / \alpha^2\bigr)$$

### Support Size

This profile has **effectively non-compact support** but exhibits rapid exponential decay:

- Practical support extends to approximately $r \approx 3\alpha$
- At $r = \alpha$: $f(r) = e^{-1} \approx 0.368$
- At $r = 2\alpha$: $f(r) = e^{-4} \approx 0.018$
- At $r = 3\alpha$: $f(r) = e^{-9} \approx 0.0001$

### Free Parameters

| Parameter | Symbol | Description | Typical Range |
|-----------|--------|-------------|---------------|
| Width parameter | $\alpha$ | Controls the Gaussian width | $\alpha > 0$ |

### Characteristics

- **Smooth everywhere**: Infinitely differentiable Gaussian profile
- **Centered peak**: Maximum value of 1 at $r = 0$
- **Exponential decay**: Rapid falloff ensures practical finite support
- **Scale invariant**: Shape preserved under scaling transformations

---

## Profile Comparison

| Property | Alcubierre | Natário Gaussian |
|----------|------------|------------------|
| **Support Type** | Compact | Effectively compact |
| **Smoothness** | $C^∞$ | $C^∞$ |
| **Peak Location** | Distributed over $[R-\Delta, R+\Delta]$ | $r = 0$ |
| **Parameters** | 2 ($R$, $\sigma$) | 1 ($\alpha$) |
| **Computational Cost** | Moderate (tanh evaluations) | Low (exponential) |
| **Physical Interpretation** | Localized warp region | Centralized warp field |

---

## Mathematical Properties

### Normalization

Both profiles can be normalized for specific applications:

- **Alcubierre**: Already normalized by construction through the denominator
- **Natário**: Can be scaled by constants or integrated for area normalization

### Derivatives

The profiles exhibit well-behaved derivatives:

**Alcubierre first derivative:**
$$f'(r) = \frac{\sigma}{2\tanh(\sigma R)} \left[ \operatorname{sech}^2(\sigma(r+R)) + \operatorname{sech}^2(\sigma(r-R)) \right]$$

**Natário first derivative:**
$$f'(r) = -\frac{2r}{\alpha^2} \exp\!\bigl(-r^2/\alpha^2\bigr)$$

### Asymptotic Behavior

- **Alcubierre**: $f(r) \to 0$ exponentially fast as $|r-R| \to \infty$
- **Natário**: $f(r) \to 0$ as $r \to \infty$ with Gaussian decay

---

## Implementation Notes

All profiles are implemented in the `scripts/plot_profiles.py` module with default parameter values chosen for clear visualization and numerical stability.

For custom parameter exploration, modify the function calls in the provided scripts or use the exported data formats for further analysis.
