import pandas as pd
import numpy as np
from scipy.stats import entropy

def calculate_entropy(probabilities):
    """Calculates Shannon Entropy given a dictionary of probabilities."""
    return entropy(list(probabilities.values()), base=2)

def calculate_entropies_for_blocks(df):
    """Calculates Shannon Entropy for distinct data points within each block."""
    entropies = {}
    columns = ['Instruction', 'Left Operand', 'Right Operand']
    for block_id, block_data in df.groupby('Block_ID'):
        block_entropies = {}
        total_data = len(block_data)
        for column in columns:
            unique_values, counts = np.unique(block_data[column].dropna(), return_counts=True)
            probabilities = {value: count / total_data for value,
                             count in zip(unique_values, counts)}
            entropy_value = calculate_entropy(probabilities)
            block_entropies[column] = {'probabilities': probabilities, 'entropy': entropy_value}
        entropies[block_id] = block_entropies
    return entropies

def save_entropies_to_csv(entropies, output_file):
    """Saves the calculated entropies to a CSV file."""
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Block ID,Column,Value,Probability,Entropy\n")
        for block_id, block_entropies in entropies.items():
            for column, data in block_entropies.items():
                for value, probability in data['probabilities'].items():
                    entropy_value = data['entropy']
                    file.write(f"{block_id},{column},{value},{probability:.2f},{entropy_value:.2f}\n")

def main():
    # Load the CSV file into a DataFrame
    INPUT_FILE = r"C:\External\Projects\8th Semester\Thesis\compiled\hello_world_disassembled\hello_world_disassembly.csv"
    df = pd.read_csv(INPUT_FILE)

    # Calculate Shannon Entropy for distinct data points within each block
    block_entropies = calculate_entropies_for_blocks(df)

    # Save the calculated entropies to a CSV file
    output_file = "hello_world_block_entropies.csv"
    save_entropies_to_csv(block_entropies, output_file)
    print(f"Entropies saved to '{output_file}'.")

if __name__ == "__main__":
    main()
