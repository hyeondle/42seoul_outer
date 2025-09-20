import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""

    inverted_array = 255 - array

    plt.figure(figsize=(6, 6))
    plt.imshow(inverted_array)
    plt.show()

    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Applies a red filter to the image."""
    filtered_array = np.zeros_like(array)
    filtered_array[..., 0] = array[..., 0]  # Keep Red channel

    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_array)
    plt.show()

    return filtered_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """Applies a green filter to the image."""
    filtered_array = np.array(array)
    filtered_array[..., 0] = 0  # Remove Red channel
    filtered_array[..., 2] = 0  # Remove Blue channel

    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_array)
    plt.show()

    return filtered_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Applies a blue filter to the image."""
    filtered_array = np.zeros_like(array)
    filtered_array[..., 2] = array[..., 2]  # Keep Blue channel

    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_array)
    plt.show()

    return filtered_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    grey_array = (array[..., 0] / 3 +
                  array[..., 1] / 3 +
                  array[..., 2] / 3).astype(np.uint8)
    filtered_array = np.stack((grey_array,) * 3, axis=-1)

    plt.figure(figsize=(6, 6))
    plt.imshow(filtered_array)
    plt.show()

    return filtered_array  # Convert back to 3-channel grayscale


def main():
    """simple test"""
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
    return


if __name__ == '__main__':
    main()
