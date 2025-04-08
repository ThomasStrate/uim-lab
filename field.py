# field.py — Core class for UIM informational field

import numpy as np

class Field:
    def __init__(self, size=(20, 20), init_pattern=None):
        self.size = size
        self.psi = np.zeros(size)  # informational value per cell
        self.rho = np.ones(size) * 0.5  # resistance per cell (default 0.5)
        self.history = []

        if init_pattern is not None:
            self.apply_pattern(init_pattern)

    def apply_pattern(self, pattern_fn):
        """Apply a pattern initialization function to psi."""
        self.psi = pattern_fn(self.size)

    def set_resistance(self, resistance_map):
        """Set resistance values directly."""
        self.rho = resistance_map

    def update(self, resonance_fn, resistance_fn=None, noise_level=0.01):
        """
        Update the field based on resonance and optional resistance feedback.
        """
        new_psi = np.copy(self.psi)
        for x in range(1, self.size[0] - 1):
            for y in range(1, self.size[1] - 1):
                neighborhood = self.psi[x-1:x+2, y-1:y+2]
                avg = np.mean(neighborhood)
                damping = np.exp(-self.rho[x, y])
                noise = np.random.normal(0, noise_level)
                new_psi[x, y] = resonance_fn(avg) * damping + noise

        if resistance_fn is not None:
            self.rho = resistance_fn(self.psi, self.rho)

        self.psi = new_psi
        self.history.append(self.psi.copy())

    def get_state(self):
        return self.psi

    def get_history(self):
        return self.history

    def reset(self):
        self.psi = np.zeros(self.size)
        self.rho = np.ones(self.size) * 0.5
        self.history = []
