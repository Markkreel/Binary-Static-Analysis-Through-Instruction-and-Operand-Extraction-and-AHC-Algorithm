"""
This module implements Agglomerative Hierarchical Clustering (AHC) with silhouette coefficient analysis.
It processes binary analysis data, performs clustering using Jensen-Shannon Divergence as a distance metric,
and evaluates cluster quality using silhouette coefficients.
"""

import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the CSV data
data = pd.read_csv("entropy_preprocessed\csv_parser_filtered_entropy.csv")


# Normalize probabilities within each block
def normalize_probabilities(df):
    """
    Normalize probabilities within each block and assembly type combination.

    Args:
        df (pandas.DataFrame): Input DataFrame containing Block_ID, Type, and
            Probability columns.

    Returns:
        pandas.DataFrame: A new DataFrame with normalized probability values where
            the sum of probabilities for each block-type combination equals 1.
    """
    normalized_df = df.copy()
    for block_id in normalized_df["Block_ID"].unique():
        for assembly_type in normalized_df["Type"].unique():
            mask = (normalized_df["Block_ID"] == block_id) & (
                normalized_df["Type"] == assembly_type
            )
            prob_sum = normalized_df.loc[mask, "Probability"].sum()
            normalized_df.loc[mask, "Probability"] = (
                normalized_df.loc[mask, "Probability"] / prob_sum
            )
    return normalized_df


normalized_data = normalize_probabilities(data)
normalized_data = normalized_data.drop(columns=["Entropy"])


# Prepare data for clustering
def prepare_data_for_clustering(df):
    """
    Prepare data for clustering by creating a pivot table from the input DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing Block_ID, Type, Assembly,
            and Probability columns.

    Returns:
        pandas.DataFrame: A pivot table with Block_ID as index, Type-Assembly combinations
            as columns, and Probability values as entries. Missing values are filled with 0.
    """
    pivot_df = df.pivot_table(
        index="Block_ID",
        columns=["Type", "Assembly"],
        values="Probability",
        fill_value=0,
    )
    return pivot_df


clustering_data = prepare_data_for_clustering(normalized_data)


# Function to calculate Jensen-Shannon Divergence
def jensen_shannon_divergence(p, q):
    """
    Calculate the Jensen-Shannon Divergence between two probability distributions.

    Args:
        p (array-like): First probability distribution
        q (array-like): Second probability distribution

    Returns:
        float: Jensen-Shannon Divergence value between p and q

    Note:
        The Jensen-Shannon Divergence is a symmetrized and smoothed version of the
        Kullback-Leibler divergence. It is always finite and bounded between 0 and 1.
    """
    p = np.asarray(p)
    q = np.asarray(q)
    m = 0.5 * (p + q)
    kl_p_m = stats.entropy(p, m)
    kl_q_m = stats.entropy(q, m)
    return 0.5 * (kl_p_m + kl_q_m)


# Calculate distance matrix using JSD
def calculate_jsd_matrix(data):
    """
    Calculate the Jensen-Shannon Divergence distance matrix for the given data.

    Args:
        data (pandas.DataFrame): Input data matrix where rows represent blocks and
            columns represent features.

    Returns:
        numpy.ndarray: A square distance matrix containing pairwise JSD distances
            between all blocks.
    """
    dist_matrix = squareform(pdist(data, metric=jensen_shannon_divergence))
    return dist_matrix


distance_matrix = calculate_jsd_matrix(clustering_data)

# Perform Agglomerative Hierarchical Clustering
linkage_matrix = linkage(distance_matrix, method="average")

# Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix, labels=clustering_data.index, leaf_rotation=90)
plt.title("Agglomerative Hierarchical Clustering using JSD")
plt.xlabel("Block ID")
plt.ylabel("Distance (JSD)")
plt.show()

# Cut the dendrogram into clusters
DISTANCE_THRESHOLD = 0.5  # Set your desired distance threshold here
clusters = fcluster(linkage_matrix, t=DISTANCE_THRESHOLD, criterion="distance")

# Calculate Silhouette Coefficients for each block
silhouette_values = silhouette_samples(distance_matrix, clusters, metric="precomputed")
average_silhouette_score = silhouette_score(
    distance_matrix, clusters, metric="precomputed"
)

# Add Silhouette Coefficients to the DataFrame
silhouette_df = pd.DataFrame(
    {"Block_ID": clustering_data.index, "Silhouette_Coefficient": silhouette_values}
)

# Print Silhouette Coefficients for each block
print(silhouette_df)

# Plot Silhouette Coefficients
plt.figure(figsize=(10, 7))
plt.barh(silhouette_df["Block_ID"], silhouette_df["Silhouette_Coefficient"])
plt.axvline(average_silhouette_score, color="red", linestyle="--")
plt.title("Silhouette Coefficients for Each Block")
plt.xlabel("Silhouette Coefficient")
plt.ylabel("Block ID")
plt.show()

# Create DataFrame mapping Block_ID to Cluster
cluster_mapping = pd.DataFrame({"Block_ID": clustering_data.index, "Cluster": clusters})

# Write the DataFrame to a CSV file
cluster_mapping.to_csv("cluster_mapping.csv", index=False)
