import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram
import csv


# Function to read similarity matrix from CSV file
def read_similarity_matrix(input_file, block_ids):
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(input_file, newline="") as csvfile:
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
    max_similarity = np.max(similarity_matrix)
    distance_matrix = max_similarity - similarity_matrix
    return distance_matrix


# Define the list of block IDs (replace with your actual block IDs)
block_ids = [str(i) for i in range(1, 9)]  # Example with 100 blocks


# Read the similarity matrix
input_file = "similarity\simple_calculator_block_similarity\simple_calculator_block_similarity_normalized.csv"
similarity_matrix = read_similarity_matrix(input_file, block_ids)

# Convert to distance matrix
distance_matrix = similarity_to_distance(similarity_matrix)

# Perform Agglomerative Hierarchical Clustering
Z = linkage(distance_matrix, method="ward")

# Plot dendrogram
plt.figure(figsize=(15, 10))  # Increase figure size for better readability
dendrogram(Z, labels=block_ids, leaf_rotation=90, leaf_font_size=8)
plt.title("Dendrogram of Block Clusters")
plt.xlabel("Block ID")
plt.ylabel("Distance")
plt.show()
