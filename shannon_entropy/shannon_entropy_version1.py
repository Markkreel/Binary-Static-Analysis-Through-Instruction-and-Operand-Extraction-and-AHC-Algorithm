"""
This script calculates the entropy of Instructions, Left Operands, and Right Operands in a CSV dataset containing assembly code.

It utilizes the Shannon Entropy equation (H(x) = -Σ(i=1 to n)(P(xi) * log2(P(xi)))) to calculate the entropy of each distinct value within a block.
"""

import csv  # Import the csv library for working with CSV files
from math import (
    log2,
)  # Import the log2 function from the math library (used for entropy calculation)


def calculate_entropy(data):
    """
    This function calculates the entropy of a given data list using the Shannon Entropy equation.

    Args:
        data: A list containing data points.

    Returns:
        The entropy of the data.
    """
    entropy = 0  # Initialize entropy to 0
    for value in set(data):  # Iterate through unique values in the data list
        probability = data.count(value) / len(
            data
        )  # Calculate probability of the current value
        entropy -= probability * log2(
            probability
        )  # Update entropy using the probability
    return entropy  # Return the calculated entropy


def main():
    """
    This function is the main entry point of the script.
    It reads the CSV data, calculates entropy for each block, and writes the results to a new CSV file.
    """
    # Replace 'your_dataset.csv' with the actual path to your CSV file
    with open("your_dataset.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)  # Create a dictionary reader for the CSV file

        # Initialize empty dictionaries to store counts for each block
        block_data = {}
        for row in reader:  # Iterate through each row in the CSV file
            block_id = row["Block_ID"]  # Extract the Block_ID from the current row
            if (
                block_id not in block_data
            ):  # Check if this block_id has been seen before
                block_data[block_id] = {
                    "Instruction": [],
                    "Left Operand": [],
                    "Right Operand": [],
                }
                # If not seen before, create new dictionaries for Instructions, Left Operands, and Right Operands within that block_id
            block_data[block_id]["Instruction"].append(
                row["Instruction"]
            )  # Append instruction to the instruction list for the block
            block_data[block_id]["Left Operand"].append(
                row["Left Operand"]
            )  # Append left operand to the left operand list for the block
            block_data[block_id]["Right Operand"].append(
                row["Right Operand"]
            )  # Append right operand to the right operand list for the block

        # Write entropy results to a new CSV file named 'entropy_results.csv'
        with open("entropy_results.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)  # Create a CSV writer for the output file
            writer.writerow(
                ["Block_ID", "Type", "Value", "Probability", "Entropy"]
            )  # Write the header row for the output CSV
            for (
                block_id,
                block_info,
            ) in block_data.items():  # Iterate through each block_id and its data
                for (
                    data_type,
                    data_list,
                ) in (
                    block_info.items()
                ):  # Iterate through Instruction, Left Operand, and Right Operand data for each block
                    for value in set(
                        data_list
                    ):  # Iterate through unique values in the current data list
                        probability = data_list.count(value) / len(
                            data_list
                        )  # Calculate probability of the current value within the block
                        entropy = calculate_entropy(
                            data_list
                        )  # Call the calculate_entropy function to get the entropy for this value
                        writer.writerow(
                            [block_id, data_type, value, probability, entropy]
                        )  # Write the calculated data to the output CSV


if __name__ == "__main__":
    main()
