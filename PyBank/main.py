import os
import csv
from datetime import datetime  # Import the datetime module

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Path to export the results
output_txt = os.path.join('Analysis', 'analysis_output.txt')

# Function to extract the year and month from a date string manually
def extract_year_month(date_str):
    month_str, year_str = date_str.split('-')
    
    # Dictionary to convert month abbreviations to numbers
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 
        'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 
        'Nov': 11, 'Dec': 12
    }
    
    # Convert the year string and month string
    month = months[month_str]
    year = 2000 + int(year_str) if int(year_str) < 50 else 1900 + int(year_str)  # Adjust for year range

    return year, month

# Initialize variables
unique_months = set()
net_total = 0  # Variable to store the net total of "Profit/Losses"
previous_profit_loss = None
changes = []
dates = []  # Store dates corresponding to changes
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Read the dataset from a CSV file
with open(budget_csv) as file:
    csv_reader = csv.DictReader(file)  
    for row in csv_reader:

        # Calculate unique months
        year, month = extract_year_month(row['Date'])
        unique_months.add((year, month))
        
        # Sum the Profit/Losses values
        current_profit_loss = int(row['Profit/Losses'])
        net_total += current_profit_loss
    
        # Calculate changes
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(row['Date']) 
            
            # Update greatest increase
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = row['Date']
            
            # Update greatest decrease
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = row['Date']

        previous_profit_loss = current_profit_loss

# Calculate the total number of unique months
total_months = len(unique_months)

# Calculate the average of changes
if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Print and save the results
output = []
output.append(f"Financial Analysis")
output.append(f"---------------------")
output.append(f"Total Months: {total_months}\n")
output.append(f"Net Total: ${net_total}\n")
output.append(f"Average Change: ${average_change:.2f}\n")
output.append(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
output.append(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# Print the output to the terminal
for line in output:
    print(line)

# Export the results to a text file
output_txt = os.path.join('Analysis', 'Financial_Analysis.txt')
with open(output_txt, 'w') as file:
    for line in output:
        file.write(line + "\n")

print(f"Results have been exported to {output_txt}")
