import time
import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    """Computes the escape time of a complex number c in the Mandelbrot set.

    Args:
        c (complex): The complex number to test.
        max_iter (int): The maximum number of iterations to perform.

    Returns:
        int: The escape time of c, or max_iter if c does not escape.
    """

    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n


def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    """Draws a Mandelbrot fractal to a NumPy array.

    Args:
        xmin (float): The minimum x-value of the image.
        xmax (float): The maximum x-value of the image.
        ymin (float): The minimum y-value of the image.
        ymax (float): The maximum y-value of the image.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        max_iter (int): The maximum number of iterations to perform per pixel.

    Returns:
        np.ndarray: A NumPy array containing the Mandelbrot fractal.
    """

    img = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            c = complex(
                xmin + x * (xmax - xmin) / width, ymin + y * (ymax - ymin) / height
            )
            img[y, x] = mandelbrot(c, max_iter)
    return img


if __name__ == "__main__":
    # Start the timer
    start_time = time.perf_counter()

    # Set the parameters of the image
    xmin = -2.5
    xmax = 1.5
    ymin = -2
    ymax = 2
    width = 512
    height = 512
    max_iter = 100

    # Draw the Mandelbrot fractal
    img = draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

    # Stop the timer
    end_time = time.perf_counter()

    # Display the image
    plt.imshow(img, cmap="jet")
    plt.colorbar()
    plt.title("Mandelbrot Fractal")
    plt.show()

    # Print the elapsed time
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")
