import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame

    :param path: str, path to the CSV file
    :return: pd.DataFrame, the loaded data
    """
    try:
        data = pd.read_csv(path)
        rows, cols = data.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")
        return data
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    print(load("life_expectancy_years.csv"))
    return


if __name__ == '__main__':
    main()
