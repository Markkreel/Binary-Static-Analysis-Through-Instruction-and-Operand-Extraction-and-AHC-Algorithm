import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """
    Loads entropy and cluster data from CSV files.

    Returns:
        tuple: A tuple containing two pandas DataFrames:
            - entropy_data: DataFrame containing entropy information
            - cluster_data: DataFrame containing cluster assignments
    """
    # Load the data from the CSV files
    entropy_data = pd.read_csv("entropy_preprocessed\csv_parser_filtered_entropy.csv")
    cluster_data = pd.read_csv("clusters.csv")
    return entropy_data, cluster_data


def filter_data(entropy_data, data_type):
    """
    Filters the entropy data based on the specified data type.

    Args:
        entropy_data (pandas.DataFrame): DataFrame containing entropy data
            with a 'Type' column
        data_type (str): The type of data to filter for (e.g., 'Left Operand')

    Returns:
        pandas.DataFrame: Filtered DataFrame containing only rows where
            'Type' matches the specified data_type
    """
    # Filter the data based on the user-specified "Type"
    filtered_data = entropy_data[entropy_data["Type"] == data_type]
    return filtered_data


def merge_data(filtered_data, cluster_data):
    """
    Merges filtered entropy data with cluster data based on Block_ID.

    Args:
        filtered_data (pandas.DataFrame): DataFrame containing filtered entropy data
            with a 'Block_ID' column
        cluster_data (pandas.DataFrame): DataFrame containing cluster assignments
            with a 'Block_ID' column

    Returns:
        pandas.DataFrame: Merged DataFrame containing both entropy and cluster data
    """
    # Merge the filtered data with the cluster data on the "Block_ID" column
    merged_data = pd.merge(filtered_data, cluster_data, on="Block_ID")
    return merged_data


def aggregate_data(merged_data):
    """
    Aggregates the merged data by grouping it by Cluster and Assembly, calculating the mean Entropy.

    Args:
        merged_data (pandas.DataFrame): DataFrame containing merged entropy and cluster data
            with columns 'Cluster', 'Assembly', and 'Entropy'

    Returns:
        pandas.DataFrame: Aggregated DataFrame with columns 'Cluster', 'Assembly', and mean 'Entropy'
    """
    # Group by "Cluster" and "Assembly", and calculate the average "Entropy"
    aggregated_data = (
        merged_data.groupby(["Cluster", "Assembly"])["Entropy"].mean().reset_index()
    )
    return aggregated_data


def plot_grouped_bar_chart(aggregated_data, data_type):
    """
    Create a grouped bar chart visualization of average entropy levels by assembly and cluster.

    Args:
        aggregated_data (pandas.DataFrame): DataFrame containing aggregated entropy data
            with columns 'Cluster', 'Assembly', and 'Entropy'
        data_type (str): Type of data being visualized (e.g., 'Left Operand')

    Returns:
        None: Displays the plot using matplotlib
    """
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
    """
    Main function that orchestrates the data processing and visualization pipeline.

    The function performs the following steps:
    1. Takes a predefined data type input
    2. Loads entropy and cluster data from CSV files
    3. Filters the data based on the specified type
    4. Merges filtered data with cluster data
    5. Aggregates the data by cluster and assembly
    6. Generates a grouped bar chart visualization
    """
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
