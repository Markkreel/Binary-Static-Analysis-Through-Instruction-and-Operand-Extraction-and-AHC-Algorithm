import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    # Load the data from the CSV files
    entropy_data = pd.read_csv("entropy_preprocessed\csv_parser_filtered_entropy.csv")
    cluster_data = pd.read_csv("clusters.csv")
    return entropy_data, cluster_data


def filter_data(entropy_data, data_type):
    # Filter the data based on the user-specified "Type"
    filtered_data = entropy_data[entropy_data["Type"] == data_type]
    return filtered_data


def merge_data(filtered_data, cluster_data):
    # Merge the filtered data with the cluster data on the "Block_ID" column
    merged_data = pd.merge(filtered_data, cluster_data, on="Block_ID")
    return merged_data


def aggregate_data(merged_data):
    # Group by "Cluster" and "Assembly", and calculate the average "Entropy"
    aggregated_data = (
        merged_data.groupby(["Cluster", "Assembly"])["Entropy"].mean().reset_index()
    )
    return aggregated_data


def plot_grouped_bar_chart(aggregated_data, data_type):
    # Pivot the data to get clusters on the X-axis and assemblies as the bar groups
    pivot_data = aggregated_data.pivot(
        index="Cluster", columns="Assembly", values="Entropy"
    )

    # Create a grouped bar chart
    pivot_data.plot(kind="bar", figsize=(12, 8), legend=False)

    plt.xlabel("Cluster ID")
    plt.ylabel("Average Entropy Level")
    plt.title(
        f"Average Entropy Level by Assembly and Cluster for {data_type} Data Points"
    )
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def main():
    # Step 1: User Input
    data_type = "Left Operand"

    # Step 2: Data Loading
    entropy_data, cluster_data = load_data()

    # Step 3: Data Filtering
    filtered_data = filter_data(entropy_data, data_type)

    # Step 4: Data Merging
    merged_data = merge_data(filtered_data, cluster_data)

    # Step 5: Data Aggregation
    aggregated_data = aggregate_data(merged_data)

    # Step 6: Bar Graph Generation
    plot_grouped_bar_chart(aggregated_data, data_type)


if __name__ == "__main__":
    main()
