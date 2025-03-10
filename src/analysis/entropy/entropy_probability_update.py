import pandas as pd

# Load the filtered CSV file containing high entropy data
df = pd.read_csv(r"entropy_preprocessed\simple_calculator_filtered_entropy.csv")


# Function to calculate probability of each Assembly value for each Type in each Block
def calculate_assembly_probabilities(df):
    # Group by 'Block_ID', 'Type', and 'Assembly' and count occurrences
    assembly_counts = (
        df.groupby(["Block_ID", "Type", "Assembly"]).size().reset_index(name="Count")
    )

    # Calculate total count of each Type within each Block
    total_counts = (
        assembly_counts.groupby(["Block_ID", "Type"])["Count"]
        .sum()
        .reset_index(name="Total_Count")
    )

    # Merge assembly counts with total counts
    merged_df = pd.merge(assembly_counts, total_counts, on=["Block_ID", "Type"])

    # Calculate probability of each Assembly value for each Type in each Block
    merged_df["Probability"] = merged_df["Count"] / merged_df["Total_Count"]

    return merged_df[["Block_ID", "Type", "Assembly", "Probability"]]


# Calculate Assembly probabilities
assembly_probabilities = calculate_assembly_probabilities(df)

# Print first few rows of the resulting DataFrame
print(assembly_probabilities.head())

# Save the result to a new CSV file
assembly_probabilities.to_csv(
    "probability_update\simple_calculator_probability_update.csv", index=False
)
