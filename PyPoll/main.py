import os
import csv
from datetime import datetime  # Import the datetime module

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}

# Read the dataset from the CSV file
with open(election_csv) as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate name from the current row
        candidate_name = row['Candidate']
        
        # If candidate is not in the dictionary, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        
        # Increment the vote count for the candidate
        candidates[candidate_name] += 1

# Determine the winner based on the popular vote
winner = max(candidates, key=candidates.get)

# Print and save the results
output = []
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")
output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Print the output to the terminal
for line in output:
    print(line)

# Export the results to a text file
output_txt = os.path.join('Analysis', 'election_results.txt')
with open(output_txt, 'w') as file:
    for line in output:
        file.write(line + "\n")

print(f"Results have been exported to {output_txt}")
