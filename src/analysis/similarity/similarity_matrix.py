import csv
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster


def calculate_probability_distributions(INPUT_FILE):
    block_variable_probabilities = {}
    with open(INPUT_FILE, newline="", encoding="UTF-8") as infile:
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


def calculate_kl_divergence(p, q):
    epsilon = 1e-10  # small constant to avoid log(0)
    p = np.array(p) + epsilon
    q = np.array(q) + epsilon
    return np.sum(p * np.log2(p / q))


def calculate_block_similarity(block_probabilities):
    """
    Calculate similarity between blocks based on their probability distributions.

    Args:
        block_probabilities (dict): A dictionary containing probability distributions
            for each block. The structure is:
            {block_id: {variable_type: {assembly: probability}}}

    Returns:
        dict: A dictionary containing pairwise similarities between blocks.
            The keys are tuples of block IDs (block_id1, block_id2) and
            the values are their similarity scores based on KL divergence.
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


def write_similarity_to_csv(similarity, output_file):
    with open(output_file, "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID_1", "Block_ID_2", "Similarity"])
        for (block_id1, block_id2), similarity_score in similarity.items():
            writer.writerow([block_id1, block_id2, similarity_score])


def create_similarity_matrix(similarity_dict, block_ids):
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    for (block_id1, block_id2), similarity in similarity_dict.items():
        i = block_ids.index(block_id1)
        j = block_ids.index(block_id2)
        similarity_matrix[i, j] = similarity
        similarity_matrix[j, i] = similarity  # symmetric matrix
    return similarity_matrix


INPUT_FILE = "entropy_preprocessed\hello_world_filtered_entropy.csv"
OUTPUT_FILE = "similarity_matrix.csv"
block_probabilities = calculate_probability_distributions(INPUT_FILE)
BLOCK_SIMILARITY = calculate_block_similarity(block_probabilities)
write_similarity_to_csv(BLOCK_SIMILARITY, OUTPUT_FILE)

block_ids = list(block_probabilities.keys())
similarity_matrix = create_similarity_matrix(BLOCK_SIMILARITY, block_ids)
