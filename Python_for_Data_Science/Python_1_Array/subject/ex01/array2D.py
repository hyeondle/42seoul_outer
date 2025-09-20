def slice_me(family: list, start: int, end: int) -> list:
    """function that takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array
    based on the provided start and end arguments.
    """
    if not isinstance(family, list) or len(family) == 0:
        raise ValueError("family must be a non-empty list of lists.")
    if not all(isinstance(row, list) for row in family):
        raise ValueError("family must be a list of lists.")
    ncols = len(family[0])
    if ncols == 0:
        raise ValueError("inner lists must be non-empty.")
    for row in family:
        if len(row) != ncols:
            raise ValueError("all rows must have same length.")

    print(f"My shape is : ({len(family)}, {ncols})")
    sliced = family[start:end]
    print(f"My new shape is : ({len(sliced)}, {ncols})")
    return [r[:] for r in sliced]


def main() -> None:
    """test from subject"""
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
