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

    print("The shape of image is:", array.shape)
    print(array)
    return array


def main():
    return


if __name__ == '__main__':
    main()
