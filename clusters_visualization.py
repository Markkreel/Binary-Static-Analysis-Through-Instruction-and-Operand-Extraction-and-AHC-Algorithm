import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Function to read cluster assignments from a CSV file
def read_cluster_assignments(cluster_file):
    clusters = {}
    with open(cluster_file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            block_id, cluster = row
            if cluster not in clusters:
                clusters[cluster] = []
            clusters[cluster].append(block_id)
    return clusters


# Function to read entropy data from a CSV file
def read_entropy_data(entropy_file):
    entropies = {}
    with open(entropy_file, newline="") as csvfile:
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
    cluster_sizes = {}
    cluster_entropies = {}
    for cluster, block_ids in clusters.items():
        cluster_sizes[cluster] = len(block_ids)
        cluster_entropy_values = []
        for block_id in block_ids:
            if block_id in entropies:
                cluster_entropy_values.extend(entropies[block_id])
        if cluster_entropy_values:
            cluster_entropies[cluster] = np.mean(cluster_entropy_values)
        else:
            cluster_entropies[cluster] = 0  # Default to 0 if no entropy values found
    return cluster_sizes, cluster_entropies


# Function to plot cluster sizes
def plot_cluster_sizes(cluster_sizes):
    clusters = list(cluster_sizes.keys())
    sizes = [cluster_sizes[cluster] for cluster in clusters]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=clusters, y=sizes)
    plt.xlabel("Cluster #")
    plt.ylabel("Cluster Size")
    plt.title("Cluster Sizes")
    plt.show()


# Function to plot cluster entropies
def plot_cluster_entropies(cluster_entropies):
    clusters = list(cluster_entropies.keys())
    entropies = [cluster_entropies[cluster] for cluster in clusters]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=clusters, y=entropies)
    plt.xlabel("Cluster #")
    plt.ylabel("Shannon Entropy Level")
    plt.title("Cluster Entropies")
    plt.show()


# Main function
def main():
    cluster_file = "csv_parser_clusters.csv"
    entropy_file = "entropy_preprocessed\csv_parser_filtered_entropy.csv"

    # Read cluster assignments and entropy data
    clusters = read_cluster_assignments(cluster_file)
    entropies = read_entropy_data(entropy_file)

    # Calculate cluster sizes and average entropies
    cluster_sizes, cluster_entropies = calculate_cluster_statistics(clusters, entropies)

    # Plot the visualizations
    plot_cluster_sizes(cluster_sizes)
    plot_cluster_entropies(cluster_entropies)


if __name__ == "__main__":
    main()
