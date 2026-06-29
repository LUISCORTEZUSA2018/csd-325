"""
Module 4.2 Assignment – High/Low Temperatures
Student: Luis Cortez
Program: sitka_high_low_lc.py

This program reads Sitka weather data from a CSV file and allows the user
to display either high temperatures, low temperatures, or exit the program.
"""

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt


filename = "sitka_weather_2018_simple.csv"

# Read dates, high temperatures, and low temperatures from the CSV file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    highs = []
    lows = []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)


def plot_temperatures(temperatures, color, title):
    """Create and display a temperature graph."""
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()

    ax.plot(dates, temperatures, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


while True:
    print("\nSitka Weather Menu")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("\nPlease select an option: ")

    if choice == "1":
        plot_temperatures(highs, "red", "Daily high temperatures - 2018")

    elif choice == "2":
        plot_temperatures(lows, "blue", "Daily low temperatures - 2018")

    elif choice == "3":
        print("\nThank you for using the Sitka Weather program. Goodbye!")
        sys.exit()

    else:
        print("\nInvalid option. Please select 1, 2, or 3.")