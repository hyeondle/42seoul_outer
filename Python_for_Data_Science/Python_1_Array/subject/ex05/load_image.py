import os
import numpy as np
from PIL import Image


def ft_load(path: str):
    """function that loads an image, prints its format, and its pixels
    content in RGB format.
    """
    try:
        if not isinstance(path, str) or not path:
            raise ValueError("path must be a non-empty string.")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        ext = os.path.splitext(path)[1].lower()
        if ext not in {".jpg", ".jpeg"}:
            raise ValueError("Unsupported format. Please use JPG or JPEG.")
        with Image.open(path) as im:
            im = im.convert("RGB")
            arr = np.asarray(im, dtype=np.uint8)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        return arr
    except Exception as exc:
        print(f"Error loading image: {exc}")
        return None


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


def main() -> None:
    """test from subject"""
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
