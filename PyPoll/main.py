# Import packages
import os
import csv

# Import CSV
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Establish the necessary variable
    Count = 0
    Candidates = []

    # Iterate through the rows in the CSV
    for row in csv_reader:
        Count = Count + 1
        Candidates = row[2]

    # Look for duplicate candidates and populate a list with no duplicate
    Candidates_No_Dupes = []
    
    for i in Candidates:
        if i not in Candidates_No_Dupes:
            Candidates_No_Dupes.append(i)

    # Calculate the vote percentage for each candidate.    
    for row in csv_reader:
        for i in Candidates_No_Dupes:
            if row[2] == Candidates_No_Dupes[i]:
                VotePercentage = "{:.0000%".format(Candidates_No_Dupes.append(1) / Count)
                VoteCount = Candidates_No_Dupes.append(2)
            End if
    
print("Election Results")   
print("-------------------------------")
print("Total Votes: " & Count)
print("-------------------------------")
for i in Candidates_No_Dupes:
    print(Candidates_No_Dupes[i] & ":" & VotePercentage[i] & "(" & VoteCount[i] & ")")
print("-------------------------------")
if i == max(Candidates_No_Dupes[1]):
    print("Winner:" & Candidates_No_Dupes[i])
print("-------------------------------")

# Output to text file.
L1 = "Election Results"
L2 = "-------------------------------"
L3 = "Total Votes: " & Count
for i in Candidates_No_Dupes:
    L5 = Candidates_No_Dupes[i] & ":" & VotePercentage[i] & "(" & VoteCount[i] & ")")
if i == max(Candidates_No_Dupes[1]):
    L7 = "Winner:" & Candidates_No_Dupes[i]

lines= [L1, L2, L3, L2, L5, L2, L7, L2] 
with open("Output", w) as f:
    for line in lines:
        f.write(line)
        f.write("\n")
        