import csv

# Function to check if a value can be converted to an int or float
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function to convert a value to int, float, or leave it as a string
def convert_to_numeric(value):
    if is_numeric(value):
        if '.' in value:
            return float(value)
        else:
            return int(value)
    else:
        return value

# Function to check if a row has null values
def has_null_values(row):
    return any(value.strip() == '' for value in row)

# Function to check if a row has consistent column count and all numerical values can be converted
def is_consistent_row(row):
    return len(row) == num_columns and not has_null_values(row) and all(is_numeric(value) for value in row)

# Read the CSV file and check for inconsistent rows
input_file = 'cicddos2019_dataset.csv'
output_file = 'cicddos2019_dataset_clean.csv'

try:
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Get the header row and determine the number of columns
        header = next(reader)
        num_columns = len(header)
        writer.writerow(header)

        # Iterate over rows, filter out inconsistent rows, convert numeric values, and write the consistent rows to the output file
        for row in reader:
            if is_consistent_row(row):
                # Convert numerical values to int or float
                row = [convert_to_numeric(value) for value in row]
                print("Processed Row:", row)  # Debug print to check the processed row
                writer.writerow(row)
except Exception as e:
    print("An error occurred:", e)
