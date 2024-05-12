import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
INPUT_FILE = "hello_world_block_entropies.csv"
df = pd.read_csv(INPUT_FILE)

# Create a grouped bar plot for each column and block ID
columns = df['Column'].unique()
for column in columns:
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df[df['Column'] == column], x='Value',
                y='Probability', hue='Block ID', legend='brief')
    plt.title(f"Probability of {column} by Block ID")
    plt.xlabel(column)
    plt.ylabel("Probability")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend(ncol=2)  # Adjust the number of legend items shown
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df[df['Column'] == column], x='Value',
                y='Entropy', hue='Block ID', legend='brief')
    plt.title(f"Entropy of {column} by Block ID")
    plt.xlabel(column)
    plt.ylabel("Entropy")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend(ncol=2)  # Adjust the number of legend items shown
    plt.show()
