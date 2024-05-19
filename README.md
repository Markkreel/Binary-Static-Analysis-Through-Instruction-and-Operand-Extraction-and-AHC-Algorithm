# Report

## Entropy Visualization

### Visualizing Entropy for Specific Blocks

This script allows you to visualize the entropy of instructions, operands (left and right), and their distribution within a chosen block. Entropy is a measure of randomness, indicating the level of disorder in the data. A higher entropy suggests more unpredictable or complex data.

1. **Specify Input File:**
   - The script expects an entropy data file in CSV format. The default file name is `"entropy\csv_parser_entropy.csv"`. You can modify this path in the `main` function if needed.
2. **Choose Block to Visualize:**
   - Run the script and enter the desired block ID when prompted. This ID corresponds to a specific block within the entropy data file.

### Data Filtering with Z-Score

The script calculates a Z-score for each data point (entropy value) to determine its relative deviation from the mean entropy within the chosen block. The Z-score equation is:

`Z = (x - mean) / standard deviation`

This helps identify data points that significantly differ from the average entropy within the block, potentially indicating unusual patterns or outliers.

### Visualization Output

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

## Block Characterization using Distribution Similarity and Hierarchical Clustering

This section details the process of characterizing blocks based on their functional similarity using two Python scripts:

1. **Distribution Similarity Calculation:**
   * **`kl_divergence.py`** or  **`kl_divergence_normalized.py`** : These scripts calculate the Kullback-Leibler (KL) divergence between the probability distributions of different blocks. KL divergence measures the difference between two probability distributions, providing a quantitative way to assess how similar they are.
     * Choose `kl_divergence.py` for raw block distributions.
     * Use `kl_divergence_normalized.py` for normalized and potentially smoothed distributions (better for distributions with low counts).
2. **Hierarchical Clustering and Visualization:**
   * **`agglomerative_hierarchical_clustering.py`** : This script employs Agglomerative Hierarchical Clustering (AHC) to group blocks based on their KL divergence similarities. AHC starts with each block as its own cluster and iteratively merges the most similar clusters until a desired hierarchy is formed. The resulting clusters represent groups of blocks with potentially similar functionalities.

### Benefits

* By analyzing block distribution similarity, you can gain insights into how blocks might be functionally related.
* The AHC algorithm helps visualize these relationships by grouping similar blocks together.

### **Understanding the Output**

* The scripts will likely generate a cluster dendrogram, a tree-like structure that depicts the hierarchical clustering process. Blocks with lower KL divergences (more similar distributions) will be merged earlier in the dendrogram, indicating their closer functional relationship.
* You can use the dendrogram to determine the appropriate number of clusters (groups of similar blocks) based on your analysis goals.

### **Additional Notes**

* Ensure the input data to these scripts is suitable for KL divergence calculations. Consider data normalization or smoothing if necessary (especially for distributions with low counts).
* The choice between `kl_divergence.py` and `kl_divergence_normalized.py` depends on your data characteristics.
* Modify the following code to the desired entropy CSV file and modify the number of existing blocks in the CSV file:
  ```
  def main():
      INPUT_FILE = "similarity\csv_parser_block_similarity\csv_parser_block_similarity_normalized.csv"
      OUTPUT_FILE = "clusters.csv"
      block_ids = [str(i) for i in range(1, 153)]  # Example with 100 blocks
  ```
## Visualizing Block Similarities with Heatmaps
This section explains how to visualize the similarity between blocks using `similarity_matrix_visualization.py`.
### Process
* The script takes the pre-calculated similarity values generated by the KL divergence scripts (`kl_divergence.py` or `kl_divergence_normalized.py`). These values represent the distance (dissimilarity) between the probability distributions of different blocks, where a lower value indicates greater similarity.
* The script then constructs a heatmap to visually represent the similarity matrix. Heatmaps use color gradients to represent data values:
   * Darker colors (closer to black) typically correspond to higher similarities (lower KL divergence values) between blocks.
   * Lighter colors (closer to white) usually indicate lower similarities (higher KL divergence values).
* The range of displayed similarity values typically falls between 0 (most similar) and positive infinity (completely dissimilar).
## Benefits
Heatmaps provide a convenient way to quickly identify blocks with high similarity scores, potentially suggesting similar functionalities. Futhermore, visualizing the entire matrix allows for a more comprehensive understanding of the relationships between all blocks.
