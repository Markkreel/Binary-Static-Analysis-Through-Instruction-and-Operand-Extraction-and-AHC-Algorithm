import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
INPUT_FILE = "/compiled/dynamic_array_allocator_disassembled/dynamic_array_allocator_diassembly.csv"
df = pd.read_csv(INPUT_FILE)

# Create a grouped bar plot for each column and block ID
columns = df['Column'].unique()
for column in columns:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df[df['Column'] == column], x='Value',
                y='Probability', hue='Block ID', legend='full')
    plt.title(f"Probability of {column} by Block ID")
    plt.xlabel(column)
    plt.ylabel("Probability")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df[df['Column'] == column], x='Value',
                y='Entropy', hue='Block ID', legend='full')
    plt.title(f"Entropy of {column} by Block ID")
    plt.xlabel(column)
    plt.ylabel("Entropy")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
