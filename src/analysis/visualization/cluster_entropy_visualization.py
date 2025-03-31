"""
This module provides visualization functionality for cluster entropy analysis.
It reads cluster and entropy data from CSV files, processes them to calculate
average entropy values per cluster, and generates bar plots using Plotly Express
to visualize the entropy distribution across different clusters.
"""

import pandas as pd
import plotly.express as px

# Load the cluster CSV
clusters_df = pd.read_csv("clusters/csv_parser_clusters.csv")

# Load the content of each block CSV
entropy_df = pd.read_csv("entropy_preprocessed/csv_parser_filtered_entropy.csv")

# Merge the cluster information with the entropy data
merged_df = pd.merge(clusters_df, entropy_df, on="Block_ID")

# Calculate average entropy for each distinct 'Assembly' of each 'Type' for each 'Cluster'
avg_entropy_df = (
    merged_df.groupby(["Cluster", "Type", "Assembly"])["Entropy"].mean().reset_index()
)

# Sort the average entropy within each cluster and type
avg_entropy_df["rank"] = avg_entropy_df.groupby(["Cluster", "Type"])["Entropy"].rank(
    method="first", ascending=False
)

# Visualize the data using Plotly Express
for assembly_type in avg_entropy_df["Type"].unique():
    assembly_type_df = avg_entropy_df[avg_entropy_df["Type"] == assembly_type]
    fig = px.bar(
        assembly_type_df,
        x="Cluster",
        y="Entropy",
        title=f"Average Entropy of {assembly_type} by Cluster (CSV Parser)",
        labels={"Cluster": "Cluster", "Entropy": "Average Entropy"},
        color="Entropy",  # Color by entropy to create a gradient
        color_continuous_scale=px.colors.sequential.Viridis,  # Using Viridis color scale
        barmode="stack",
        template="plotly_white",
    )
    fig.update_layout(showlegend=False)
    fig.show()
