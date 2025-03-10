"""This module calculates the Kullback-Leibler divergence between blocks of assembly code
to measure their similarity. It processes probability distributions of variables within blocks
and outputs normalized similarity scores."""

import csv
import numpy as np


# Function to calculate probability distributions of variables within each block
def calculate_probability_distributions(input_file):
    """Calculate probability distributions of variables within assembly code blocks.

    Args:
        input_file (str): Path to the input CSV file containing block data.
            The CSV should have columns: Block_ID, Type, Assembly, Probability

    Returns:
        dict: A nested dictionary containing probability distributions for each block.
            Structure: {block_id: {variable_type: {assembly: probability}}}
            where:
            - block_id: Identifier for the code block
            - variable_type: Type of the variable/feature
            - assembly: Assembly instruction or operand
            - probability: Probability value for that assembly element
    """
    block_variable_probabilities = {}
    with open(input_file, newline="", encoding="UTF-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            block_id = row["Block_ID"]
            variable_type = row["Type"]
            probability = float(row["Probability"])
            block_variable_probabilities.setdefault(block_id, {}).setdefault(
                variable_type, {}
            )[row["Assembly"]] = probability
    return block_variable_probabilities


# Function to calculate KL-Divergence between two probability distributions
def calculate_kl_divergence(p, q):
    """Calculate the Kullback-Leibler divergence between two probability distributions.

    Args:
        p (list): First probability distribution
        q (list): Second probability distribution

    Returns:
        float: KL divergence value between distributions p and q

    Note:
        A small epsilon value is added to avoid log(0) errors
    """
    epsilon = 1e-10  # small constant to avoid log(0)
    p = np.array(p) + epsilon
    q = np.array(q) + epsilon
    return np.sum(p * np.log2(p / q))


# Function to calculate similarity between blocks using KL-Divergence
def calculate_block_similarity(block_probabilities):
    """Calculate pairwise similarity between blocks using KL-Divergence.

    Args:
        block_probabilities (dict): Dictionary containing probability distributions for each block.
            Structure: {block_id: {variable_type: {assembly: probability}}}

    Returns:
        dict: Dictionary containing pairwise similarity scores between blocks.
            Keys are tuples of (block_id1, block_id2) and values are similarity scores
            calculated using KL-divergence.
    """
    block_similarity = {}
    block_ids = list(block_probabilities.keys())
    for i, block_id1 in enumerate(block_ids):
        for block_id2 in block_ids[i + 1 :]:
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
    """Write block similarity scores to a CSV file.

    Args:
        similarity (dict): Dictionary containing pairwise block similarity scores.
            Keys are tuples of (block_id1, block_id2) and values are similarity scores.
        output_file (str): Path to the output CSV file where results will be written.

    The output CSV will have three columns:
    - Block_ID_1: ID of the first block in the pair
    - Block_ID_2: ID of the second block in the pair
    - Similarity: Calculated similarity score between the blocks
    """
    with open(output_file, "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID_1", "Block_ID_2", "Similarity"])
        writer.writerows(
            [
                (block_id1, block_id2, similarity_score)
                for (block_id1, block_id2), similarity_score in similarity.items()
            ]
        )


# Main function
def main():
    """Main function that processes assembly code blocks to calculate similarity scores.

    This function reads preprocessed entropy data from a CSV file, calculates probability
    distributions for code blocks, computes similarity scores using KL-divergence, and
    writes the results to an output CSV file.

    The input file should contain filtered entropy data for assembly code blocks.
    The output file will contain pairwise similarity scores between blocks.
    """
    input_file_filtered = "entropy_preprocessed/simple_calculator_filtered_entropy.csv"
    output_file_filtered = "simple_calculator_block_similarity_normalized.csv"

    block_probabilities_filtered = calculate_probability_distributions(
        input_file_filtered
    )
    block_similarity_filtered = calculate_block_similarity(block_probabilities_filtered)
    write_similarity_to_csv(block_similarity_filtered, output_file_filtered)
    print("Block Similarity written to:", output_file_filtered)


if __name__ == "__main__":
    main()
