import pandas as pd
from math import log2
import numpy as np


def calculate_distribution(block):
    total_probability = block["Probability"].sum()
    distribution = block.groupby("Assembly")["Probability"].sum() / total_probability
    return distribution


def kl_divergence(p, q):
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
