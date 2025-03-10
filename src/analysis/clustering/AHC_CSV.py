import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the CSV data
data = pd.read_csv("entropy_preprocessed\csv_parser_filtered_entropy.csv")


# Normalize probabilities within each block
def normalize_probabilities(df):
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
    p = np.asarray(p)
    q = np.asarray(q)
    m = 0.5 * (p + q)
    kl_p_m = stats.entropy(p, m)
    kl_q_m = stats.entropy(q, m)
    return 0.5 * (kl_p_m + kl_q_m)


# Calculate distance matrix using JSD
def calculate_jsd_matrix(data):
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
distance_threshold = 0.5  # Set your desired distance threshold here
clusters = fcluster(linkage_matrix, t=distance_threshold, criterion="distance")

# Create DataFrame mapping Block_ID to Cluster
cluster_mapping = pd.DataFrame({"Block_ID": clustering_data.index, "Cluster": clusters})

# Write the DataFrame to a CSV file
cluster_mapping.to_csv("clusters\csv_parser_clusters.csv", index=False)
