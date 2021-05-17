import os 
import csv

county_list = []
candidate_options = []
candidate_votes = {}
#dictionary format { "candidate 1" : votecount , "candidate 2" : votecount}
winning_candidate = ""
winning_count = 0
total_count = 0
total_votes = 0

print(total_votes)

csv_path = os.path.join('Election_Data.csv')
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        county_name = row[1]
        candidate_name = row[2]
        if county_name not in county_list:
            county_list.append(county_name)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
    print("The total number of votes cast: ", total_votes)
    print("List of counties:", county_list)
    print("List of candidates:" , candidate_options)

    csv_path = os.path.join('Election_Data.csv')
    


with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    headers = next(csvreader)
    for row in csvreader:
        candidate_name = row[2]
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 
    print(candidate_votes)

winning_count = 0
winning_percentage = 0


for candidate_name in candidate_options:
    votes = candidate_votes[candidate_name]
    vote_percentage = 100 * float(votes) / float(total_votes)
    print(f"{candidate_name}: received {votes} votes or {vote_percentage}% of the total vote count.")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name
print(f"Winning Candidate is {winning_candidate} with {winning_count} votes, which accounts for {winning_percentage}% of total votes!!!")




for i in county_list:
    candidate_votes = 0
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        headers = next(csvreader)
        county_vote_counter = 0
        for row in csvreader:
            if (row[1] == i):
                county_vote_counter = county_vote_counter + 1
    print(f"Total votes of {i} county is : {county_vote_counter}")

cli = ""
for i in county_list:
    print(f"Vote breakdown for {i} County:")
    for j in candidate_options:
        county_votes = 0
        with open(csv_path) as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ',')
            headers = next(csvreader)
            county_vote_counter = 0
            for row in csvreader:
                if (row[1] == i and row[2] == j):
                    county_votes = county_votes + 1
        print(f"Candidate name: {j} ---- {county_votes} votes counted.")
        cli = cli + f"County {i} : \n\n Candidate name: {j} - {county_votes} votes counted. \n"

             
        with open("election_results.txt", "w") as txt_file:
        # Print the final vote count to the terminal.
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                + cli)
            print(election_results, end="")
            # Save the final vote count to the text file.
            txt_file.write(election_results)