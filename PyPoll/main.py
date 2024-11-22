# imported modules
import os
import csv


# path
Total_Votes = 0
Charles_Count = 0
Diana_Count = 0
Raymon_Count = 0

csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        if row[2] == "Charles Casper Stockham":
            Charles_Count = Charles_Count + 1
        elif row[2] == "Diana DeGette":
            Diana_Count = Diana_Count + 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Count = Raymon_Count + 1

Charles_PCT = (Charles_Count/Total_Votes)
Diana_PCT = (Diana_Count/Total_Votes)
Raymon_PCT = (Raymon_Count/Total_Votes)
Charles_PCT1 = "{:.3%}".format(Charles_PCT)
Diana_PCT1 = "{:.3%}".format(Diana_PCT)
Raymon_PCT1 = "{:.3%}".format(Raymon_PCT)

print("Election Results")
print("------------------------")
print("Total Votes:", Total_Votes)
print("------------------------")
print("Charles Casper Stockham:","{:.3%}".format(Charles_PCT), "(",Charles_Count,")")
print("Diana DeGette:","{:.3%}".format(Diana_PCT), "(",Diana_Count,")")
print("Raymon Anthony Doane:","{:.3%}".format(Raymon_PCT), "(",Raymon_Count,")")

output_path = os.path.join("analysis", "analysis.txt")
with open(output_path,'w') as f:
    f.writelines("Election Results")
    f.writelines("\n")
    f.writelines("------------------------")
    f.writelines("\n")
    f.writelines(f'Total Votes:, {Total_Votes}')
    f.writelines("\n")
    f.writelines("------------------------")
    f.writelines("\n")
    f.writelines(f'Charles Casper Stockham:{Charles_PCT1}, ({Charles_Count})')
    f.writelines("\n")
    f.writelines(f'Diana DeGette:,{Diana_PCT1} ({Diana_Count})')
    f.writelines("\n")
    f.writelines(f'Raymon Anthony Doane:{Raymon_PCT1}, ({Raymon_Count})')
