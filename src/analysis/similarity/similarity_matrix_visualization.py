"""
This module provides functionality for visualizing similarity matrices between binary code blocks.
It reads similarity data from CSV files and generates heatmap visualizations using matplotlib and seaborn.
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Function to read similarity matrix from CSV file and generate block IDs
def read_similarity_matrix(input_file):
    """
    Reads a similarity matrix from a CSV file and generates corresponding block IDs.

    Args:
        input_file (str): Path to the CSV file containing similarity data.

    Returns:
        tuple: A tuple containing:
            - numpy.ndarray: A square similarity matrix where each element represents
              the similarity between two blocks
            - list: Sorted list of unique block IDs
    """
    # Initialize empty set for unique block IDs and list for similarity entries
    unique_block_ids = set()
    similarities = []

    # Open and read the CSV file containing similarity data
    with open(input_file, newline="", encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            # Extract block IDs and similarity value from each row
            block_id1, block_id2, similarity = row
            # Add block IDs to set (duplicates automatically handled)
            unique_block_ids.add(block_id1)
            unique_block_ids.add(block_id2)
            # Store similarity data as tuple with converted float value
            similarities.append((block_id1, block_id2, float(similarity)))

    block_ids = sorted(block_ids)  # Sort block IDs
    size = len(block_ids)  # Get dimension for square matrix
    # Initialize empty square matrix with zeros
    matrix = np.zeros((size, size))

    # Populate similarity matrix with values
    for block_id1, block_id2, similarity in similarities:
        # Get indices for both blocks in the matrix
        i = block_ids.index(block_id1)
        j = block_ids.index(block_id2)
        # Set similarity values symmetrically (matrix[i,j] = matrix[j,i])
        similarity_matrix[i, j] = similarity
        similarity_matrix[j, i] = similarity  # symmetric matrix

    return similarity_matrix, block_ids


# Read the similarity matrix and block IDs from the CSV file
INPUT_FILE = "probability_update/simple_calculator_probability_update.csv"
similarity_matrix, block_ids = read_similarity_matrix(INPUT_FILE)

# Create a new figure with specified dimensions (10x8 inches)
plt.figure(figsize=(10, 8))

# Generate heatmap visualization using seaborn
sns.heatmap(
    similarity_matrix,  # Input data matrix
    xticklabels=block_ids,  # Labels for x-axis ticks
    yticklabels=block_ids,  # Labels for y-axis ticks
    cmap="viridis",  # Color scheme for heatmap
    annot=True,  # Show numerical values in cells
    fmt=".2f",  # Format numbers to 2 decimal places
)

# Set the title and axis labels for the plot
plt.title("Block Similarity Matrix Heatmap")
plt.xlabel("Block ID")
plt.ylabel("Block ID")

# Rotate x-axis labels 90 degrees for better readability
plt.xticks(rotation=90)
# Keep y-axis labels horizontal
plt.yticks(rotation=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()
