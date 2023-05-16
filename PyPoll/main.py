import csv
import os
import pandas as pd

election_data = os.path.join("Resources", "election_data.csv")
#election_data =  '/Users/win/Desktop/python_challenge-moduel-3-/PyPoll/Resources/election_data.csv'

data = pd.read_csv(election_data)

total_votes = data['Ballot ID'].count()
vote_count = data['Candidate'].value_counts()
vote_percentage = round((vote_count / total_votes) * 100, 3)
winner = str(vote_count.idxmax())

#print(vote_count)
#print(total_votes)
#print(vote_percentage)
#print(winner)
#print(vote_count.index)

print("Election Results")
print("-----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------------------------")

for i in vote_count.index:
        print(f"{i}: {vote_percentage[i]:.3f}% ({vote_count[i]})")

print("-----------------------------------------------------------")
print(f"winner: {winner}")
print("-----------------------------------------------------------")

output_path = os.path.join("Analysis", "Election Results.txt")
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-----------------------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-----------------------------------------------------------\n")

    for i in vote_count.index:
         file.write(f"{i}: {vote_percentage[i]:.3f}% ({vote_count[i]})\n")

    file.write("-----------------------------------------------------------\n")
    file.write(f"winner: {winner}\n")
    file.write("-----------------------------------------------------------\n")