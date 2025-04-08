# resistance.py — Resistance dynamics for UIM fields

import numpy as np

# Static resistance: returns unchanged

def static_resistance(psi, rho):
    return rho

# Gradient-based resistance: more change = more resistance

def gradient_resistance(psi, rho, sensitivity=1.0):
    new_rho = rho.copy()
    for x in range(1, psi.shape[0] - 1):
        for y in range(1, psi.shape[1] - 1):
            local = psi[x-1:x+2, y-1:y+2]
            grad = np.abs(local - psi[x, y])
            delta = np.mean(grad)
            new_rho[x, y] = rho[x, y] + sensitivity * delta
    return np.clip(new_rho, 0.01, 1.0)

# Exponential decay: resistance fades slowly over time

def decaying_resistance(psi, rho, decay_rate=0.01):
    return rho * (1 - decay_rate)

# Threshold-triggered resistance boost

def threshold_resistance(psi, rho, threshold=1.0, boost=0.1):
    new_rho = rho.copy()
    trigger = np.abs(psi) > threshold
    new_rho[trigger] += boost
    return np.clip(new_rho, 0.01, 1.0)

# Composite logic

def composite_resistance(psi, rho, mode="gradient"):
    if mode == "gradient":
        return gradient_resistance(psi, rho)
    elif mode == "decay":
        return decaying_resistance(psi, rho)
    elif mode == "threshold":
        return threshold_resistance(psi, rho)
    else:
        return static_resistance(psi, rho)