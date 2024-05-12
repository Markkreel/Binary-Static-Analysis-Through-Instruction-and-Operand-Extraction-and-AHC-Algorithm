import pandas as pd

# Define input and output file paths (modify as needed)
input_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\updated_formatted_data.csv"
output_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\updated_formatted_data.csv"

# Read the CSV data
df = pd.read_csv(input_file)

# Initialize a counter and dictionary for assigning numerical IDs
block_id = 1
block_id_map = {}

# Iterate through rows (excluding the header)
for index, row in df.iterrows():
  if index == 0:
    continue  # Skip the header row

  # Get the Block_ID and check if it's already seen
  current_block_id = row["Block_ID"]
  if current_block_id not in block_id_map:
    block_id_map[current_block_id] = block_id
    block_id += 1  # Increment counter for new unique IDs

  # Update the Block_ID with the numerical ID
  row["Block_ID"] = block_id_map[current_block_id]

# Update the DataFrame with the modified values
df.update(df)

# Save the updated data to a new CSV file
df.to_csv(output_file, index=False)

print("CSV file updated with numerical Block IDs!")
