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
    # Group by "Cluster" and count the number of distinct "Assembly"
    aggregated_data = merged_data.groupby("Cluster")["Assembly"].nunique().reset_index()
    aggregated_data.rename(columns={"Assembly": "Distinct_Assemblies"}, inplace=True)
    return aggregated_data


def plot_bar_chart(aggregated_data, data_type):
    # Create a bar chart
    plt.figure(figsize=(12, 8))
    plt.bar(aggregated_data["Cluster"], aggregated_data["Distinct_Assemblies"])

    plt.xlabel("Cluster ID")
    plt.ylabel("Number of Distinct Assemblies")
    plt.title(f"Number of Distinct Assemblies by Cluster for {data_type} Data Points")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def main():
    # Step 1: User Input
    data_type = "Instruction"
    # Step 2: Data Loading
    entropy_data, cluster_data = load_data()

    # Step 3: Data Filtering
    filtered_data = filter_data(entropy_data, data_type)

    # Step 4: Data Merging
    merged_data = merge_data(filtered_data, cluster_data)

    # Step 5: Data Aggregation
    aggregated_data = aggregate_data(merged_data)

    # Step 6: Bar Graph Generation
    plot_bar_chart(aggregated_data, data_type)


if __name__ == "__main__":
    main()
