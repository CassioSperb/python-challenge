import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources','budget_data.csv')
# Function to extract the year and month from a date
def extract_year_month(date_str):
    # Replace '%Y-%m-%d' with the actual date format in your dataset
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.year, date.month

# Initialize a set to store unique (year, month) pairs
unique_months = set()

# Read the dataset from a CSV file
# Replace 'budget_data.csv' with the actual file path
with open(budget_csv) as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header if it exists
    
    # Replace 'Date' with the index of the date column if necessary
    date_column_index = header.index('Date')
    
    for row in csv_reader:
        year, month = extract_year_month(row[date_column_index])
        unique_months.add((year, month))

# Calculate the total number of unique months
total_months = len(unique_months)

print(f"The total number of months included in the dataset is: {total_months}")