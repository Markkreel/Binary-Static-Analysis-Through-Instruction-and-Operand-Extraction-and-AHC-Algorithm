"""
This module implements Agglomerative Hierarchical Clustering (AHC) for analyzing
binary code blocks. It provides functionality to:
- Read similarity matrices from CSV files
- Convert similarity scores to distances
- Perform hierarchical clustering
- Generate dendrograms
- Output cluster assignments

The module uses Ward's method for clustering and supports both static and
interactive visualizations of the clustering results.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import plotly.figure_factory as ff


# Function to read similarity matrix from CSV file
def read_similarity_matrix(INPUT_FILE, block_ids):
    """
    Read a similarity matrix from a CSV file.

    Args:
        INPUT_FILE (str): Path to the input CSV file containing similarity scores
        block_ids (list): List of block identifiers

    Returns:
        numpy.ndarray: A square similarity matrix where each element [i,j] represents
                      the similarity score between blocks i and j

    The function expects the CSV file to:
    - Have a header row (which is skipped)
    - Contain three columns: block_id1, block_id2, and similarity score
    - Store similarity scores for pairs of blocks
    The resulting matrix is symmetric, with identical values for [i,j] and [j,i]
    """
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(INPUT_FILE, newline="", encoding="UTF-8") as csvfile:
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
    Convert a similarity matrix to a distance matrix.

    Args:
        similarity_matrix (numpy.ndarray): A square matrix of similarity scores between data points

    Returns:
        numpy.ndarray: A distance matrix where each element represents the distance between data points,
                      calculated as the maximum similarity minus the similarity score
    """
    max_similarity = np.max(similarity_matrix)
    distance_matrix = max_similarity - similarity_matrix
    return distance_matrix


# Perform Agglomerative Hierarchical Clustering
def perform_ahc(distance_matrix):
    """
    Perform Agglomerative Hierarchical Clustering on the given distance matrix.

    Args:
        distance_matrix (numpy.ndarray): A square matrix of distances between data points

    Returns:
        numpy.ndarray: The hierarchical clustering encoded as a linkage matrix Z.
                      Each row of Z represents a clustering step, containing:
                      - Two cluster indices that were merged
                      - The distance between the clusters
                      - The number of original observations in the merged cluster
    """
    Z = linkage(distance_matrix, method="ward")
    return Z


# Plot Dendrogram
def plot_dendrogram(Z, block_ids):
    """
    Plot a dendrogram visualization of the hierarchical clustering results.

    Args:
        Z (numpy.ndarray): The hierarchical clustering encoded as a linkage matrix
        block_ids (list): List of block identifiers to use as leaf labels

    The function creates a dendrogram visualization with:
    - Figure size of 15x10 inches
    - Block IDs as leaf labels rotated 90 degrees
    - Font size of 8 for leaf labels
    - Labeled axes and title
    """
    plt.figure(figsize=(15, 10))
    dendrogram(Z, labels=block_ids, leaf_rotation=90, leaf_font_size=8)
    plt.title("Dendrogram of Block Clusters")
    plt.xlabel("Block ID")
    plt.ylabel("Distance")
    plt.show()


# Create interactive dendrogram using Plotly
def plot_interactive_dendrogram(Z, block_ids):
    """
    Create and display an interactive dendrogram using Plotly.

    Args:
        Z (numpy.ndarray): The hierarchical clustering encoded as a linkage matrix
        block_ids (list): List of block identifiers to use as labels

    The function creates an interactive dendrogram visualization with:
    - Custom width (1000px) and height (800px)
    - Block IDs as leaf labels
    - Interactive features like zoom and pan
    """
    fig = ff.create_dendrogram(Z, labels=block_ids)
    fig.update_layout(width=1000, height=800)
    fig.show()


# Get cluster assignments
def get_cluster_assignments(Z, max_d):
    """
    Get cluster assignments for data points based on hierarchical clustering results.

    Args:
        Z (numpy.ndarray): The hierarchical clustering encoded as a linkage matrix
        max_d (float): The threshold distance for forming flat clusters

    Returns:
        numpy.ndarray: An array containing cluster labels for each data point
    """
    clusters = fcluster(Z, max_d, criterion="distance")
    return clusters


# Write clusters to a CSV file
def write_clusters_to_csv(block_ids, clusters, OUTPUT_FILE):
    """
    Write cluster assignments to a CSV file.

    Args:
        block_ids (list): List of block identifiers
        clusters (numpy.ndarray): Array containing cluster assignments for each block
        OUTPUT_FILE (str): Path to the output CSV file

    The function creates a CSV file with two columns:
    - Block_ID: The identifier for each block
    - Cluster: The cluster number assigned to that block
    """
    with open(OUTPUT_FILE, "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID", "Cluster"])
        for block_id, cluster in zip(block_ids, clusters):
            writer.writerow([block_id, cluster])


# Main function
def main():
    """
    Main function that orchestrates the Agglomerative Hierarchical Clustering process.

    This function:
    1. Reads a similarity matrix from a CSV file
    2. Converts it to a distance matrix
    3. Performs hierarchical clustering
    4. Generates and displays a dendrogram
    5. Assigns clusters based on a threshold
    6. Writes the cluster assignments to a CSV file
    """
    INPUT_FILE = "similarity\csv_parser_block_similarity\csv_parser_block_similarity_normalized.csv"
    OUTPUT_FILE = "csv_parser_clusters.csv"
    block_ids = [str(i) for i in range(1, 153)]  # Example with 100 blocks

    # Read the similarity matrix
    similarity_matrix = read_similarity_matrix(INPUT_FILE, block_ids)

    # Convert to distance matrix
    distance_matrix = similarity_to_distance(similarity_matrix)

    # Perform Agglomerative Hierarchical Clustering
    Z = perform_ahc(distance_matrix)

    # Plot dendrogram
    plot_dendrogram(Z, block_ids)

    # Plot interactive dendrogram (optional)
    # plot_interactive_dendrogram(Z, block_ids)

    # Get cluster assignments (tune max_d to decide the cut-off)
    max_d = 0.5 * np.max(Z[:, 2])  # This is an example threshold, adjust as needed
    clusters = get_cluster_assignments(Z, max_d)
    print(f"Cluster assignments: {clusters}")

    # Write clusters to CSV
    write_clusters_to_csv(block_ids, clusters, OUTPUT_FILE)
    print(f"Cluster assignments written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
