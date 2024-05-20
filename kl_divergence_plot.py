import pandas as pd
from math import log2
import numpy as np


# Function to calculate probability distribution for a block
def calculate_distribution(block):
    total_probability = block["Probability"].sum()
    distribution = block.groupby("Assembly")["Probability"].sum() / total_probability
    return distribution


# Function to calculate KL Divergence between two distributions
def kl_divergence(p, q):
    # Ensure the distributions have the same index
    p, q = p.align(q, fill_value=0)

    # Check for empty or invalid distributions
    if p.sum() == 0 or q.sum() == 0:
        return np.nan  # Return NaN if one of the distributions is empty or invalid

    # Calculate the KL divergence
    kl_div = (p * np.log2(p / q)).sum()

    # Handle cases where probabilities are close to zero to avoid math domain errors
    if np.isnan(kl_div) or np.isinf(kl_div):
        return np.nan  # Return NaN if KL divergence is NaN or infinite

    return kl_div


# Load the CSV files for each type
instruction_df = pd.read_csv("Instruction.csv")
left_operand_df = pd.read_csv("Left Operand.csv")
right_operand_df = pd.read_csv("Right Operand.csv")

# Group data by Block_ID for each type
instruction_blocks = instruction_df.groupby("Block_ID")
left_operand_blocks = left_operand_df.groupby("Block_ID")
right_operand_blocks = right_operand_df.groupby("Block_ID")

# Calculate KL Divergence between blocks for each type
kl_divergences = {}
for type_name, blocks in [
    ("Instruction", instruction_blocks),
    ("Left Operand", left_operand_blocks),
    ("Right Operand", right_operand_blocks),
]:
    for block_id, group in blocks:
        distribution_p = calculate_distribution(group)
        for other_block_id, other_group in blocks:
            if block_id != other_block_id:
                distribution_q = calculate_distribution(other_group)
                kl_divergences[(type_name, block_id, other_block_id)] = kl_divergence(
                    distribution_p, distribution_q
                )

# You now have a dictionary kl_divergences where keys are tuples (Type, Block_ID, Other_Block_ID)
# and values are the KL Divergence between the probability distributions of the corresponding blocks.
