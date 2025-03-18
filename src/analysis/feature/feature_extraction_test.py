"""
This module provides functionality for parsing and extracting features from assembly code blocks.
It processes disassembled instruction blocks and converts them into a structured CSV format
for further analysis.
"""

import re
import csv


def parse_block(data):
    """
    Parse a block of assembly instructions and extract relevant information.

    Args:
        data (str): A string containing a block of assembly instructions with block ID
                   and tab-separated instruction details.

    Returns:
        list: A list of tuples containing parsed instruction information.
              Each tuple contains (block_id, address, instruction, left_operand, right_operand).

    The function processes a block of text that starts with a block ID in angle brackets,
    followed by lines of tab-separated assembly instruction details.
    """
    lines = data.strip().split("\n")
    block_id_match = re.search(r"<([^>]*)>", lines[0])
    if block_id_match:
        block_id = block_id_match.group(1)
    else:
        block_id = "Unknown"
    instructions = []
    for line in lines[1:]:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            address, instruction, operands = parts[0], parts[1], parts[2]
            operands = operands.split(",")
            left_operand, right_operand = operands[0], ", ".join(operands[1:])
            instructions.append(
                (block_id, address, instruction, left_operand, right_operand)
            )
        else:
            # Handle incomplete lines gracefully
            print(f"Ignoring incomplete line: {line}")
    return instructions


def main():
    """
    Main function that processes a disassembled text file containing instruction blocks
    and converts it into a structured CSV format.

    The function reads instruction blocks from the input file, parses each block to extract
    instruction details (block ID, address, instruction, operands), and writes the formatted
    data to a CSV file.

    Input file format:
    - Text file containing instruction blocks separated by blank lines
    - Each block starts with an ID in angle brackets
    - Each instruction line contains tab-separated address, instruction, and operands

    Output file format:
    - CSV file with columns: Block ID, Address, Instruction, Left Operand, Right Operand
    """
    input_file = (
        "C:\\External\\Projects\\8th Semester\\Thesis\\"
        "feature_extraction\\disassembled_test.txt"
    )
    output_file = "formatted_data.csv"

    with open(input_file, "r", encoding="UTF-8") as f:
        data = f.read()

    blocks = re.split(r"\n\s*\n", data)
    parsed_instructions = [parse_block(block) for block in blocks]

    with open(output_file, "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["Block ID", "Address", "Instruction", "Left Operand", "Right Operand"]
        )
        for instructions in parsed_instructions:
            for instruction in instructions:
                writer.writerow(instruction)


if __name__ == "__main__":
    main()
