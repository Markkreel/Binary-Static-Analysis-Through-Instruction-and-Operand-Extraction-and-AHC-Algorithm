"""
This module provides functionality for visualizing entropy data from binary analysis.
It reads entropy values from CSV files and creates visualizations using matplotlib
and seaborn to display entropy distributions for instructions and operands across
different code blocks.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Function to read the entropy CSV file and filter data for a specified block
def read_entropy_data(input_file, block_id):
    """
    Reads entropy data from a CSV file and filters it for a specified block ID.

    Args:
        input_file (str): Path to the CSV file containing entropy data
        block_id (str): ID of the block to filter data for

    Returns:
        dict: Dictionary containing filtered entropy data with keys 'Instruction',
             'Left Operand', and 'Right Operand'. Each key maps to a list of
             tuples containing (assembly, entropy) pairs.
    """
    data = {"Instruction": [], "Left Operand": [], "Right Operand": []}

    with open(input_file, newline="", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Block_ID"] == block_id:
                variable_type = row["Type"]
                assembly = row["Assembly"]
                entropy = float(row["Entropy"])
                if variable_type == "Instruction":
                    data["Instruction"].append((assembly, entropy))
                elif variable_type == "Left Operand":
                    data["Left Operand"].append((assembly, entropy))
                elif variable_type == "Right Operand":
                    data["Right Operand"].append((assembly, entropy))

    return data


# Function to encode variables by numbers starting from 1
def encode_variables(data):
    """
    Encodes variables by assigning sequential numbers starting from 1.

    Args:
        data (list): List of tuples containing (assembly, entropy) pairs

    Returns:
        list: List of tuples containing (index, entropy) pairs where index
              is the sequential number assigned to each variable
    """
    encoded_data = []
    for i, (_, entropy) in enumerate(data, start=1):
        encoded_data.append((i, entropy))
    return encoded_data


# Function to plot entropies for a specified variable type with threshold
def plot_entropies(data, variable_type, block_id, threshold):
    """
    Creates a bar plot visualization of entropy values for a specific variable type.

    Args:
        data (list): List of tuples containing (assembly, entropy) pairs
        variable_type (str): Type of variable being plotted (Instruction, Left Operand, or Right Operand)
        block_id (str): ID of the code block being analyzed
        threshold (float): Threshold value for entropy visualization

    Returns:
        None: Displays the plot using matplotlib
    """
    encoded_data = encode_variables(data)
    indices, entropies = zip(*encoded_data)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=indices, y=entropies)
    plt.axhline(
        y=threshold, color="r", linestyle="--", label=f"Threshold: {threshold:.2f}"
    )
    plt.xlabel(f"{variable_type} (Encoded)")
    plt.ylabel("Shannon Entropy Level")
    plt.title(f"{variable_type} Entropies for Block {block_id}")
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


# Function to calculate entropy statistics for each variable type within each block
def calculate_variable_type_entropy_statistics(input_file):
    """
    Calculates entropy statistics for each variable type within each code block.

    Args:
        input_file (str): Path to the CSV file containing entropy data

    Returns:
        dict: A nested dictionary containing entropy thresholds for each variable type
              within each block. The structure is:
              {block_id: {variable_type: threshold}}
              where threshold = mean entropy + standard deviation
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


# Main function
def main():
    """
    Main function that handles the entropy visualization workflow.

    Prompts the user for a Block ID, reads entropy data for that block,
    calculates entropy thresholds, and generates visualization plots for
    instructions and operands if data is available.

    The function processes data from a CSV file containing entropy values
    and creates separate plots for instructions, left operands, and right
    operands using the calculated threshold values.
    """
    input_file = "entropy\csv_parser_entropy.csv"
    block_id = input("Enter the Block ID to visualize: ")

    # Read the entropy data for the specified block
    data = read_entropy_data(input_file, block_id)

    # Calculate block-wise variable type entropy statistics
    block_variable_thresholds = calculate_variable_type_entropy_statistics(input_file)

    # Plot the entropies for instructions, left operands, and right operands
    if data["Instruction"]:
        threshold = block_variable_thresholds[block_id]["Instruction"]
        plot_entropies(data["Instruction"], "Instruction", block_id, threshold)
    if data["Left Operand"]:
        threshold = block_variable_thresholds[block_id]["Left Operand"]
        plot_entropies(data["Left Operand"], "Left Operand", block_id, threshold)
    if data["Right Operand"]:
        threshold = block_variable_thresholds[block_id]["Right Operand"]
        plot_entropies(data["Right Operand"], "Right Operand", block_id, threshold)


if __name__ == "__main__":
    main()
