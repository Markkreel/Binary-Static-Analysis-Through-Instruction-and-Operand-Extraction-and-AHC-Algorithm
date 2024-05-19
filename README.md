# Report

## Entropy Visualization

**Visualizing Entropy for Specific Blocks**

This script allows you to visualize the entropy of instructions, operands (left and right), and their distribution within a chosen block. Entropy is a measure of randomness, indicating the level of disorder in the data. A higher entropy suggests more unpredictable or complex data.

**Here's how to use it:**

1. **Specify Input File:**
   - The script expects an entropy data file in CSV format. The default file name is `"entropy\csv_parser_entropy.csv"`. You can modify this path in the `main` function if needed.
2. **Choose Block to Visualize:**
   - Run the script and enter the desired block ID when prompted. This ID corresponds to a specific block within the entropy data file.

**Data Filtering with Z-Score**

The script calculates a Z-score for each data point (entropy value) to determine its relative deviation from the mean entropy within the chosen block. The Z-score equation is:

`Z = (x - mean) / standard deviation`

This helps identify data points that significantly differ from the average entropy within the block, potentially indicating unusual patterns or outliers.

**Visualization Output**

The script's output (likely a plot or chart) will display the following information:

- Entropy of each instruction, left operand, and right operand for the chosen block.
- Z-score threshold for data filtering (configurable).

This visualization can aid in understanding the entropy distribution within a block and identifying areas with potentially high randomness or unexpected patterns.

Modify `entropy_visualization.py`:

```
def main():
    input_file = "entropy\csv_parser_entropy.csv"
    block_id = input("Enter the Block ID to visualize: ")
```

## Block Characterization
