import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(image_array: np.ndarray, channel: int) -> np.ndarray:
    """
    Zooms into the center of the given image array
    and optionally reduces the channels.

    Parameters:
    image_array (np.ndarray): The original image array.
    channel (int): The number of channels (1 for grayscale, 3 for RGB).

    Returns:
    np.ndarray: A zoomed and optionally channel-reduced image array.
    """
    if image_array.ndim != 3 or image_array.shape[2] not in [1, 3]:
        raise ValueError("Error: Image array must have 3 dimensions.")

    # get center point of the image
    center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2
    # set offset to slicing the image
    zoomed_array = image_array[
        center_y - 290:center_y + 110,
        center_x - 50:center_x + 350
    ]

    # three kind of grayscale color system.
    # https://en.wikipedia.org/wiki/Grayscale
    if channel == 1 and zoomed_array.shape[2] == 3:
        # np.dot is a matrix multiplication
        zoomed_array = np.dot(zoomed_array[..., :3], [0.2989, 0.5870, 0.1140])
        # add a new axis to the array
        zoomed_array = zoomed_array[..., np.newaxis]

    print("New shape after slicing:", zoomed_array.shape)
    print(zoomed_array)

    return zoomed_array


def main():
    """
    load image and zoom image test.
    """
    try:
        image_array = ft_load("animal.jpeg")
        zoomed_image = ft_zoom(image_array, 1)

        plt.figure(figsize=(6, 6))

        # if the image is grayscale
        if zoomed_image.shape[2] == 1:
            plt.imshow(zoomed_image.squeeze(), cmap='gray')
        # if the image is RGB
        else:
            plt.imshow(zoomed_image)

        plt.xticks(np.arange(0, zoomed_image.shape[1], 50))
        plt.yticks(np.arange(0, zoomed_image.shape[0], 50))
        plt.show()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
