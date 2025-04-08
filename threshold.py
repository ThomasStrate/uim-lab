# threshold.py — Perception and collapse functions in UIM

import numpy as np

# Sigmoid perception activation function
def sigmoid_threshold(rho, k=10, rho_0=0.5):
    """
    Returns a perception intensity from 0 to 1 based on resistance.
    """
    return 1 / (1 + np.exp(-k * (rho - rho_0)))

# Hard collapse (binary)
def binary_collapse(psi, rho, threshold=0.7):
    """
    Collapse to 1 where resistance exceeds threshold, else 0.
    """
    collapsed = np.where(rho >= threshold, 1, 0)
    return collapsed * psi

# Smooth collapse with damping
def damped_collapse(psi, rho, threshold=0.7, sharpness=5):
    """
    Damps psi based on resistance gradient around threshold.
    """
    mask = 1 / (1 + np.exp(-sharpness * (rho - threshold)))
    return psi * mask

# Perception gating function (dynamic control)
def perception_filter(psi, rho, mode="sigmoid"):
    if mode == "sigmoid":
        return psi * sigmoid_threshold(rho)
    elif mode == "binary":
        return binary_collapse(psi, rho)
    elif mode == "damped":
        return damped_collapse(psi, rho)
    else:
        return psi