"""
Imports
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram


# Function to read similarity matrix from CSV file
def read_similarity_matrix(input_file, block_ids):
    """
    Calculate similarity matrix
    """
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            block_id1, block_id2, similarity = row
            i = block_ids.index(block_id1)
            j = block_ids.index(block_id2)
            similarity_matrix[i, j] = float(similarity)
            similarity_matrix[j, i] = float(similarity)  # symmetric matrix
    return similarity_matrix


# Convert similarity matrix to distance matrix
def similarity_to_distance(similarity_matrix):
    """
    Converting similarity matrix to distance values
    """
    max_similarity = np.max(similarity_matrix)
    distance_matrix = max_similarity - similarity_matrix
    return distance_matrix


# Define the list of block IDs (replace with your actual block IDs)
BLOCK_ID = [str(i) for i in range(1, 9)]  # Example with 100 blocks


# Read the similarity matrix
INPUT_FILE = r"similarity\simple_calculator_block_similarity\simple_calculator_block_similarity_normalized.csv"
SIMILARITY_MATRIX = read_similarity_matrix(INPUT_FILE, BLOCK_ID)

# Convert to distance matrix
DISTANCE_MATRIX = similarity_to_distance(SIMILARITY_MATRIX)

# Perform Agglomerative Hierarchical Clustering
Z = linkage(DISTANCE_MATRIX, method="ward")

# Plot dendrogram
plt.figure(figsize=(15, 10))  # Increase figure size for better readability
dendrogram(Z, labels=BLOCK_ID, leaf_rotation=90, leaf_font_size=8)
plt.title("Dendrogram of Block Clusters")
plt.xlabel("Block ID")
plt.ylabel("Distance")
plt.show()
