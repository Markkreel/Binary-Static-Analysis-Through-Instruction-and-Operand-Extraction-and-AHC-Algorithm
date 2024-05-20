import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load the CSV file into a DataFrame
df = pd.read_csv(r"entropy\hello_world_entropy.csv")


# Function to calculate threshold as mean + standard deviation
def calculate_threshold(group):
    mean_entropy = group["Entropy"].mean()
    std_entropy = group["Entropy"].std()
    threshold = mean_entropy + std_entropy
    return threshold


# Function to visualize the entropy values with threshold line using Plotly
def visualize_entropy(df, block_id, data_type):
    # Filter the DataFrame for the specific Block_ID and Type
    filtered_df = df[(df["Block_ID"] == block_id) & (df["Type"] == data_type)]

    # Map Assembly values to numeric IDs
    filtered_df.loc[:, "Assembly_ID"] = range(1, len(filtered_df) + 1)

    # Calculate the threshold
    threshold = calculate_threshold(filtered_df)

    # Create the bar chart
    fig = px.bar(
        filtered_df,
        x="Assembly_ID",
        y="Entropy",
        title=f"Entropy Visualization for Block {block_id} and {data_type} : Z-Score = 1 (Print 'Hello World')",
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
        yaxis_range=[0, filtered_df["Entropy"].max() * 1.1],
        font=dict(
            family="SF Pro Display, sans-serif",  # Specify the desired font family
            size=12,  # Specify the font size
            color="black",  # Specify the font color
        ),
    )  # Extend y-axis range slightly above max entropy

    # Show the plot
    fig.show()


# Example usage
block_id_to_visualize = 8
instruction_to_visualize = "Instruction"
leftOperand_to_visualize = "Left Operand"
rightOperand_to_visualize = "Right Operand"

visualize_entropy(df, block_id_to_visualize, instruction_to_visualize)
visualize_entropy(df, block_id_to_visualize, leftOperand_to_visualize)
visualize_entropy(df, block_id_to_visualize, rightOperand_to_visualize)
