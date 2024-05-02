import csv
import re

def extract_assembly_features(INPUT_FILE, OUTPUT_FILE):
    """
    Extracts assembly code features (address, instruction, operands) from a file
    and writes them to a CSV file.

    Args:
        INPUT_FILE (str): Path to the input assembly file.
        OUTPUT_FILE (str): Path to the output CSV file.
    """

    pattern = r"^(?P<address>[0-9a-fA-F]+):\s*(?P<instruction>\S+)\s*(?P<left_operand>(?:\(.+\))|(?:\S+))?\s*(?P<right_operand>.*)$"
    regex = re.compile(pattern)

    with open(INPUT_FILE, "r", encoding="utf-8") as file, \
         open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as csvfile:  # UTF-8 encoding

        csv_writer = csv.writer(csvfile)
        in_block = False  # Track if we're currently within an assembly block

        for line in file:
            # Skip section headers and function names
            if "Disassembly of section" in line or "<" in line:
                in_block = False
            elif ":" in line:  # Potential block start
                in_block = True

            if in_block:
                match = regex.match(line)
                if match:
                    # Extract features from the match
                    address = match.group("address")
                    instruction = match.group("instruction")
                    left_operand = match.group("left_operand") or ""
                    right_operand = match.group("right_operand") or ""
                    csv_writer.writerow([address, instruction, left_operand, right_operand])

# Example Usage (assuming you want to run this as a script)
if __name__ == "__main__":
    INPUT_FILE = "compiled/hello_world_disassembled/hello_world_disassembled.asm"
    OUTPUT_FILE = "output.csv"
    extract_assembly_features(INPUT_FILE, OUTPUT_FILE)
