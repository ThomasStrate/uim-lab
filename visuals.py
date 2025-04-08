# visuals.py — Field rendering and animation for UIM simulations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Render a single field state
def render_field(field_state, title="Field", cmap="viridis"):
    plt.figure(figsize=(6, 5))
    plt.imshow(field_state, cmap=cmap, interpolation='nearest')
    plt.colorbar(label="ψ")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

# Animate a list of field states
def animate_field(history, interval=100, cmap="viridis", save_path=None):
    fig, ax = plt.subplots()
    cax = ax.imshow(history[0], cmap=cmap, interpolation='nearest')
    fig.colorbar(cax)
    
    def animate(i):
        cax.set_array(history[i])
        ax.set_title(f"Timestep {i}")
        return [cax]

    ani = animation.FuncAnimation(fig, animate, frames=len(history), interval=interval, blit=True)
    plt.tight_layout()

    if save_path:
        ani.save(save_path, writer="pillow")
        print(f"Animation saved to {save_path}")
    else:
        plt.show()

# Compare two states side-by-side
def compare_fields(state1, state2, labels=("State 1", "State 2"), cmap="viridis"):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, state, label in zip(axes, [state1, state2], labels):
        im = ax.imshow(state, cmap=cmap, interpolation='nearest')
        ax.set_title(label)
        plt.colorbar(im, ax=ax)
    plt.tight_layout()
    plt.show()
