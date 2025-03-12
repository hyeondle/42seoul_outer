import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(data: pd.DataFrame, country: str):
    """
    Plots the life expectancy data for a given country.

    Parameters:
    data (pd.DataFrame): The DataFrame containing life expectancy data.
    country (str): The name of the country whose data should be plotted.
    """
    if country not in data["country"].values:
        print(f"Error: '{country}' not found in the dataset.")
        return

    country_data = (
        data[data["country"] == country]
        .iloc[:, 1:]
        .T
    )
    country_data.columns = ["Life Expectancy"]
    years = country_data.index.astype(int)

    plt.figure(figsize=(7, 5))
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    plt.plot(years, country_data["Life Expectancy"], linestyle='-')

    plt.xticks(range(1800, 2081, 40))
    plt.yticks(range(30, 91, 10))

    plt.show()


def main():
    data = load("life_expectancy_years.csv")
    if data is not None:
        plot_life_expectancy(data, "South Korea")


if __name__ == '__main__':
    main()
