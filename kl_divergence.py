import csv
import numpy as np


# Function to calculate probability distributions of variables within each block
def calculate_probability_distributions(input_file):
    block_variable_probabilities = {}
    with open(input_file, newline="") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            block_id = row["Block_ID"]
            variable_type = row["Type"]
            probability = float(row["Probability"])
            if block_id not in block_variable_probabilities:
                block_variable_probabilities[block_id] = {}
            if variable_type not in block_variable_probabilities[block_id]:
                block_variable_probabilities[block_id][variable_type] = {}
            block_variable_probabilities[block_id][variable_type][
                row["Assembly"]
            ] = probability
    return block_variable_probabilities


# Function to calculate KL-Divergence between two probability distributions
def calculate_kl_divergence(p, q):
    epsilon = 1e-10  # small constant to avoid log(0)
    p = np.array(p) + epsilon
    q = np.array(q) + epsilon
    return np.sum(p * np.log2(p / q))


# Function to calculate similarity between blocks using KL-Divergence
def calculate_block_similarity(block_probabilities):
    block_similarity = {}
    block_ids = list(block_probabilities.keys())
    for i in range(len(block_ids)):
        for j in range(i + 1, len(block_ids)):
            block_id1 = block_ids[i]
            block_id2 = block_ids[j]
            similarity = 0
            for variable_type, probabilities1 in block_probabilities[block_id1].items():
                probabilities2 = block_probabilities[block_id2].get(variable_type, {})
                all_assemblies = set(probabilities1.keys()).union(probabilities2.keys())
                p = [probabilities1.get(assembly, 0) for assembly in all_assemblies]
                q = [probabilities2.get(assembly, 0) for assembly in all_assemblies]
                similarity += calculate_kl_divergence(p, q)
            block_similarity[(block_id1, block_id2)] = similarity
    return block_similarity


# Function to write block similarity to a CSV file
def write_similarity_to_csv(similarity, output_file):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID_1", "Block_ID_2", "Similarity"])
        for (block_id1, block_id2), similarity_score in similarity.items():
            writer.writerow([block_id1, block_id2, similarity_score])


# Main function
def main():
    input_file = "entropy/hello_world_entropy.csv"
    input_file_filtered = "entropy_preprocessed/hello_world_filtered_entropy.csv"
    output_file = "similarity/hello_world_block_similarity.csv"
    output_file_filtered = "similarity/hello_world_filtered_block_similarity.csv"

    # Calculate probability distributions of variables within each block
    block_probabilities = calculate_probability_distributions(input_file)
    block_probabilities_filtered = calculate_probability_distributions(
        input_file_filtered
    )

    # Calculate similarity between blocks using KL-Divergence
    block_similarity = calculate_block_similarity(block_probabilities)
    block_similarity_filtered = calculate_block_similarity(block_probabilities_filtered)

    # Write block similarity to CSV file
    write_similarity_to_csv(block_similarity, output_file)
    print("Block Similarity written to:", output_file)

    write_similarity_to_csv(block_similarity_filtered, output_file_filtered)
    print("Block Similarity written to:", output_file_filtered)


if __name__ == "__main__":
    main()
