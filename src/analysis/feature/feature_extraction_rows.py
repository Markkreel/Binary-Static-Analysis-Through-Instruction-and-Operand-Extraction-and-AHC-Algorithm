"""
This code uses OS and CSV modules.
"""

import os
import csv


def parse_disassembly(disassembly_text):
    """Parses the disassembly text and extracts addresses, instructions, operands.

    Args:
        disassembly_text: The raw text of the disassembled file.

    Returns:
        A list of lists, where each inner list represents one row in the CSV:
           - [address, instruction, left_operand, right_operand]
    """

    results = []
    current_block = []

    for line in disassembly_text.splitlines():
        if line.endswith(":"):  # Address line
            if current_block:  # Store any previous block
                results.append(current_block)
            current_block = [line.split()[0]]  # Start new block with address
        elif line.strip():  # Instruction lines
            parts = (
                line.strip().split("\t")[-1].split()
            )  # Isolate instruction & operands
            current_block.extend(parts)  # Add instruction, operand(s)

    if current_block:  # Store the last block
        results.append(current_block)

    return results


# Read disassembly from file
FILE_INPUT = (
    r"C:\External\Projects\8th Semester\Thesis\feature_extraction\disassembled_test.txt"
)
with open(FILE_INPUT, "r", encoding="utf-8") as file:
    disassembly = file.read()

instructions = parse_disassembly(disassembly)

# Define output directory
OUTPUT_DIRECTORY = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# Define the output CSV file path
output_csv_file_path = os.path.join(OUTPUT_DIRECTORY, "disassembly_output_rows.csv")

with open(output_csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(instructions)

print("Output CSV file saved to:", output_csv_file_path)
