import csv
from math import log2


def calculate_entropy(data):
    """
    Calculates the entropy of a given data list using Shannon Entropy equation.

    Args:
        data: A list of data points.

    Returns:
        The entropy of the data.
    """
    entropy = 0
    for value in set(data):
        probability = data.count(value) / len(data)
        entropy -= probability * log2(probability)
    return entropy


def main():
    # Replace 'your_dataset.csv' with the actual path to your CSV file
    with open(
        "C:\External\Projects\8th Semester\Thesis\compiled\dynamic_array_allocator_disassembled\dynamic_array_allocator_diassembly.csv",
        "r",
    ) as csvfile:
        reader = csv.DictReader(csvfile)

        # Initialize empty dictionaries to store counts
        block_data = {}
        for row in reader:
            block_id = row["Block_ID"]
            if block_id not in block_data:
                block_data[block_id] = {
                    "Instruction": [],
                    "Left Operand": [],
                    "Right Operand": [],
                }
            block_data[block_id]["Instruction"].append(row["Instruction"])
            block_data[block_id]["Left Operand"].append(row["Left Operand"])
            block_data[block_id]["Right Operand"].append(row["Right Operand"])

        # Write entropy results to a new CSV file
        with open(
            "C:\External\Projects\8th Semester\Thesis\shannon_entropy\output\dynamic_array_allocator_entropy\dynamic_array_allocator_entropy_1.csv",
            "w",
            newline="",
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Block_ID", "Type", "Value", "Probability", "Entropy"])
            for block_id, block_info in block_data.items():
                for data_type, data_list in block_info.items():
                    for value in set(data_list):
                        probability = data_list.count(value) / len(data_list)
                        entropy = calculate_entropy(data_list)
                        writer.writerow(
                            [block_id, data_type, value, probability, entropy]
                        )


if __name__ == "__main__":
    main()
