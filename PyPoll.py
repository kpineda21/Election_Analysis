# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0

#Candidate Options and candidate votes
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}

#county options
county_names =[]
county_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

largest_county_turnout =""
largest_county_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        #county name from each row
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0 
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1  
        
        if county_name not in county_names:        
            # Add the county name to the county list.
            county_names.append(county_name)
            # Begin tracking that counties count
            county_votes[county_name] = 0 
        # Add a vote to that counties count.
        county_votes[county_name] += 1    
        
#save results
with open (file_to_save,"w") as txt_file:
    election_results =(
        f"\nElection Results\n"
        f"\n-----------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n-----------------\n\n"
        f"County Votes:\n"
    )      
    print(election_results, end="")
    txt_file.write(election_results)
        
    #challenge save final county votes
    for county in county_votes:
        #retrieve vote count
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) *100
        county_results = (
            f"{county}: {county_percent:1f}% ({county_vote:,})\n"
        )  
        print(county_results, end="")
        txt_file.write(county_results)  
        
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
            
    largest_county_turnout = (
        f"\n---------------------------\n"
        f"Largest County Turnout:{largest_county_turnout}\n"
        f"-----------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)
    
    for candidate in candidate_votes:
        votes= candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) *100
        candidate_results =(
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        txt_file.write(candidate_results)
        
        #determine winning vote count
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
            
    winning_candidate_summary =(
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    