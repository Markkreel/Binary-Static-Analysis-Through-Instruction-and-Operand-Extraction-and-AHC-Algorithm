"""
This module calculates entropy metrics for assembly code blocks.
It processes assembly instructions and operands to compute probability
distributions and entropy values, providing insights into code complexity
and patterns within basic blocks of assembly code.
"""

import csv
from collections import defaultdict
import math


# Function to calculate entropy
def calculate_entropy(probabilities):
    """
    Calculate the entropy of a probability distribution.

    Args:
        probabilities (list): A list of probability values that sum to 1.0

    Returns:
        float: The calculated entropy value using the formula: -Σ(p * log2(p))
              where p represents each probability in the distribution.
    """
    entropy = 0
    for prob in probabilities:
        if prob != 0:
            entropy -= prob * math.log2(prob)
    return entropy


# Function to calculate probability distribution and entropy
def calculate_probabilities_and_entropy(blocks):
    """
    Calculate probability distributions and entropy values for instructions and
    operands in assembly code blocks.

    Args:
        blocks (dict): A dictionary where keys are block IDs and values are lists of dictionaries
                      containing instruction and operand information for each line in the block.
                      Each dictionary has keys 'Instruction', 'Left Operand', and 'Right Operand'.

    The function writes the results to a CSV file containing:
        - Block_ID: Identifier for the basic block
        - Type: Type of assembly component (Instruction, Left Operand, or Right Operand)
        - Assembly: The actual assembly component value
        - Probability: Calculated probability of occurrence within the block
        - Entropy: Entropy value calculated for the probability
    """
    with open(
        r"entropy\dynamic_array_calculator_entropy.csv",
        "w",
        newline="",
        encoding="UTF-8",
    ) as csvfile:
        fieldnames = ["Block_ID", "Type", "Assembly", "Probability", "Entropy"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for block_id, block in blocks.items():
            total_count = len(block)
            variables = defaultdict(int)

            # Count occurrences of each variable type
            for line in block:
                variables[(line["Instruction"], "Instruction")] += 1
                if line["Left Operand"]:
                    variables[(line["Left Operand"], "Left Operand")] += 1
                if line["Right Operand"]:
                    variables[(line["Right Operand"], "Right Operand")] += 1

            # Calculate probabilities and entropies
            for (variable, variable_type), count in variables.items():
                probability = count / total_count
                entropy = calculate_entropy([probability])
                writer.writerow(
                    {
                        "Block_ID": block_id,
                        "Type": variable_type,
                        "Assembly": variable,
                        "Probability": probability,
                        "Entropy": entropy,
                    }
                )


# Function to read the assembly CSV file
def read_assembly_csv(file_path):
    """
    Read assembly code from a CSV file and organize it into blocks.

    Args:
        file_path (str): Path to the CSV file containing assembly code.

    Returns:
        defaultdict: A dictionary where keys are block IDs and values are lists of dictionaries
                    containing instruction and operand information for each line in the block.
                    Each dictionary has keys 'Instruction', 'Left Operand', and 'Right Operand'.
    """
    blocks = defaultdict(list)
    with open(file_path, newline="", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            block_id = row["Block_ID"]
            blocks[block_id].append(
                {
                    "Instruction": row["Instruction"],
                    "Left Operand": row["Left Operand"],
                    "Right Operand": row["Right Operand"],
                }
            )
    return blocks


# Main function
def main():
    """
    Main function that processes assembly code file and calculates entropy metrics.

    This function reads an assembly code file, extracts basic blocks, and calculates
    probability distributions and entropy values for instructions and operands within
    each block. Results are written to a CSV file.
    """
    assembly_file_path = (
        "compiled\\dynamic_array_allocator_disassembled\\"
        "dynamic_array_allocator_diassembly.csv"
    )
    blocks = read_assembly_csv(assembly_file_path)
    calculate_probabilities_and_entropy(blocks)


if __name__ == "__main__":
    main()
