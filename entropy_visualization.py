import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Function to read the entropy CSV file and filter data for a specified block
def read_entropy_data(input_file, block_id):
    data = {"Instruction": [], "Left Operand": [], "Right Operand": []}

    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Block_ID"] == block_id:
                variable_type = row["Type"]
                assembly = row["Assembly"]
                entropy = float(row["Entropy"])
                if variable_type == "Instruction":
                    data["Instruction"].append((assembly, entropy))
                elif variable_type == "Left Operand":
                    data["Left Operand"].append((assembly, entropy))
                elif variable_type == "Right Operand":
                    data["Right Operand"].append((assembly, entropy))

    return data


# Function to encode variables by numbers starting from 1
def encode_variables(data):
    encoded_data = []
    for i, (assembly, entropy) in enumerate(data, start=1):
        encoded_data.append((i, entropy))
    return encoded_data


# Function to plot entropies for a specified variable type with threshold
def plot_entropies(data, variable_type, block_id, threshold):
    encoded_data = encode_variables(data)
    indices, entropies = zip(*encoded_data)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=indices, y=entropies)
    plt.axhline(
        y=threshold, color="r", linestyle="--", label=f"Threshold: {threshold:.2f}"
    )
    plt.xlabel(f"{variable_type} (Encoded)")
    plt.ylabel("Shannon Entropy Level")
    plt.title(f"{variable_type} Entropies for Block {block_id}")
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


# Function to calculate entropy statistics for each variable type within each block
def calculate_variable_type_entropy_statistics(input_file):
    block_variable_statistics = {}
    with open(input_file, newline="") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            block_id = row["Block_ID"]
            variable_type = row["Type"]
            entropy = float(row["Entropy"])
            if block_id not in block_variable_statistics:
                block_variable_statistics[block_id] = {}
            if variable_type not in block_variable_statistics[block_id]:
                block_variable_statistics[block_id][variable_type] = []
            block_variable_statistics[block_id][variable_type].append(entropy)

    block_variable_thresholds = {}
    for block_id, variable_statistics in block_variable_statistics.items():
        block_variable_thresholds[block_id] = {}
        for variable_type, entropies in variable_statistics.items():
            mean_entropy = np.mean(entropies)
            std_dev_entropy = np.std(entropies)
            threshold = mean_entropy + std_dev_entropy
            block_variable_thresholds[block_id][variable_type] = threshold
    return block_variable_thresholds


# Main function
def main():
    input_file = "entropy/csv_parser_entropy.csv"
    block_id = input("Enter the Block ID to visualize: ")

    # Read the entropy data for the specified block
    data = read_entropy_data(input_file, block_id)

    # Calculate block-wise variable type entropy statistics
    block_variable_thresholds = calculate_variable_type_entropy_statistics(input_file)

    # Plot the entropies for instructions, left operands, and right operands
    if data["Instruction"]:
        threshold = block_variable_thresholds[block_id]["Instruction"]
        plot_entropies(data["Instruction"], "Instruction", block_id, threshold)
    if data["Left Operand"]:
        threshold = block_variable_thresholds[block_id]["Left Operand"]
        plot_entropies(data["Left Operand"], "Left Operand", block_id, threshold)
    if data["Right Operand"]:
        threshold = block_variable_thresholds[block_id]["Right Operand"]
        plot_entropies(data["Right Operand"], "Right Operand", block_id, threshold)


if __name__ == "__main__":
    main()
