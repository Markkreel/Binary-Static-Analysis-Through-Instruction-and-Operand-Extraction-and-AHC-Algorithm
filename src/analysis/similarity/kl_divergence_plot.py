"""
This module calculates and analyzes Kullback-Leibler divergence between probability
distributions of assembly instructions and operands from different code blocks.
It processes instruction and operand data from CSV files to measure the similarity
between code blocks based on their instruction and operand usage patterns.
"""

import pandas as pd
import numpy as np


def calculate_distribution(block):
    """
    Calculate the probability distribution of assembly instructions in a block.

    Args:
        block (pandas.DataFrame): DataFrame containing assembly instructions and their probabilities

    Returns:
        pandas.Series: Normalized probability distribution of assembly instructions
    """
    total_probability = block["Probability"].sum()
    distribution = block.groupby("Assembly")["Probability"].sum() / total_probability
    return distribution


def kl_divergence(p, q):
    """
    Calculate the Kullback-Leibler divergence between two probability distributions.

    Args:
        p (pandas.Series): First probability distribution
        q (pandas.Series): Second probability distribution

    Returns:
        float: KL divergence value, or np.nan if distributions are invalid
    """
    p, q = p.align(q, fill_value=0)

    # Check for empty or invalid distributions
    if p.sum() == 0 or q.sum() == 0:
        return np.nan

    kl_div = (p * np.log2(p / q)).sum()

    if np.isnan(kl_div) or np.isinf(kl_div):
        return np.nan

    return kl_div


instruction_df = pd.read_csv("Instruction.csv")
left_operand_df = pd.read_csv("Left Operand.csv")
right_operand_df = pd.read_csv("Right Operand.csv")

instruction_blocks = instruction_df.groupby("Block_ID")
left_operand_blocks = left_operand_df.groupby("Block_ID")
right_operand_blocks = right_operand_df.groupby("Block_ID")

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
