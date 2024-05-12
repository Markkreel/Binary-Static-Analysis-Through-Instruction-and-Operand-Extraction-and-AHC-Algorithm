import pandas as pd

# Read the CSV file
input_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\formatted_data.csv"
output_file = r"C:\External\Projects\8th Semester\Thesis\feature_extraction\output\updated_formatted_data.csv"

def split_left_operand(text):
  """
  Splits the left operand while handling commas inside brackets.

  Args:
      text (str): The text to be split.

  Returns:
      tuple: A tuple containing the left operand and right operand (if present).
  """
  open_count = 0
  split_index = None
  for i, char in enumerate(text):
    if char == '(':
      open_count += 1
    elif char == ')':
      open_count -= 1
    elif char == ',' and open_count == 0:
      split_index = i
      break
  if split_index is None:
    return text, ""  # No comma, return entire text as left operand
  else:
    return text[:split_index], text[split_index+1:]

# Read the CSV data
df = pd.read_csv(input_file)

# Apply the split function to the Left Operand column
split_results = df["Left Operand"].apply(split_left_operand)

# Fill missing values with empty strings (for Right Operand in rows without commas)
df[["Left Operand", "Right Operand"]] = split_results.fillna("")

# Clear the Instruction column (if needed)
if any(df["Instruction"]):  # Check if Instruction column has any values
  df["Instruction"] = ""

# Save the updated data to a new CSV file
df.to_csv(output_file, index=False)

print("CSV file updated successfully!")
