# patterns.py — Predefined field patterns for UIM simulations

import numpy as np

# Fibonacci pattern initializer
def init_fibonacci(size):
    fib = [0, 1]
    while len(fib) < max(size):
        fib.append(fib[-1] + fib[-2])
    fib_norm = np.array(fib[:size[1]]) / max(fib[:size[1]])
    return np.tile(fib_norm, (size[0], 1))

# Phi spiral pattern (approximate golden angle field)
def init_phi_spiral(size, phi=1.618):
    cx, cy = size[0] // 2, size[1] // 2
    field = np.zeros(size)
    for i in range(1, size[0] * size[1]):
        r = np.sqrt(i)
        theta = i * 2 * np.pi / phi
        x = int(cx + r * np.cos(theta))
        y = int(cy + r * np.sin(theta))
        if 0 <= x < size[0] and 0 <= y < size[1]:
            field[x, y] = 1
    return field

# Prime lattice: fill grid with 1 where index is prime
def init_prime_lattice(size):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    field = np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            idx = i * size[1] + j
            if is_prime(idx):
                field[i, j] = 1
    return field
