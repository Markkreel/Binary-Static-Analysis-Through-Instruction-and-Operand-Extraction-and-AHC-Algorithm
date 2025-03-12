"""
This module handles the calculation and analysis of KL divergence between probability distributions.
It provides functionality to process probability data from CSV files and compute similarity metrics.
"""

import pandas as pd

# Read the CSV data
data = pd.read_csv("probability_update/simple_calculator_probability_update.csv")

# Get unique types
types = data["Type"].unique()

# Iterate over types and create separate CSV files
for t in types:
    # Filter data based on type
    type_data = data[data["Type"] == t]

    # Save filtered data to a new CSV file
    type_data.to_csv(f"{t}.csv", index=False)
