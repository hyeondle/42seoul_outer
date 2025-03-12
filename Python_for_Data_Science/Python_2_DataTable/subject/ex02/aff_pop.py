import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """
    Converts population values
    from 'M' (millions) and 'k' (thousands) to integers.

    Parameters:
    value (str): The population value to convert.

    Returns:
    float: The converted population value.
    """
    if isinstance(value, str):
        if "M" in value:
            return float(value.replace("M", "")) * 1_000_000
        elif "k" in value:
            return float(value.replace("k", "")) * 1_000
    return float(value)


def aff_pop(data: pd.DataFrame, country1: str, country2: str):
    """
    Plots the population data for two given countries.

    Parameters:
    data (pd.DataFrame): The DataFrame containing population data.
    country1 (str): The name of the first country to plot.
    country2 (str): The name of the second country to plot.
    """
    if country1 not in data["country"].values:
        print(f"Error: '{country1}' not found in the dataset.")
        return
    if country2 not in data["country"].values:
        print(f"Error: '{country2}' not found in the dataset.")
        return

    # Extract country data including year columns
    country1_data = data[data["country"] == country1].iloc[:, 1:].T
    country1_data.columns = ["Population"]
    country1_data.index = country1_data.index.astype(int)
    country1_data = country1_data.loc[1800:2050]
    country1_data["Population"] = (
        country1_data["Population"]
        .apply(convert_population)
    )

    country2_data = data[data["country"] == country2].iloc[:, 1:].T
    country2_data.columns = ["Population"]
    country2_data.index = country2_data.index.astype(int)
    country2_data = country2_data.loc[1800:2050]
    country2_data["Population"] = (
        country2_data["Population"]
        .apply(convert_population)
    )

    plt.figure(figsize=(7, 5))
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.plot(
        country1_data.index,
        country1_data["Population"],
        linestyle='-',
        label=country1
    )
    plt.plot(
        country2_data.index,
        country2_data["Population"],
        linestyle='-',
        label=country2
    )
    plt.legend()

    plt.xticks(range(1800, 2051, 40))
    plt.yticks(
        range(20_000_000, 61_000_000, 20_000_000),
        ["20M", "40M", "60M"]
    )
    plt.show()


def main():
    data = load("population_total.csv")
    if data is not None:
        aff_pop(data, "France", "Belgium")


if __name__ == '__main__':
    main()
