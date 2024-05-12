import pandas as pd
import numpy as np
from scipy.stats import entropy
import re

def calculate_entropy(probabilities):
    """Calculates Shannon Entropy given a dictionary of probabilities."""
    return entropy(list(probabilities.values()), base=2)

def extract_values_from_brackets(value):
    """Extracts values within brackets and returns them as a single string."""
    if pd.isna(value):
        return ""
    bracket_values = re.findall(r'\((.*?)\)', value)
    return ','.join(bracket_values)


def calculate_entropies_for_blocks(df):
    """Calculates Shannon Entropy for distinct data points within each block."""
    entropies = {}
    columns = ['Instruction', 'Left Operand', 'Right Operand']
    for block_id, block_data in df.groupby('Block_ID'):
        block_entropies = {}
        total_data = len(block_data)
        for column in columns:
            if column == 'Right Operand':
                # Extract values from brackets for Right Operand column
                block_data[column] = block_data[column].apply(extract_values_from_brackets)
            unique_values, counts = np.unique(block_data[column].dropna(), return_counts=True)
            probabilities = {value: count / total_data for value, count in zip(unique_values, counts)}
            entropy_value = calculate_entropy(probabilities)
            block_entropies[column] = {'probabilities': probabilities, 'entropy': entropy_value}
        entropies[block_id] = block_entropies
    return entropies

def save_entropies_to_csv(entropies, OUTPUT_FILE):
    """Saves the calculated entropies to a CSV file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write("Block ID,Column,Value,Probability,Entropy\n")
        for block_id, block_entropies in entropies.items():
            for column, data in block_entropies.items():
                for value, probability in data['probabilities'].items():
                    entropy_value = data['entropy']
                    file.write(f"{block_id},{column},{value},{probability:.2f},{entropy_value:.2f}\n")

def main():
    """The main function is where I input the INPUT_FILE and where the print process is."""
    # Load the CSV file into a DataFrame
    INPUT_FILE = r"compiled\csv_parser_disassembled\csv_parser_disassembly.csv"
    df = pd.read_csv(INPUT_FILE)

    # Calculate Shannon Entropy for distinct data points within each block
    block_entropies = calculate_entropies_for_blocks(df)

    # Save the calculated entropies to a CSV file
    OUTPUT_FILE = "hello_world_block_entropies.csv"
    save_entropies_to_csv(block_entropies, OUTPUT_FILE)
    print(f"Entropies saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
