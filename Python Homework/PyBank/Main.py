#Standard import
import os
import csv

#Join correct path
PyBank_csv = os.path.join('.', 'Budget_Data.csv')

#Set Variables
Months = 0
Net_total = 0
Greatest_increase = 0
Greatest_decrease = 0
Greatest_month_increase = 0
Greatest_month_decrease = 0
Month_change = []
Count_months = []

#Initial set up to split csv by comma 
with open(PyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    row = next(csvreader)
    #Account for previous row and months
    previous_row = int(row[1])
    Months = Months + 1
    Net_total = Net_total + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    #For loop
    for row in csvreader:
        Months = Months + 1 #Every time the row goes to the next one, month will add a + 1
        Net_total = Net_total + int(row[1]) #Same for Net total (can be negative number)

         # Calculate Change From Current Month To Previous Month
        Rev_change = int(row[1]) - previous_row
        Month_change.append(Rev_change)
        previous_row = int(row[1])
        Count_months.append(row[0])
        
        #Find the greatest increase and decrease
        if int(row[1]) > Greatest_increase:
            Greatest_increase = int(row[1])
            Greatest_month_increase = (row[0])

        if int(row[1]) < Greatest_decrease:
            Greatest_decrease = int(row[1])
            Greatest_month_decrease = (row[0])
        
        #Find average and min/max. (I might have been able to d this with sum(Month_change)/Months but this seemed cleaner
        Average = sum(Month_change)/ len(Month_change)
        Max = max(Month_change)
        Min = min(Month_change)
#Printing out results
print("Financial Report")        
print("-" * 80)
print(f"Total month: {Months}")
print(f"Total: ${Net_total}")
print(f"Average Change: ${Average}")
print(f"Greatest Increase in Profits: {Greatest_month_increase} (${Max})")
print(f"Greatest Increase in Profits: {Greatest_month_decrease} (${Min})")

#Text File
Bank_Report = os.path.join('.', 'Banking_report.txt')
# new line help https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
with open(Bank_Report, 'w') as text:
    text.write("Financial Report\n")
    text.write("--------------------------------------------------------------------------------\n")
    text.write(f"Total month: {Months}\n")
    text.write(f"Total: ${Net_total}\n")
    text.write(f"Average Change: ${Average}\n")
    text.write(f"Greatest Increase in Profits: {Greatest_month_increase} (${Max})\n")
    text.write(f"Greatest Increase in Profits: {Greatest_month_decrease} (${Min})\n")
