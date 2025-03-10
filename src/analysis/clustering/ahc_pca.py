"""
This module implements Agglomerative Hierarchical Clustering (AHC) with PCA visualization.
It provides functionality to process similarity matrices, perform clustering analysis,
and visualize results using Principal Component Analysis (PCA).
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, fcluster


# Function to read similarity matrix from CSV file
def read_similarity_matrix(input_file, block_ids):
    """
    Reads a similarity matrix from a CSV file and constructs a symmetric matrix.

    Args:
        input_file (str): Path to the CSV file containing similarity scores
        block_ids (list): List of block identifiers

    Returns:
        numpy.ndarray: A symmetric similarity matrix where each element [i,j]
        represents the similarity score between blocks i and j
    """
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(input_file, newline="", encoding="UTF-8") as csvfile:
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
    Converts a similarity matrix to a distance matrix by subtracting each similarity
    value from the maximum similarity value in the matrix.

    Args:
        similarity_matrix (numpy.ndarray): Matrix containing similarity scores between data points

    Returns:
        numpy.ndarray: Distance matrix where each value represents the distance between data points
    """
    max_similarity = np.max(similarity_matrix)
    distance_matrix = max_similarity - similarity_matrix
    return distance_matrix


# Perform Agglomerative Hierarchical Clustering
def perform_ahc(distance_matrix):
    """
    Performs Agglomerative Hierarchical Clustering on the given distance matrix.

    Args:
        distance_matrix (numpy.ndarray): Matrix containing distances between data points

    Returns:
        numpy.ndarray: The linkage matrix Z describing the hierarchical clustering
    """
    Z = linkage(distance_matrix, method="ward")
    return Z


# Get cluster assignments
def get_cluster_assignments(Z, max_d):
    """
    Assigns data points to clusters based on the linkage matrix and distance threshold.

    Args:
        Z (numpy.ndarray): The linkage matrix from hierarchical clustering
        max_d (float): The distance threshold for forming flat clusters

    Returns:
        numpy.ndarray: Array of cluster assignments for each data point
    """
    clusters = fcluster(Z, max_d, criterion="distance")
    return clusters


# Function to visualize clusters using PCA
def visualize_clusters_pca(distance_matrix, clusters, block_ids):
    """
    Visualize clusters using Principal Component Analysis (PCA).

    Args:
        distance_matrix (numpy.ndarray): Matrix containing distances between blocks
        clusters (numpy.ndarray): Array containing cluster assignments for each block
        block_ids (list): List of block identifiers

    Returns:
        None: Displays a matplotlib plot showing the PCA visualization of clusters
    """
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(distance_matrix)

    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(
        principal_components[:, 0],
        principal_components[:, 1],
        c=clusters,
        cmap="viridis",
    )
    plt.colorbar(scatter, label="Cluster")
    for i, block_id in enumerate(block_ids):
        plt.annotate(
            block_id,
            (principal_components[i, 0], principal_components[i, 1]),
            fontsize=8,
        )
    plt.title("PCA of Blocks with Cluster Coloring")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.show()


# Main function
def main():
    """
    Main function that performs the following operations:
    1. Reads similarity matrix from CSV file
    2. Converts similarity matrix to distance matrix
    3. Performs Agglomerative Hierarchical Clustering
    4. Assigns clusters based on a threshold
    5. Visualizes clusters using PCA
    6. Writes cluster assignments to CSV file

    Returns:
        None
    """
    input_file = "similarity\csv_parser_block_similarity\csv_parser_filtered_block_similarity_normalized.csv"
    block_ids = [str(i) for i in range(1, 153)]  # Example with 100 blocks

    # Read the similarity matrix
    similarity_matrix = read_similarity_matrix(input_file, block_ids)

    # Convert to distance matrix
    distance_matrix = similarity_to_distance(similarity_matrix)

    # Perform Agglomerative Hierarchical Clustering
    Z = perform_ahc(distance_matrix)

    # Get cluster assignments (tune max_d to decide the cut-off)
    max_d = 0.5 * np.max(Z[:, 2])  # This is an example threshold, adjust as needed
    clusters = get_cluster_assignments(Z, max_d)
    print(f"Cluster assignments: {clusters}")

    # Visualize clusters using PCA
    visualize_clusters_pca(distance_matrix, clusters, block_ids)

    # (Optional) Write clusters to CSV
    output_file = "csv_parser_clusters_pca.csv"
    with open(output_file, "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID", "Cluster"])
        for block_id, cluster in zip(block_ids, clusters):
            writer.writerow([block_id, cluster])
    print(f"Cluster assignments written to: {output_file}")


if __name__ == "__main__":
    main()
