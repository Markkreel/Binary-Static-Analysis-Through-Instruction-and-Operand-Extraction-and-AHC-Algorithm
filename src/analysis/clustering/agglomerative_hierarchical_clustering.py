import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import csv
import plotly.figure_factory as ff


# Function to read similarity matrix from CSV file
def read_similarity_matrix(INPUT_FILE, block_ids):
    size = len(block_ids)
    similarity_matrix = np.zeros((size, size))
    with open(INPUT_FILE, newline="") as csvfile:
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


# Perform Agglomerative Hierarchical Clustering
def perform_ahc(distance_matrix):
    Z = linkage(distance_matrix, method="ward")
    return Z


# Plot Dendrogram
def plot_dendrogram(Z, block_ids):
    plt.figure(figsize=(15, 10))
    dendrogram(Z, labels=block_ids, leaf_rotation=90, leaf_font_size=8)
    plt.title("Dendrogram of Block Clusters")
    plt.xlabel("Block ID")
    plt.ylabel("Distance")
    plt.show()


# Create interactive dendrogram using Plotly
def plot_interactive_dendrogram(Z, block_ids):
    fig = ff.create_dendrogram(Z, labels=block_ids)
    fig.update_layout(width=1000, height=800)
    fig.show()


# Get cluster assignments
def get_cluster_assignments(Z, max_d):
    clusters = fcluster(Z, max_d, criterion="distance")
    return clusters


# Write clusters to a CSV file
def write_clusters_to_csv(block_ids, clusters, OUTPUT_FILE):
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID", "Cluster"])
        for block_id, cluster in zip(block_ids, clusters):
            writer.writerow([block_id, cluster])


# Main function
def main():
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
