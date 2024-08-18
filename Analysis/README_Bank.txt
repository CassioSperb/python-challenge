# Bank Analysis

## Overview

This Python script analyzes a CSV file containing financial data to calculate the following metrics:
- Total number of months in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Average change in "Profit/Losses"
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)

## Script Details

### File Path

- Update the `budget_csv` variable with the path to your CSV file.

### CSV File Format

The CSV file should have the following columns:
- `Date`: The date of the financial record (format: `Month-Year`)
- `Profit/Losses`: The profit or loss amount for the given month

### Example CSV Format

```csv
Date,Profit/Losses
Jan-10,867884
Feb-10,984655
Mar-10,322013

### Results

Financial Analysis
---------------------------
Total Months: 86
Net Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)