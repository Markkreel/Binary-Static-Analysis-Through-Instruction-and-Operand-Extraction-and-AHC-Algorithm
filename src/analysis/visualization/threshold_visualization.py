"""
This module provides functionality for visualizing entropy thresholds in binary analysis.
It uses pandas for data manipulation and plotly for creating interactive visualizations
of entropy values across different block IDs and data types (instructions and operands).
"""

import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
df = pd.read_csv(r"entropy\hello_world_entropy.csv")


# Function to calculate threshold as mean + standard deviation
def calculate_threshold(group):
    """
    Calculate the threshold value as the sum of mean and standard deviation of entropy values.

    Args:
        group (pandas.DataFrame): DataFrame containing entropy values in an 'Entropy' column

    Returns:
        float: Calculated threshold value (mean + standard deviation)
    """
    mean_entropy = group["Entropy"].mean()
    std_entropy = group["Entropy"].std()
    threshold = mean_entropy + std_entropy
    return threshold


# Function to visualize the entropy values with threshold line using Plotly
def visualize_entropy(data_frame, block_id, data_type):
    """
    Visualize entropy values with threshold line for specific block ID and data type.

    Args:
        data_frame (pandas.DataFrame): DataFrame containing entropy data
        block_id (int): ID of the block to visualize
        data_type (str): Type of data to visualize ('Instruction', 'Left Operand',
            or 'Right Operand')

    Returns:
        None: Displays a plotly figure with entropy visualization
    """
    # Filter the DataFrame for the specific Block_ID and Type
    filtered_data_frame = data_frame[
        (data_frame["Block_ID"] == block_id) & (data_frame["Type"] == data_type)
    ]

    # Map Assembly values to numeric IDs
    filtered_data_frame.loc[:, "Assembly_ID"] = range(1, len(filtered_data_frame) + 1)

    # Calculate the threshold
    threshold = calculate_threshold(filtered_data_frame)

    # Create the bar chart
    fig = px.bar(
        filtered_data_frame,
        x="Assembly_ID",
        y="Entropy",
        title=(
            f"Entropy Visualization for Block {block_id} and {data_type}: "
            f"Z-Score = 1 (Print 'Hello World')"
        ),
        labels={"Entropy": "Entropy", "Assembly_ID": "Assembly ID"},
    )

    # Add the threshold line
    fig.add_hline(
        y=threshold,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Threshold: {threshold:.2f}",
        annotation_position="top right",
    )

    # Update layout for better readability
    fig.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        yaxis_range=[0, filtered_data_frame["Entropy"].max() * 1.1],
        font=dict(
            family="SF Pro Display, sans-serif",  # Specify the desired font family
            size=12,  # Specify the font size
            color="black",  # Specify the font color
        ),
    )  # Extend y-axis range slightly above max entropy

    # Show the plot
    fig.show()


# Example usage
BLOCK_ID_TO_VISUALIZE = 8
INSTRUCTION_TO_VISUALIZE = "Instruction"
LEFT_OPERAND_TO_VISUALIZE = "Left Operand"
RIGHT_OPERAND_TO_VISUALIZE = "Right Operand"

visualize_entropy(df, BLOCK_ID_TO_VISUALIZE, INSTRUCTION_TO_VISUALIZE)
visualize_entropy(df, BLOCK_ID_TO_VISUALIZE, LEFT_OPERAND_TO_VISUALIZE)
visualize_entropy(df, BLOCK_ID_TO_VISUALIZE, RIGHT_OPERAND_TO_VISUALIZE)
