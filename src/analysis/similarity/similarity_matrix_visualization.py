"""
This module provides functionality for visualizing similarity matrices between binary code blocks.
It reads similarity data from CSV files and generates heatmap visualizations using matplotlib and seaborn.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Function to read similarity matrix from CSV file and generate block IDs
def read_similarity_matrix(input_file):
    block_ids = set()
    similarities = []
    with open(input_file, newline="", encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            block_id1, block_id2, similarity = row
            block_ids.add(block_id1)
            block_ids.add(block_id2)
            similarities.append((block_id1, block_id2, float(similarity)))
    block_ids = sorted(block_ids)  # Sort block IDs
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    for block_id1, block_id2, similarity in similarities:
        i = block_ids.index(block_id1)
        j = block_ids.index(block_id2)
        similarity_matrix[i, j] = similarity
        similarity_matrix[j, i] = similarity  # symmetric matrix
    return similarity_matrix, block_ids


# Read the similarity matrix and block IDs
INPUT_FILE = "probability_update\simple_calculator_probability_update.csv"
similarity_matrix, block_ids = read_similarity_matrix(INPUT_FILE)

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    similarity_matrix,
    xticklabels=block_ids,
    yticklabels=block_ids,
    cmap="viridis",
    annot=True,
    fmt=".2f",
)
plt.title("Block Similarity Matrix Heatmap")
plt.xlabel("Block ID")
plt.ylabel("Block ID")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
