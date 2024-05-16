import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, fcluster
import seaborn as sns
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


# Perform Agglomerative Hierarchical Clustering
def perform_ahc(distance_matrix):
    Z = linkage(distance_matrix, method="ward")
    return Z


# Get cluster assignments
def get_cluster_assignments(Z, max_d):
    clusters = fcluster(Z, max_d, criterion="distance")
    return clusters


# Function to visualize clusters using PCA
def visualize_clusters_pca(distance_matrix, clusters, block_ids):
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
    input_file = "similarity\simple_calculator_block_similarity\simple_calculator_filtered_block_similarity_normalized.csv"
    block_ids = [str(i) for i in range(1, 9)]  # Example with 100 blocks

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
    output_file = "clusters_pca.csv"
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Block_ID", "Cluster"])
        for block_id, cluster in zip(block_ids, clusters):
            writer.writerow([block_id, cluster])
    print(f"Cluster assignments written to: {output_file}")


if __name__ == "__main__":
    main()
