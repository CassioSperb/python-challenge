import os
import csv
from datetime import datetime  # Import the datetime module

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Path to export the results
output_txt = os.path.join('Analysis', 'analysis_output.txt')
  
# Function to extract the year and month from a date
def extract_year_month(date_str):
     # Adjust '%b-%y' to match the date format 'Jan-10'
    date = datetime.strptime(date_str, '%b-%y')
    return date.year, date.month

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
    csv_reader = csv.DictReader(file)  # Access columns by name
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
            dates.append(row['Date'])  # Store the date corresponding to the change
            
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

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Export results to a text file
with open(output_txt, 'w') as file:
    file.write("Financial Analysis")
    file.write("---------------------------")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print(f"Results have been exported to {output_txt}")