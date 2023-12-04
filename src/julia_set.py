import numpy as np
import matplotlib.pyplot as plt


def generate_julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    fractal = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        Z = Z**2 + c
        mask = np.abs(Z) < 1000  # Escape condition
        fractal += mask

    return fractal


def plot_fractal(fractal):
    plt.imshow(fractal, cmap="hot", extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title("Julia Set")
    plt.show()


# Set parameters
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
c = complex(-0.7, 0.27)  # You can experiment with different values of 'c'
max_iter = 100

# Generate and plot Julia Set
fractal = generate_julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)
plot_fractal(fractal)
