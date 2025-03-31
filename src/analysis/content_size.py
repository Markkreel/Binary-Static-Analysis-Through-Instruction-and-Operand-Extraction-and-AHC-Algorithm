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
        df.groupby(["Block_ID", "Type"])["Assembly"].nunique().reset_index()
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
    distinct_counts = calculate_distinct_assemblies(df)
    fig = px.bar(
        distinct_counts,
        x="Block_ID",
        y="Assembly",
        color="Type",
        title="Number of Distinct Assembly Types per Block and Type (Print 'Hello World')",
        labels={"Assembly": "Number of Distinct Assembly", "Block_ID": "Block #"},
        barmode="group",
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(
            family="SF Pro Display, sans-serif",
            size=12,
            color="black",
        ),
    )

    fig.show()


visualize_distinct_assemblies_bar_chart(df)
