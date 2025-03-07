import numpy as np
from load_image import ft_load, ft_zoom
import matplotlib.pyplot as plt


def ft_rotate(image_array: np.ndarray) -> np.ndarray:
    """
    Rotates the given image
    by transposing the array manually (90-degree rotation).

    Parameters:
    image_array (np.ndarray): The input image array.

    Returns:
    np.ndarray: The rotated image array.
    """
    if image_array.ndim != 3:
        raise ValueError("Error: Image array must have 3 dimensions.")

    height, width, channels = image_array.shape
    # np.zeros creates an array filled with zeros
    # original shape is (height, width, channels)
    # rotated shape is (width, height, channels)
    rotated_array = np.zeros(
        (width, height, channels),
        dtype=image_array.dtype
    )

    for i in range(height):
        for j in range(width):
            rotated_array[j, i] = image_array[i, j]

    return rotated_array


def main():
    try:
        image_array = ft_load("animal.jpeg")
        zoomed_image = ft_zoom(image_array, 1)
        rotated_image = ft_rotate(zoomed_image)

        plt.figure(figsize=(6, 6))

        if rotated_image.shape[2] == 1:
            plt.imshow(rotated_image.squeeze(), cmap='gray')
        else:
            plt.imshow(rotated_image)

        plt.xticks(np.arange(0, rotated_image.shape[1], 50))
        plt.yticks(np.arange(0, rotated_image.shape[0], 50))
        plt.show()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
