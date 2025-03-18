import re
import csv


def parse_block(data):
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
    input_file = "C:\\External\\Projects\\8th Semester\\Thesis\\feature_extraction\\disassembled_test.txt"
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
