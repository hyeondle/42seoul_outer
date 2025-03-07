import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape,
    and returns its pixel content in RGB format.

    Parameters:
    path (str): The file path of the image.

    Returns:
    np.ndarray: A NumPy array containing the image pixels in RGB format.

    Raises:
    FileNotFoundError: If the file does not exist.
    ValueError: If the file format is not supported.
    """
    try:
        image = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")
    except Exception:
        raise ValueError("Error: Unable to open the file.")

    if image.format not in ("JPEG", "JPG"):
        raise ValueError("Error: Only JPG and JPEG formats are supported.")

    image = image.convert("RGB")
    array = np.array(image)

    # print("The shape of image is:", array.shape)
    # print(array)
    return array


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

    print("The shape of image is:", zoomed_array.shape)
    print(zoomed_array)

    return zoomed_array


def main():
    return


if __name__ == '__main__':
    main()
