"""
This module implements Agglomerative Hierarchical Clustering (AHC) on CSV data.
It performs clustering analysis using Jensen-Shannon Divergence as the distance metric
and generates dendrograms to visualize the clustering results.
"""

import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the CSV data
data = pd.read_csv(r"entropy_preprocessed\csv_parser_filtered_entropy.csv")


# Normalize probabilities within each block
def normalize_probabilities(df):
    """
    Normalize probabilities within each block and assembly type combination.

    Args:
        df (pandas.DataFrame): Input DataFrame containing Block_ID, Type, Assembly,
                             and Probability columns

    Returns:
        pandas.DataFrame: A new DataFrame with normalized probabilities where the sum
                         of probabilities for each block and assembly type combination
                         equals 1
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
    Prepare the data for clustering by creating a pivot table from the input DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame containing Block_ID, Type, Assembly,
            and Probability columns

    Returns:
        pandas.DataFrame: A pivot table with Block_ID as index, compound columns of Type and
                         and Probability values. Missing values are filled with 0.
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
        float: The Jensen-Shannon Divergence between p and q, which is a value between 0 and 1
              where 0 indicates identical distributions and 1 indicates maximally
              different distributions
    """
    p = np.asarray(p)
    q = np.asarray(q)
    m = 0.5 * (p + q)
    kl_p_m = stats.entropy(p, m)
    kl_q_m = stats.entropy(q, m)
    return 0.5 * (kl_p_m + kl_q_m)


# Calculate distance matrix using JSD
def calculate_jsd_matrix(input_data):
    """
    Calculate the Jensen-Shannon Divergence (JSD) matrix for the input data.

    Args:
        input_data: DataFrame containing the probability distributions to compare

    Returns:
        numpy.ndarray: A square matrix containing pairwise JSD distances between input
            distributions
    """
    dist_matrix = squareform(pdist(input_data, metric=jensen_shannon_divergence))
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

# Create DataFrame mapping Block_ID to Cluster
cluster_mapping = pd.DataFrame({"Block_ID": clustering_data.index, "Cluster": clusters})

# Write the DataFrame to a CSV file
cluster_mapping.to_csv(r"clusters/csv_parser_clusters.csv", index=False)
