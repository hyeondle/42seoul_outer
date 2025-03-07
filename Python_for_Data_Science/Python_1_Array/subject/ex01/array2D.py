import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a given 2D list based on the provided start and end indices.

    Parameters:
    family (list): A 2D list representing numerical data.
    start (int): The starting index for slicing.
    end (int): The ending index for slicing.

    Returns:
    list: A new 2D list containing the truncated data.

    Raises:
    TypeError: If the input is not a list.
    ValueError: If the input is not a valid 2D list.
    """
    if (
        not isinstance(family, list) or
        not all(isinstance(row, list) for row in family)
    ):
        raise TypeError("Input must be a 2D list.")

    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) != 1:
        raise ValueError("All inner lists must have the same length.")

    array = np.array(family)
    print("My shape is :", array.shape)
    new_array = array[start:end]
    print("My new shape is :", new_array.shape)

    return new_array.tolist()


def main():
    return


if __name__ == '__main__':
    main()
