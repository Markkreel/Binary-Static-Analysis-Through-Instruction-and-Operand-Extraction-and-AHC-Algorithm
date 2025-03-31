"""
This module provides functionality for analyzing similarity between binary code blocks
through distance matrix calculations and hierarchical clustering visualization.

The module reads similarity scores from CSV files, converts them to distance matrices,
and generates dendrograms to visualize the hierarchical relationships between code blocks.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


def read_similarity_matrix(input_file, block_ids):
    """
    Read a similarity matrix from a CSV file.

    Args:
        input_file (str): Path to the CSV file containing similarity scores
        block_ids (list): List of block identifiers

    Returns:
        numpy.ndarray: A square matrix where each element [i,j] represents
                      the similarity score between blocks i and j
    """
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            block_id1, block_id2, similarity = row
            i = block_ids.index(block_id1)
            j = block_ids.index(block_id2)
            similarity_matrix[i, j] = float(similarity)
            similarity_matrix[j, i] = float(similarity)
    return similarity_matrix


def similarity_to_distance(similarity_matrix):
    """
    Convert a similarity matrix to a distance matrix.

    Args:
        similarity_matrix (numpy.ndarray): Matrix containing similarity scores between elements

    Returns:
        numpy.ndarray: Distance matrix where each value represents the distance between elements,
                      calculated as the maximum similarity minus each similarity score
    """
    max_similarity = np.max(similarity_matrix)
    distance_matrix = max_similarity - similarity_matrix
    return distance_matrix


BLOCK_ID = [str(i) for i in range(1, 9)]

INPUT_FILE = (
    r"similarity\simple_calculator_block_similarity"
    r"\simple_calculator_block_similarity_normalized.csv"
)
SIMILARITY_MATRIX = read_similarity_matrix(INPUT_FILE, BLOCK_ID)

DISTANCE_MATRIX = similarity_to_distance(SIMILARITY_MATRIX)

Z = linkage(DISTANCE_MATRIX, method="ward")

plt.figure(figsize=(15, 10))
dendrogram(Z, labels=BLOCK_ID, leaf_rotation=90, leaf_font_size=8)
plt.title("Dendrogram of Block Clusters")
plt.xlabel("Block ID")
plt.ylabel("Distance")
plt.show()
