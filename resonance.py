# resonance.py — Resonance functions for UIM field dynamics

import numpy as np

# Basic passthrough (identity resonance)
def identity_resonance(x):
    return x

# Sinusoidal resonance based on amplitude
# Models a simple harmonic activation

def sinusoidal_resonance(x, amplitude=1.0, frequency=1.0):
    return amplitude * np.sin(frequency * x)

# Resonance decay — simulates a feedback that dampens toward zero

def decaying_resonance(x, decay_rate=0.1):
    return x * np.exp(-decay_rate * abs(x))

# Stabilizing phi-style ratio resonance (toward golden mean)
def phi_resonance(x, phi_target=1.618, k=2.5):
    """
    Feedback function that pulls values toward golden ratio
    """
    return x + (phi_target - x) / k

# Composite resonance builder (combine multiple modes)
def composite_resonance(x, mode="phi"):
    if mode == "phi":
        return phi_resonance(x)
    elif mode == "decay":
        return decaying_resonance(x)
    elif mode == "sin":
        return sinusoidal_resonance(x)
    else:
        return identity_resonance(x)
