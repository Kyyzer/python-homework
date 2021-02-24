"""
Pybank homework

Your task is to create a Python script that analyzes the records to calculate each of the following:

    The total number of months included in the dataset.

    The net total amount of Profit/Losses over the entire period.

    The average of the changes in Profit/Losses over the entire period.

    The greatest increase in profits (date and amount) over the entire period.

    The greatest decrease in profits (date and amount) over the entire period.
    
"""

# Import pathlib and CSV library. Set the path for budget_data.csv

from pathlib import Path
import csv
csvpath = Path("Resources/budget_data.csv")

# Initialise a records list

records = []

# Open the csv file as csvfile
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Calculate the total number of months included in dataset
    for row in csvreader:
        total_months += 1