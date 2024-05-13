"""
This code uses the OS and CSV modules.
"""

import os
import csv


def parse_disassembly(disassembly_text):
    """Parses the disassembly text.

    Args:
        disassembly_text: The raw text of the disassembled file.

    Returns:
        A dictionary where:
            - Keys: Block addresses
            - Values: A list of instructions/operands from each line of the block
    """
    results = {}
    current_addr = None

    for line in disassembly_text.splitlines():
        if line.endswith(":"):  # Address line
            current_addr = line.split()[0]
            results[current_addr] = []
        elif line.strip():  # Instruction lines
            parts = line.strip().split("\t")[-1].split()
            results[current_addr].append(parts)

    return results


# Read disassembly from file
INPUT_FILE = (
    r"C:\External\Projects\8th Semester\Thesis\feature_extraction\disassembled_test.txt"
)
with open(INPUT_FILE, "r", encoding="utf-8") as file:
    disassembly = file.read()

# Process the disassembly
instructions = parse_disassembly(disassembly)

# Define output directory
OUTPUT_DIRECTORY = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

# Define the output CSV file path
output_csv_file_path = os.path.join(OUTPUT_DIRECTORY, "disassembly_output_columns.csv")

# Export to CSV
with open(output_csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row (block addresses)
    writer.writerow(instructions.keys())

    # Transpose data for writing rows
    max_row_length = max(len(instruction) for addr, instruction in instructions.items())
    for i in range(max_row_length):
        row = []
        for addr, instruction in instructions.items():
            if i < len(instructions[addr]):
                row.extend(instructions[addr][i])  # Add instruction/operands
            else:
                row.append("")  # Fill blank cells
        writer.writerow(row)

print("Output CSV file saved to:", output_csv_file_path)
