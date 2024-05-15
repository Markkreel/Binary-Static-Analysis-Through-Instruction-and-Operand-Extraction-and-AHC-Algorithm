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
# Function to calculate KL-Divergence between two probability distributions
def calculate_kl_divergence(p, q):
    kl_divergence = np.sum(np.where(p != 0, p * np.log2(p / q), 0))
    return kl_divergence if not np.isinf(kl_divergence) else 0


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
                for assembly, probability1 in probabilities1.items():
                    probability2 = probabilities2.get(assembly, 0)
                    similarity += calculate_kl_divergence(
                        np.array([probability1, probability2]),
                        np.array([probability2, probability1]),
                    )
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
    input_file = "entropy\hello_world_entropy.csv"
    output_file = "block_similarity_output.csv"

    # Calculate probability distributions of variables within each block
    block_probabilities = calculate_probability_distributions(input_file)

    # Calculate similarity between blocks using KL-Divergence
    block_similarity = calculate_block_similarity(block_probabilities)

    # Write block similarity to CSV file
    write_similarity_to_csv(block_similarity, output_file)
    print("Block Similarity written to:", output_file)


if __name__ == "__main__":
    main()
