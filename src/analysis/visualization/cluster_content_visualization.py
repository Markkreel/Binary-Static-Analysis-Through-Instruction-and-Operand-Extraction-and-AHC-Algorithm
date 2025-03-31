import pandas as pd
import plotly.express as px

# Read the cluster CSV file
cluster_df = pd.read_csv("clusters\csv_parser_clusters.csv")

# Read the block CSV file
block_df = pd.read_csv("entropy_preprocessed/csv_parser_filtered_entropy.csv")

# Merge the cluster and block dataframes on 'Block_ID'
merged_df = pd.merge(cluster_df, block_df, on="Block_ID")

# Group by 'Cluster' and 'Type', then count the distinct 'Assembly' values
assembly_counts = (
    merged_df.groupby(["Cluster", "Type"])["Assembly"].nunique().reset_index()
)

# Fill in missing clusters with 0 count for each 'Type'
all_clusters = set(cluster_df["Cluster"])
all_types = set(assembly_counts["Type"])
all_combinations = [(cluster, type_) for cluster in all_clusters for type_ in all_types]
assembly_counts = assembly_counts.merge(
    pd.DataFrame(all_combinations, columns=["Cluster", "Type"]),
    on=["Cluster", "Type"],
    how="right",
).fillna(0)

# Sort clusters in ascending order
assembly_counts["Cluster"] = assembly_counts["Cluster"].astype(int)
assembly_counts = assembly_counts.sort_values(by=["Cluster", "Type"])

# Apply styling configuration
layout_config = dict(
    xaxis_tickangle=-45,
    xaxis={"type": "category"},
    font=dict(
        family="SF Pro Display, sans-serif",  # Specify the desired font family
        size=12,  # Specify the font size
        color="black",  # Specify the font color
    ),
)

# Create separate graphs for each 'Type'
for type_name in assembly_counts["Type"].unique():
    type_data = assembly_counts[assembly_counts["Type"] == type_name]

    # Plot the bar graph using Plotly Express
    fig = px.bar(
        type_data,
        x="Cluster",
        y="Assembly",
        title=f"Distinct Assembly Count for Type: {type_name} (CSV Parser)",
        labels={"Cluster": "Cluster", "Assembly": "Distinct Assembly Count"},
        color_discrete_sequence=["#636EFA"],
    )  # Use a single solid color

    # Apply layout configuration
    fig.update_layout(layout_config)

    # Remove legend
    fig.update_layout(showlegend=False)

    # Show the graph
    fig.show()
