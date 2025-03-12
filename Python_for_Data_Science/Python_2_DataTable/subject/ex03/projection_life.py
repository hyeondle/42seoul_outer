import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def extract_specific_year_data(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Extracts the 1900 data along with country names from a given dataset.

    Parameters:
    df (pd.DataFrame): DataFrame containing country-wise data.

    Returns:
    pd.DataFrame: Processed DataFrame with country names and 1900 values.
    """

    if "country" not in df.columns or f"{year}" not in df.columns:
        raise ValueError(
            f"Required columns ('country', '{year}') not found in dataset.")

    return df[["country", f"{year}"]].dropna()


def plot_gdp_vs_life_expectancy(
        gdp_df: pd.DataFrame, life_df: pd.DataFrame, year: int):
    """
    Plots life expectancy vs GDP per capita for all countries in the year 1900.

    Parameters:
    gdp_df (pd.DataFrame): DataFrame containing GDP per capita for 1900.
    life_df (pd.DataFrame): DataFrame containing life expectancy for 1900.
    """

    merged_data = pd.merge(
        gdp_df, life_df, on="country", suffixes=("_gdp", "_life"))

    plt.figure(figsize=(8, 6))
    plt.scatter(
        merged_data[f"{year}_gdp"], merged_data[f"{year}_life"], alpha=0.5)

    plt.xscale("log")  # Log scale for GDP
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title(f"{year}")

    plt.show()


def main():
    gdp_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_data = load("life_expectancy_years.csv")

    if gdp_data is not None and life_data is not None:
        gdp_specific = extract_specific_year_data(gdp_data, 1900)
        life_specific = extract_specific_year_data(life_data, 1900)
        plot_gdp_vs_life_expectancy(gdp_specific, life_specific, 1900)


if __name__ == '__main__':
    main()
