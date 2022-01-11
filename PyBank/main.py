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
    print(f"Header: {csv_header}")

    Count = 0
    Total = 0
    PriorRow = []
    CurrentRow = []

    for row in csv_reader:
        Count = Count + 1
        Total = int(row[1]) + Total
        PriorRow.append(row[1])
        CurrentRow.append(row[1])

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

#Change = CurrentRow_Value - PriorRow_Value

#analysis_CSV = zip(PriorRow_Value, CurrentRow_Value)

#with open(analysis_CSV) as csv_file:
    #analysis_CSV = csv.reader(csv_file, delimiter=",")
    
#analysis_file = os.path.join("analysis.csv")
    #for value in analysis_CSV:
        #Change = int(CurrentRow_Value[int(value),1]) - int(PriorRow_Value[int(value),0])
        #TotalChange = TotalChange + Change

    #for Value in CurrentRow_Value:
        #Change = int(CurrentRow_Value[int(Value)]) - int(PriorRow_Value[int(Value)])
    
    #Change = 0
    # Total2 = 0
    # CurrentChange = []

    #for Current_Value in CurrentRow_Value:
        #for Prior_Value in PriorRow_Value:
            #Change = int(CurrentRow_Value[int(Current_Value)]) - int(PriorRow_Value[int(Prior_Value)])
            

print(Count)
print(Total)
print(len(CurrentRow_Value))
print(len(PriorRow_Value))
print(CurrentRow_Value[84])
#print(Change)