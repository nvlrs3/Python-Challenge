# Import packages
import os
import csv

# Import CSV
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Establish necessary variables
    Count = 0
    Total = 0
    PriorRow = []
    CurrentRow = []

    # Iterate through the rows in the CSV
    for row in csv_reader:
        Count = Count + 1
        Total = int(row[1]) + Total
        PriorRow.append(row[1])
        CurrentRow.append(row[1])

    # Start the building blocks for the average change.
    PriorRow_Index = range(0, len(PriorRow)-1)
    PriorRow_List = list(PriorRow_Index)
    PriorRow_Value = []

    for index in PriorRow_List:
        PriorRow_Value.append(PriorRow[index])

    CurrentRow_Index = range(1, len(CurrentRow))
    CurrentRow_List = list(CurrentRow_Index)
    CurrentRow_Value = []

    for index in CurrentRow_List:
        CurrentRow_Value.append(CurrentRow[index])

    #Calculate the average change and iterate to find the corresponding dates.
    TotalChange = 0

    for Value in range(0, len(CurrentRow_Value)):
        Change = int(CurrentRow_Value[int(Value)]) - int(PriorRow_Value[int(Value)])
        TotalChange = TotalChange + Total
        AverageChange = TotalChange / (Count - 1)
        GreatestIncrease = max(Change)
        GreatestDecrease = min(Change)
        if GreatestIncrease == csv_reader[1]:
            GreatestIncreaseMonth = csv_reader[0]
        elif GreatestDecrease == csv_reader[1]:
            GreatestDecreaseMonth = csv_reader[0]
        End if

# Output to the terminal.
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " & Count)
print("Total: $" & Total)
print("Average Change: $" & AverageChange)
print("Greatest Increase in Profits: " & GreatestIncreaseMonth & "($" & GreatestIncrease &")")
print("Greatest Decrease in Profits:" & GreatestDecreaseMonth & "($" & GreatestDecrease &")")

# Output to text file.
L1 = "Financial Analysis"
L2 = "-------------------------------"
L3 = "Total Months: " & Count
L4 = "Total: $" & Total
L5 = "Average Change: $" & AverageChange
L6 = "Greatest Increase in Profits: " & GreatestIncreaseMonth & "($" & GreatestIncrease &")"
L7 = "Greatest Decrease in Profits:" & GreatestDecreaseMonth & "($" & GreatestDecrease &")"

lines= [L1, L2, L3, L4, L5, L6, L7] 
with open("Output", w) as f:
    for line in lines:
        f.write(line)
        f.write("\n")