import csv  # Importing the CSV module to read and write CSV files
import math  # Importing the math module to perform mathematical calculations


def calculate_entropy(probabilities):
    """
    Calculate the Shannon entropy given a list of probabilities.

    Args:
        probabilities (list): List of probabilities.

    Returns:
        float: Shannon entropy value.
    """
    entropy = 0
    for prob in probabilities:
        if prob != 0:
            entropy -= prob * math.log(prob, 2)
    return entropy


# Read the CSV file and compute probabilities and entropies
with open(
    r"C:\External\Projects\8th Semester\Thesis\compiled\csv_parser_disassembled\csv_parser_disassembly.csv",
    newline="",
) as csvfile:
    reader = csv.DictReader(csvfile)  # Creating a CSV reader object

    # Initialize dictionaries to store probabilities and counts
    instruction_counts = {}  # Dictionary to store counts of instructions
    left_operand_counts = {}  # Dictionary to store counts of left operands
    right_operand_counts = {}  # Dictionary to store counts of right operands
    block_counts = {}  # Dictionary to store counts of block IDs

    # Count occurrences of each instruction, left operand, right operand, and block ID
    for row in reader:
        block_id = int(row["Block_ID"])  # Extracting block ID from the row
        instruction = row["Instruction"]  # Extracting instruction from the row
        left_operand = row["Left Operand"]  # Extracting left operand from the row
        right_operand = row["Right Operand"]  # Extracting right operand from the row

        # Update block counts
        block_counts[block_id] = block_counts.get(block_id, 0) + 1

        # Update instruction counts
        instruction_counts[(block_id, instruction)] = (
            instruction_counts.get((block_id, instruction), 0) + 1
        )

        # Update left operand counts
        left_operand_counts[(block_id, left_operand)] = (
            left_operand_counts.get((block_id, left_operand), 0) + 1
        )

        # Update right operand counts
        right_operand_counts[(block_id, right_operand)] = (
            right_operand_counts.get((block_id, right_operand), 0) + 1
        )

# Calculate probabilities and entropies for each instruction, left operand, and right operand
results = []

for block_id, count in block_counts.items():
    for (b_id, instruction), instruction_count in instruction_counts.items():
        if b_id == block_id:
            probability = instruction_count / count
            entropy = calculate_entropy([probability])
            results.append((block_id, "Instruction", instruction, probability, entropy))

    for (b_id, left_operand), left_operand_count in left_operand_counts.items():
        if b_id == block_id:
            probability = left_operand_count / count
            entropy = calculate_entropy([probability])
            results.append(
                (block_id, "Left Operand", left_operand, probability, entropy)
            )

    for (b_id, right_operand), right_operand_count in right_operand_counts.items():
        if b_id == block_id:
            probability = right_operand_count / count
            entropy = calculate_entropy([probability])
            results.append(
                (block_id, "Right Operand", right_operand, probability, entropy)
            )

# Write results to a new CSV file
with open("entropy_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Block_ID", "Type", "Value", "Probability", "Entropy"]
    )  # Writing header row
    writer.writerows(results)  # Writing results to the CSV file
