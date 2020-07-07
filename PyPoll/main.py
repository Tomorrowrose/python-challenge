import os
import csv 
fileload = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("Analysis", "election_data.txt")
candidate_votes = {}
with open(fileload) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        candidate = row [2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1
with open (outputfile,"w") as text_file:

    totalvotes = sum(candidate_votes.values())
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    text_file.write(election_results)
    percent = []
    for i in candidate_votes:
        percent = round((float(candidate_votes[i])/totalvotes)*100,0)
    for key in candidate_votes.keys():
        if candidate_votes[key] == max(candidate_votes.values()):
            winner = key
    for i in candidate_votes:
        percent = round((float(candidate_votes[i])/totalvotes)*100,0)
        output = (f" {i} : %{percent} ({candidate_votes[i]})")
        text_file.write(output)
        print("  Election Results")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    print("------------------------------------------")
    print(f" Total Votes : {totalvotes}")
    print("------------------------------------------")
    for i in candidate_votes:
        percent = round((float(candidate_votes[i])/totalvotes)*100,0)
        print(f" {i} : %{percent} ({candidate_votes[i]})")
    print("------------------------------------------")
    print(f" The winner is : {winner}")
    print("------------------------------------------")
