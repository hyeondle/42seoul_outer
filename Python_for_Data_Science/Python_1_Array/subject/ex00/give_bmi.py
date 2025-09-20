def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """take 2 lists of integers or floats in input and returns a list
    of BMI values
    ERR : ValueError (type/size/domain)
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("height and weight must be lists of int|float.")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length.")
    bmis: list[float] = []
    for i, (h, w) in enumerate(zip(height, weight)):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("height and weight must contain only numbers.")
        if h <= 0 or w <= 0:
            raise ValueError("height and weight must be > 0.")
        bmis.append(float(w) / (float(h) * float(h)))
    return bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans.
    ERR : ValueError (Invalid Value)
    """
    if not isinstance(bmi, list):
        raise ValueError("bmi must be a list.")
    if not isinstance(limit, int):
        raise ValueError("limit must be an int.")
    for x in bmi:
        if not isinstance(x, (int, float)):
            raise ValueError("bmi must contain only numbers.")
    return [bool(x > limit) for x in bmi]


def main() -> None:
    """Test Code from Subject"""
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
