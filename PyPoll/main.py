# import dependencies 
import os
import csv

# Assign value to variables 
max_votes = 0
total_votes = 0

#Assign variables to store data
candidate_votes = {}
candidate_list = []

# Set a a path for the file
poll_summary = os.path.join("election_data.csv")

# Open and read csv
with open(poll_summary, newline="") as csv_file:

    #Split the data 
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row
    csv_header = next(csv_file)

    # Read each row of data
    for row in csv_reader: 

        #Count Total Votes
        total_votes += 1
   
        #Get Candidate Names
        candidate_name = (row[2])
   
        #Loop to keep the data clean
    for candidate_name not in candidate_list:
        candidate_list.append(candidate_name)
        candidate_votes[candidate_name]=0
       
candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    #Loop through the data
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name) == candidate_votes[candidate_name]
        vote_percentage = (votes/total_votes) * 100
        if(votes > max_votes):
            max_votes = votes
            winning_candidate = candidate_name

    #Print out the summary
    print(f"Total Votes: {total_votes}")
    print(f"Candidate Name: {candidate_name}")
    print(f"Vote Percentage: {vote_percentage}%")
    print(f"Candidate Votes: {candidate_votes}")
    print(f"Election Winner: {winning_candidate}!")
   
# Set a path to the output file
poll_output = os.path.join("poll_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(poll_output, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows of data to a csv
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([f"Candidate Name: {candidate_name}"])
    csvwriter.writerow([f"Vote Percentage: {vote_percentage}%"])
    csvwriter.writerow([f"Candidate Votes: {candidate_votes}"])
    csvwriter.writerow([f"Election Winner: {winning_candidate}!"])
