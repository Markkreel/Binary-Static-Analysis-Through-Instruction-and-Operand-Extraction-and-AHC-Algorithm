"""
This module provides functionality for visualizing cluster data and entropy information.
It reads cluster assignments and entropy data from CSV files, calculates statistics,
and generates interactive visualizations using Plotly.
"""

import csv
import pandas as pd
import plotly.express as px


# Function to read cluster assignments from a CSV file
def read_cluster_assignments(cluster_file):
    """
    Read cluster assignments from a CSV file and organize them by cluster ID.

    Args:
        cluster_file (str): Path to the CSV file containing cluster assignments.
            The file should have two columns: block ID and cluster number.

    Returns:
        dict: A dictionary mapping cluster IDs (integers) to lists of block IDs.
            Each cluster ID maps to all block IDs assigned to that cluster.
    """
    clusters = {}
    with open(cluster_file, newline="", encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            block_id, cluster = row
            cluster = int(cluster)  # Ensure cluster is treated as integer
            if cluster not in clusters:
                clusters[cluster] = []
            clusters[cluster].append(block_id)
    return clusters


# Function to read entropy data from a CSV file
def read_entropy_data(entropy_file):
    """
    Read entropy data from a CSV file and organize it by block ID.

    Args:
        entropy_file (str): Path to the CSV file containing entropy data.
            The file should have 'Block_ID' and 'Entropy' columns.

    Returns:
        dict: A dictionary mapping block IDs to lists of entropy values.
            Each block ID can have multiple associated entropy values.
    """
    entropies = {}
    with open(entropy_file, newline="", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            block_id = row["Block_ID"]
            entropy = float(row["Entropy"])
            if block_id not in entropies:
                entropies[block_id] = []
            entropies[block_id].append(entropy)
    return entropies


# Function to calculate cluster sizes and average entropies
def calculate_cluster_statistics(clusters, entropies):
    """
    Calculate statistics for each cluster including size and average entropy.

    Args:
        clusters (dict): Dict mapping cluster IDs to lists of block IDs
        entropies (dict): Dictionary mapping block IDs to lists of entropy values

    Returns:
        tuple: A pair of dictionaries containing:
            - cluster_sizes (dict): Maps cluster IDs to number of blocks in each cluster
            - cluster_entropies (dict): Maps cluster IDs to average entropy of blocks in
                each cluster
    """
    cluster_sizes = {}
    cluster_entropies = {}
    for cluster, block_ids in clusters.items():
        cluster_sizes[cluster] = len(block_ids)
        cluster_entropy_values = []
        for block_id in block_ids:
            if block_id in entropies:
                cluster_entropy_values.extend(entropies[block_id])
        if cluster_entropy_values:
            cluster_entropies[cluster] = sum(cluster_entropy_values) / len(
                cluster_entropy_values
            )
        else:
            cluster_entropies[cluster] = 0  # Default to 0 if no entropy values found
    return cluster_sizes, cluster_entropies


# Main function
def main():
    """
    Main function that reads cluster assignments and entropy data from CSV files,
    calculates cluster statistics, and generates visualizations using Plotly.

    The function performs the following steps:
    1. Reads cluster assignments from a CSV file
    2. Reads entropy data from a CSV file
    3. Calculates cluster sizes and average entropies
    4. Creates and displays bar charts for cluster sizes and entropies
    """
    cluster_file = "clusters/csv_parser_clusters.csv"
    entropy_file = "entropy_preprocessed/csv_parser_filtered_entropy.csv"

    # Read cluster assignments and entropy data
    clusters = read_cluster_assignments(cluster_file)
    entropies = read_entropy_data(entropy_file)

    # Calculate cluster sizes and average entropies
    cluster_sizes, cluster_entropies = calculate_cluster_statistics(clusters, entropies)

    # Convert to DataFrames and sort by cluster
    cluster_sizes_df = pd.DataFrame(
        {"Cluster": list(cluster_sizes.keys()), "Size": list(cluster_sizes.values())}
    )
    cluster_sizes_df = cluster_sizes_df.sort_values(by="Cluster")

    cluster_entropies_df = pd.DataFrame(
        {
            "Cluster": list(cluster_entropies.keys()),
            "Entropy": list(cluster_entropies.values()),
        }
    )
    cluster_entropies_df = cluster_entropies_df.sort_values(by="Cluster")

    # Plot the visualizations using Plotly
    fig_cluster_sizes = px.bar(
        cluster_sizes_df, x="Cluster", y="Size", title="Cluster Sizes"
    )
    fig_cluster_sizes.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(
            family="SF Pro Display, sans-serif",  # Specify the desired font family
            size=12,  # Specify the font size
            color="black",  # Specify the font color
        ),
    )

    fig_cluster_entropies = px.bar(
        cluster_entropies_df, x="Cluster", y="Entropy", title="Cluster Entropies"
    )
    fig_cluster_entropies.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(
            family="SF Pro Display, sans-serif",  # Specify the desired font family
            size=12,  # Specify the font size
            color="black",  # Specify the font color
        ),
    )

    fig_cluster_sizes.show()
    fig_cluster_entropies.show()


if __name__ == "__main__":
    main()
