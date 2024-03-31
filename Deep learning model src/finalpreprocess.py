import csv

# Function to check if a row has consistent column count
def is_consistent_row(row, num_columns):
    return len(row) == num_columns

# Read the CSV file and remove rows with inconsistent column counts
input_file = 'cicddos2019_dataset.csv'
output_file = 'cicddos2019_dataset_clean.csv'

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Get the header row and determine the number of columns
    header = next(reader)
    num_columns = len(header)
    writer.writerow(header)

    # Iterate over rows, filter out inconsistent rows, and write the consistent rows to the output file
    for row in reader:
        if is_consistent_row(row, num_columns):
            writer.writerow(row)