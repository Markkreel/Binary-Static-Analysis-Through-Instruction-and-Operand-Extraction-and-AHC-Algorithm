# Binary Static Analysis Through Instruction and Operand Extraction and Agglomerative Hierarchical Clustering (AHC)

A computational forensic instrumentation framework employing Algorithmic Hierarchical Clustering (AHC) for comprehensive binary code block visualization and structural decomposition. The methodology integrates entropy-based probabilistic analysis and sophisticated similarity measurement protocols to facilitate introspective examination of disassembled binary architectural semantics.

## Entropy Visualization

### Visualizing Entropy for Specific Blocks

This script facilitates the visualization of entropy associated with instructions and operands (both left and right) within a specified block. Entropy, as a quantitative metric of randomness, serves as an indicator of the degree of disorder or unpredictability inherent in the data. Elevated entropy values typically correspond to data exhibiting greater complexity or stochasticity.

1. **Specify Input File:**
   - The script expects an entropy data file in CSV format. The default file name is `"entropy\csv_parser_entropy.csv"`. You can modify this path in the `main` function if needed.
2. **Choose Block to Visualize:**
   - Run the script and enter the desired block ID when prompted. This ID corresponds to a specific block within the entropy data file.

### Data Filtering with Z-Score

The script calculates a Z-score for each data point (entropy value) to determine its relative deviation from the mean entropy within the chosen block. The Z-score equation is:

```mathematica
Z = (x - mean) / standard deviation
```

This helps identify data points that significantly differ from the average entropy within the block, potentially indicating unusual patterns or outliers.

### Visualization Output

The script's output (likely a plot or chart) will display the following information:

- Entropy of each instruction, left operand, and right operand for the chosen block.
- Z-score threshold for data filtering (configurable).

This visualization can aid in understanding the entropy distribution within a block and identifying areas with potentially high randomness or unexpected patterns.

Modify `entropy_visualization.py`:

```python
def main():
    input_file = "entropy\csv_parser_entropy.csv"
    block_id = input("Enter the Block ID to visualize: ")
```

## Block Characterization using Distribution Similarity and Hierarchical Clustering

This section details the process of characterizing blocks based on their functional similarity using two Python scripts:

1. **Distribution Similarity Calculation:**
   - **`kl_divergence.py`** or **`kl_divergence_normalized.py`** : These scripts calculate the Kullback-Leibler (KL) divergence between the probability distributions of different blocks. KL divergence measures the difference between two probability distributions, providing a quantitative way to assess how similar they are.
     - Choose `kl_divergence.py` for raw block distributions.
     - Use `kl_divergence_normalized.py` for normalized and potentially smoothed distributions (better for distributions with low counts).
2. **Hierarchical Clustering and Visualization:**
   - **`agglomerative_hierarchical_clustering.py`** : This script employs Agglomerative Hierarchical Clustering (AHC) to group blocks based on their KL divergence similarities. AHC starts with each block as its own cluster and iteratively merges the most similar clusters until a desired hierarchy is formed. The resulting clusters represent groups of blocks with potentially similar functionalities.

### Advantages

Analyzing the similarity in block distributions provides insights into potential functional relationships among blocks. The Agglomerative Hierarchical Clustering (AHC) algorithm aids in visualizing these relationships by clustering similar blocks together.

### **Understanding the Output**

The scripts are anticipated to produce a cluster dendrogram, which is a tree-like diagram illustrating the hierarchical clustering process. Within this structure, blocks exhibiting lower KL divergences, indicative of more similar probability distributions, will be merged at earlier stages of the dendrogram, signifying a closer functional relationship. This dendrogram can be utilized to ascertain the optimal number of clusters, or groups of similar blocks, tailored to the specific objectives of the analysis.

### **Additional Notes**

- Ensure the input data to these scripts is suitable for KL divergence calculations. Consider data normalization or smoothing if necessary (especially for distributions with low counts).
- The choice between `kl_divergence.py` and `kl_divergence_normalized.py` depends on your data characteristics.
- Modify the following code to the desired entropy CSV file and modify the number of existing blocks in the CSV file:

  ```python
  def main():
      INPUT_FILE = "similarity\csv_parser_block_similarity\csv_parser_block_similarity_normalized.csv"
      OUTPUT_FILE = "clusters.csv"
      block_ids = [str(i) for i in range(1, 153)]  # Example with 100 blocks
  ```

## Visualizing Block Similarities with Heatmaps

The Python script utilizes pre-computed similarity metrics derived from the Kullback-Leibler (KL) divergence algorithms, as implemented in the scripts `kl_divergence.py` or `kl_divergence_normalized.py`. These metrics quantify the dissimilarity between the probability distributions of distinct blocks, with lower values denoting higher degrees of similarity. Subsequently, the script generates a heatmap to provide a visual representation of the similarity matrix.

In this visualization, color gradients are employed to depict the data values: darker shades, approaching black, are indicative of higher similarity (lower KL divergence values), whereas lighter shades, nearing white, signify lower similarity (higher KL divergence values). The spectrum of similarity values typically spans from 0, representing maximum similarity, to positive infinity, denoting complete dissimilarity.

### Benefits

Heatmaps facilitate the rapid identification of blocks with high similarity scores, suggesting potential functional similarities. Visualizing the entire matrix enhances the comprehensive understanding of inter-block relationships.

**Last Updated:** 29-03-2025 ⸺ **Last Reviewed:** 29-03-2025
