# entropy.py — Entropy and order metrics for UIM field analysis

import numpy as np

# Shannon entropy of field state
def calculate_entropy(field_state, bins=50):
    """
    Estimate Shannon entropy of psi values in field.
    """
    hist, _ = np.histogram(field_state, bins=bins, density=True)
    hist = hist[hist > 0]  # remove zeros to avoid log(0)
    return -np.sum(hist * np.log2(hist))

# Relative change in entropy over time
def entropy_change(history):
    """
    Compute list of entropy values over time.
    """
    return [calculate_entropy(state) for state in history]

# Structure index: deviation from uniformity
def structure_score(field_state):
    """
    Measures deviation from uniform randomness (lower is more structured).
    """
    flat = field_state.flatten()
    mean = np.mean(flat)
    variance = np.var(flat)
    return 1 / (1 + variance)  # low variance = high structure

# Detect emergence point (entropy drop or structure spike)
def detect_emergence(entropy_series, threshold=0.05):
    """
    Returns the timestep where structure significantly increases.
    """
    diffs = np.diff(entropy_series)
    for i, d in enumerate(diffs):
        if d < -threshold:
            return i + 1
    return None