#Standard imports
import os
import csv

PyPoll = os.path.join('.','Election_poll.csv')
#Set values for each candidate
Total_Cast = 0
Khan = 0
Correy = 0
Li = 0
Otooly = 0

#Set up the new line and delimiter and row
with open(PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    row = next(csvreader)
    Vote = row[2] #Not used in the python more to remind myself
#For loop setup 
    for row in csvreader:
        Total_Cast = Total_Cast + 1
       
        if (row[2] == "Khan"):
            Khan = Khan + 1
        elif (row[2] == "Correy"):
            Correy = Correy + 1
        elif (row[2] == "Li"):
            Li = Li + 1
        else: #make sure is else rather than elif otherwise will return 0
            Otooly = Otooly + 1
    #Finding the total % each person recieved in the poll, not use how to set it to %
    Khan_total = Khan/Total_Cast
    Correy_total = Correy/Total_Cast
    Li_total = Li/Total_Cast
    Otooly_total = Otooly/Total_Cast
    Winner = max(Khan, Correy, Li, Otooly)
     
     #Second if statement to define winner
    if Winner == Khan:
        Winner_name = "Khan"
    elif Winner == Correy:
        Winner_name = "Correy"
    elif Winner == Li:
        Winner_name = "Li"
    else:
        Winner_name = "Otooly"
#Print results in % (https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python)
print("Election Results")
print("--------------------------------------------------------------------------------")
print(f"Total Votes: {Total_Cast}")
print("--------------------------------------------------------------------------------")
print(f"Khan: {Khan_total: .2%} ({Khan})")
print(f"Correy: {Correy_total: .2%} ({Correy})")
print(f"Li: {Li_total: .2%} ({Li})")
print(f"Otooly: {Otooly_total: .2%} ({Otooly})")
print("--------------------------------------------------------------------------------")
print(f"The winner is {Winner_name}")

Poll_report = os.path.join('.', 'Poll_results.txt')

with open(Poll_report, 'w') as text:
# new line help https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
    text.write("Election Results\n")
    text.write("--------------------------------------------------------------------------------\n")
    text.write(f"Total Votes: {Total_Cast}\n")
    text.write("--------------------------------------------------------------------------------\n")
    text.write(f"Khan: {Khan_total: .2%} ({Khan})\n")
    text.write(f"Correy: {Correy_total: .2%} ({Correy})\n")
    text.write(f"Li: {Li_total: .2%} ({Li})\n")
    text.write(f"O'Tooley: {Otooly_total: .2%} ({Otooly})\n")
    text.write("--------------------------------------------------------------------------------\n")
    text.write(f"The winner is {Winner_name}\n")
