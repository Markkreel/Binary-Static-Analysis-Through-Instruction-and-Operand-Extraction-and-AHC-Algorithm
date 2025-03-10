"""
This module provides functionality for analyzing and filtering entropy data from CSV files.
It calculates entropy statistics for different variable types within blocks and applies
thresholds to filter out low entropy variables.
"""

import csv
import numpy as np


# Function to calculate entropy statistics for each variable type within each block
def calculate_variable_type_entropy_statistics(input_file):
    """
    Calculate entropy statistics for each variable type within each block from input CSV file.

    Args:
        input_file (str): Path to the input CSV file containing entropy data

    Returns:
        dict: A nested dictionary containing entropy thresholds for each variable type within each block.
              The structure is {block_id: {variable_type: threshold}}
              where threshold = mean_entropy + standard_deviation_entropy
    """
    block_variable_statistics = {}
    with open(input_file, newline="", encoding="UTF-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            block_id = row["Block_ID"]
            variable_type = row["Type"]
            entropy = float(row["Entropy"])
            if block_id not in block_variable_statistics:
                block_variable_statistics[block_id] = {}
            if variable_type not in block_variable_statistics[block_id]:
                block_variable_statistics[block_id][variable_type] = []
            block_variable_statistics[block_id][variable_type].append(entropy)

    block_variable_thresholds = {}
    for block_id, variable_statistics in block_variable_statistics.items():
        block_variable_thresholds[block_id] = {}
        for variable_type, entropies in variable_statistics.items():
            mean_entropy = np.mean(entropies)
            std_dev_entropy = np.std(entropies)
            threshold = mean_entropy + std_dev_entropy
            block_variable_thresholds[block_id][variable_type] = threshold
    return block_variable_thresholds


# Function to filter out low entropy variables for each variable type within each block
def filter_variables_by_variable_type(input_file, output_file, thresholds):
    """
    Filter variables based on entropy thresholds for each variable type within each block.

    Args:
        input_file (str): Path to the input CSV file containing entropy data
        output_file (str): Path to the output CSV file where filtered data will be written
        thresholds (dict): Dictionary containing entropy thresholds for each variable type within each block

    The function reads entropy data from the input file and writes only those entries to the
    output file where the entropy value is greater than or equal to the corresponding threshold
    for that variable type and block.
    """
    with open(input_file, newline="", encoding="UTF-8") as infile, open(
        output_file, "w", newline="", encoding="UTF-8"
    ) as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            block_id = row["Block_ID"]
            variable_type = row["Type"]
            entropy = float(row["Entropy"])
            threshold = thresholds[block_id].get(
                variable_type, 0
            )  # Default to 0 if threshold is not found
            if entropy >= threshold:
                writer.writerow(row)


# Main function
def main():
    """
    Main function that processes entropy data from CSV files.

    This function performs two main operations:
    1. Calculates entropy thresholds for each variable type within each block
    2. Filters variables based on the calculated thresholds

    The function reads from a CSV file containing entropy data and writes the filtered
    results to a new CSV file.
    """
    input_file = "entropy\csv_parser_entropy.csv"
    output_file = "entropy_preprocessed\csv_parser_filtered_entropy.csv"

    # Calculate block-wise variable type entropy statistics
    block_variable_thresholds = calculate_variable_type_entropy_statistics(input_file)
    print("Block-wise Variable Type Thresholds:", block_variable_thresholds)

    # Filter variables for each variable type within each block based on calculated thresholds
    filter_variables_by_variable_type(
        input_file, output_file, block_variable_thresholds
    )


if __name__ == "__main__":
    main()
