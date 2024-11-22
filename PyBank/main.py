# Imported modules
import os
import csv

# Initialize variables
Total_Months = 0
Sum = 0
Max = float('-inf')
Min = float('inf')
PNLChange = 0
PNLList = []

# Path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")
    
    previous_row = None
    for row in csvreader:
        # Update total months and total sum
        Total_Months += 1
        current_pnl = int(row[1])
        Sum += current_pnl
        
        # Calculate PNL change if not the first row
        if previous_row is not None:
            PNLChange = current_pnl - int(previous_row[1])
            PNLList.append(PNLChange)
            
            # Track maximum and minimum PNL changes and their dates
            if PNLChange > Max:
                Max = PNLChange
                MaxDate = row[0]
            if PNLChange < Min:
                Min = PNLChange
                MinDate = row[0]
        
        previous_row = row

# Calculate average change
average = sum(PNLList) / len(PNLList) if PNLList else 0

# Print the results
print("Total Months:", Total_Months)
print("Total:", Sum)
print("Average Change:", average)
print("Greatest Increase In Profits:", MaxDate, f"({Max})")
print("Greatest Decrease In Profits:", MinDate, f"({Min})")

# Ensure output folder exists
output_dir = "analysis"
os.makedirs(output_dir, exist_ok=True) 

# Define the output path for the text file
output_path = os.path.join(output_dir, "analysis.txt")

# Output results to a text file
with open(output_path, 'w') as f:
    f.write(f"Total Months: {Total_Months}\n")
    f.write(f"Total: {Sum}\n")
    f.write(f"Average Change: {average}\n")
    f.write(f"Greatest Increase In Profits: {MaxDate} ({Max})\n")
    f.write(f"Greatest Decrease In Profits: {MinDate} ({Min})\n")