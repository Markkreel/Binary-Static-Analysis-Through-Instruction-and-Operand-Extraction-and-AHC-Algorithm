"""
This module handles CSV file operations for address data formatting.
It reads a CSV file, modifies address values by adding leading zeros,
and saves the updated data to a new CSV file.
"""

import pandas as pd

# Define input and output file paths (modify as needed)
INPUT_FILE = (
    r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output"
    r"updated_formatted_data.csv"
)
OUTPUT_FILE = (
    r"C:\External\Projects\8th Semester\Thesis\feature_extraction"
    r"output\updated_formatted_data.csv"
)

# Read the CSV data
df = pd.read_csv(INPUT_FILE)

# Modify the second column (Address)
df["Address"] = "000000000000" + df["Address"]

# Save the updated data to a new CSV file
df.to_csv(OUTPUT_FILE, index=False)

print("CSV file updated successfully!")
