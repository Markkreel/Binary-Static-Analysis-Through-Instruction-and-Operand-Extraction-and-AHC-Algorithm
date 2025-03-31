"""
This module provides functionality for analyzing and visualizing distinct assembly 
instructions in binary code blocks. It uses pandas for data manipulation and 
plotly for creating interactive visualizations of assembly instruction distributions.
"""

import pandas as pd
import plotly.express as px


df = pd.read_csv(r"entropy\hello_world_entropy.csv")


def calculate_distinct_assemblies(df):
    """
    Calculate the number of unique assembly instructions per block and type.

    Args:
        df (pandas.DataFrame): DataFrame containing assembly data with Block_ID, Type,
            and Assembly columns

    Returns:
        pandas.DataFrame: DataFrame containing counts of distinct assembly instructions
            grouped by Block_ID and Type
    """
    distinct_counts = (
        df.groupby(["Block_ID", "Type"])[  # Group data by Block_ID and Type columns
            "Assembly"
        ]  # Select the Assembly column
        .nunique()  # Count unique assembly instructions in each group
        .reset_index()  # Convert the grouped result back to a DataFrame
    )
    return distinct_counts


def visualize_distinct_assemblies_bar_chart(df):
    """
    Creates a bar chart visualization of distinct assembly types per block and type.

    Args:
        df (pandas.DataFrame): DataFrame containing assembly data with Block_ID, Type,
            and Assembly columns

    Returns:
        None: Displays the interactive bar chart using plotly
    """
    # Calculate distinct assembly instructions per block and type
    distinct_counts = calculate_distinct_assemblies(df)

    # Create a grouped bar chart using plotly express
    fig = px.bar(
        distinct_counts,  # Input DataFrame containing the distinct counts
        x="Block_ID",  # X-axis: Block ID numbers
        y="Assembly",  # Y-axis: Count of unique assembly instructions
        color="Type",  # Color bars based on instruction type
        title="Number of Distinct Assembly Types per Block and Type (Print 'Hello World')",  # Chart title
        labels={
            "Assembly": "Number of Distinct Assembly",
            "Block_ID": "Block #",
        },  # Axis labels
        barmode="group",  # Group bars side by side instead of stacking
    )

    fig.update_layout(
        xaxis_tickangle=-45,  # Rotate x-axis labels by -45 degrees for better readability
        xaxis={"type": "category"},  # Set x-axis type to categorical
        legend=dict(
            orientation="h",  # Set legend orientation to horizontal
            yanchor="bottom",  # Anchor legend to bottom
            y=1.02,  # Position legend slightly above the plot
            xanchor="right",  # Anchor legend to right side
            x=1,  # Position legend at rightmost position
        ),
        font=dict(
            family="SF Pro Display, sans-serif",  # Set font family
            size=12,  # Set font size to 12
            color="black",  # Set font color to black
        ),
    )

    fig.show()  # Display the interactive plot


visualize_distinct_assemblies_bar_chart(
    df
)  # Call the visualization function with the DataFrame
