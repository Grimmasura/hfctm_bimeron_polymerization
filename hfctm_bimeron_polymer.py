import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import argparse

# Parameters
K = 1.0
D = 0.8
H_ext = 0.0
J = 0.2
T = 0.05

# Initialize phase grid
grid_size = (100, 100)
phase_grid = np.random.choice([-1, 1], size=grid_size)

# Energy computation (simple prototype)
def compute_energy(grid, K, D, H_ext, J):
    E = 0
    for i in range(grid.shape[0]-1):
        for j in range(grid.shape[1]-1):
            E += -K * grid[i,j] * (grid[i+1,j] + grid[i,j+1])
            E += -D * grid[i,j] * (grid[i+1,j+1])
            E += -H_ext * grid[i,j]
    return E

# Evolution function
def evolve_phase(grid, steps, K, D, H_ext, J, T):
    for step in range(steps):
        i, j = np.random.randint(0, grid.shape[0]), np.random.randint(0, grid.shape[1])
        dE = -2 * grid[i,j] * compute_energy(grid, K, D, H_ext, J)
        if dE < 0 or np.random.rand() < np.exp(-dE / T):
            grid[i,j] *= -1
    return grid

# Visualization
def plot_phase(grid, title='Phase Space', out_path='phase_space.png'):
    """Save the phase grid as an image without opening a window."""
    plt.imshow(grid, cmap='coolwarm')
    plt.title(title)
    plt.colorbar()
    plt.savefig(out_path)
    plt.close()

def main():
    parser = argparse.ArgumentParser(
        description='Bimeron polymerization prototype simulation')
    parser.add_argument('--steps', type=int, default=10000,
                        help='Number of evolution steps')
    parser.add_argument('--output', default='phase_space.png',
                        help='Filename for saved phase plot')
    args = parser.parse_args()

    grid = evolve_phase(phase_grid, args.steps, K, D, H_ext, J, T)
    plot_phase(grid, 'Bimeron Polymerization Prototype', args.output)

    glyph_array = np.sign(grid)
    np.save('bimeron_codex_glyph.npy', glyph_array)
    print(
        f'Glyph array saved to bimeron_codex_glyph.npy and plot saved to {args.output}'
    )


if __name__ == '__main__':
    main()
