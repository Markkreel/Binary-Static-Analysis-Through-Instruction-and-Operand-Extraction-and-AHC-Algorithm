import re
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
        if line.endswith(':'):  # Address line
            current_addr = line.split()[0]
            results[current_addr] = []
        elif line.strip():  # Instruction lines
            parts = line.strip().split('\t')[-1].split() 
            results[current_addr].append(parts)

    return results
  
# Read disassembly from file
disassembly_file_path = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\disassembled_test.txt"
with open(disassembly_file_path, 'r') as file:
    disassembly = file.read()

# Process the disassembly
instructions = parse_disassembly(disassembly)

# Export to CSV 
with open('disassembly_output_columns.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row (block addresses)
    writer.writerow(instructions.keys())

    # Transpose data for writing rows
    max_row_length = max(len(instructions[addr]) for addr in instructions)
    for i in range(max_row_length):
        row = []
        for addr in instructions:
            if i < len(instructions[addr]):
                row.extend(instructions[addr][i])  # Add instruction/operands
            else:
                row.append('')  # Fill blank cells
        writer.writerow(row)
