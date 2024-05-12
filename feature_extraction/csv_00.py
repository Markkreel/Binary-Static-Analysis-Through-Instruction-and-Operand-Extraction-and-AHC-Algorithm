import pandas as pd

# Define input and output file paths (modify as needed)
input_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\updated_formatted_data.csv"
output_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\updated_formatted_data.csv"

# Read the CSV data
df = pd.read_csv(input_file)

# Modify the second column (Address)
df["Address"] = "000000000000" + df["Address"]

# Save the updated data to a new CSV file
df.to_csv(output_file, index=False)

print("CSV file updated successfully!")
