import csv
from collections import defaultdict
import math


# Function to calculate entropy
def calculate_entropy(probabilities):
    entropy = 0
    for prob in probabilities:
        if prob != 0:
            entropy -= prob * math.log2(prob)
    return entropy


# Function to calculate probability distribution and entropy
def calculate_probabilities_and_entropy(blocks):
    with open(
        "entropy\dynamic_array_calculator_entropy.csv", "w", newline=""
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
    blocks = defaultdict(list)
    with open(file_path, newline="") as csvfile:
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
    assembly_file_path = "compiled\dynamic_array_allocator_disassembled\dynamic_array_allocator_diassembly.csv"
    blocks = read_assembly_csv(assembly_file_path)
    calculate_probabilities_and_entropy(blocks)


if __name__ == "__main__":
    main()
