#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0
#total county count
total_county = 0

#Candidate Options and candidate votes
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}

#Counties
county_options = []
#County dictionary
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Winning county
winning_county = ""

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
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:        
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0 
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1  
        
    for row in file_reader:
        # Add to the total county
        total_county += 1
        # Print county name for each row
        county_name = row[1]
        # If the county name  does not match any existing county...
        if county_name not in county_options:        
            # Add the county name to the county list.
            county_options.append(county_name)
            # Begin tracking that counties count
            county_votes[county_name] = 0 
        # Add a vote to that counties count.
        county_votes[county_name] += 1        

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

     #  To do: print out the total votes per county, vote count and percentage to
    #   terminal.
    #county_summary = (
        #f"County Votes:\n"
        #f"----------\n"
        #f"{county_name}: {county_votes:.1f}% ({votes:,})\n")
    #print(county_summary)
    # Save the winning candidate's results to the text file.
    #txt_file.write(county_summary)
   
     #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
    winning_county_summary = (
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
        # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)
    
    for county in county_votes:
        # Retrieve vote count of a county.
        votes = county_votes[county]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_county) * 100
        # Print the candidate name and percentage of votes.
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        county_votes = (
        f"{county_name}: {county_votes:.1f}% ({county:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(county_votes)
        #  Save the candidate results to our text file.
        txt_file.write(county_votes)
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (
        f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

   






                        