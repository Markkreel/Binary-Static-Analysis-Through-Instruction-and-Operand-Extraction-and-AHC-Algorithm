import pandas as pd
import plotly.express as px

# Load the cluster CSV
clusters_df = pd.read_csv("clusters\csv_parser_clusters.csv")

# Load the content of each block CSV
entropy_df = pd.read_csv("entropy_preprocessed\csv_parser_filtered_entropy.csv")

# Merge the cluster information with the entropy data
merged_df = pd.merge(clusters_df, entropy_df, on="Block_ID")

# Calculate average entropy for each distinct 'Assembly' of each 'Type' for each 'Cluster'
avg_entropy_df = (
    merged_df.groupby(["Cluster", "Type", "Assembly"])["Entropy"].mean().reset_index()
)

# Define custom color scale based on entropy levels
color_scale = [
    (0, "#FF0000"),
    (0.5, "#EC00FF"),
    (1, "#0080FF"),
]  # Low entropy to high entropy

# Visualize the data using Plotly Express
for assembly_type in avg_entropy_df["Type"].unique():
    assembly_type_df = avg_entropy_df[avg_entropy_df["Type"] == assembly_type]
    fig = px.bar(
        assembly_type_df,
        x="Cluster",
        y="Entropy",
        title=f"Average Entropy of {assembly_type} by Cluster",
        labels={"Cluster": "Cluster", "Entropy": "Average Entropy"},
        color="Entropy",
        color_continuous_scale=color_scale,  # Using custom color scale
        barmode="stack",
        template="plotly_white",
    )
    fig.update_layout(showlegend=False)
    fig.show()
