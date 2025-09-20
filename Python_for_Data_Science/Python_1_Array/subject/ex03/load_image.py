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


def main() -> None:
    """test from subject"""
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
