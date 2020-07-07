import os
import csv 
fileload = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis", "budget_analysis.txt")
totalmonths =0
totalnet = 0
netchangelist = []
monthlist = []
greatestincrease = ["",0]
greatestdecrease = ["",999999999]
with open (fileload) as csvfile: 
    reader = csv.reader(csvfile)
    header = next (reader)
    firstrow = next(reader)
    totalmonths = totalmonths + 1
    totalnet = totalnet + int(firstrow[1])
    previousnet = int(firstrow[1])
    for row in reader: 
        totalmonths = totalmonths + 1
        totalnet = totalnet + int(row[1])
        change = int(row[1]) - previousnet
        previousnet = int(row[1])
        netchangelist = netchangelist + [change]
        monthlist = monthlist + [row[0]]
        if change > greatestincrease [1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = change
        if change < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = change   
averagechange = sum(netchangelist)/len(netchangelist)
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${totalnet}\n"
    f"Average  Change: ${averagechange:.2f}\n"
    f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})\n"
    f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})\n")
print(totalmonths)
print(totalnet)
print(round(averagechange, 2))
print(greatestincrease[0], greatestincrease[1])
print(greatestdecrease[0], greatestdecrease[1])
with open(outputfile, "w") as text_file: 
    text_file.write (output)