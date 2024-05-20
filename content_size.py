import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
df = pd.read_csv(r"entropy\hello_world_entropy.csv")


# Function to calculate the number of distinct 'Assembly' for each 'Block_ID' and 'Type'
def calculate_distinct_assemblies(df):
    # Group by 'Block_ID' and 'Type', then count the distinct 'Assembly'
    distinct_counts = (
        df.groupby(["Block_ID", "Type"])["Assembly"].nunique().reset_index()
    )
    return distinct_counts


# Function to visualize the number of distinct 'Assembly' values as a grouped bar chart
def visualize_distinct_assemblies_bar_chart(df):
    distinct_counts = calculate_distinct_assemblies(df)

    # Create the grouped bar chart
    fig = px.bar(
        distinct_counts,
        x="Block_ID",
        y="Assembly",
        color="Type",
        title="Number of Distinct Assembly Types per Block and Type (Print 'Hello World')",
        labels={"Assembly": "Number of Distinct Assembly", "Block_ID": "Block #"},
        barmode="group",
    )

    # Update layout for better readability
    fig.update_layout(
        xaxis_tickangle=-45,
        xaxis={"type": "category"},
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        font=dict(
            family="SF Pro Display, sans-serif",  # Specify the desired font family
            size=12,  # Specify the font size
            color="black",  # Specify the font color
        ),
    )

    # Show the plot
    fig.show()


# Example usage
visualize_distinct_assemblies_bar_chart(df)
