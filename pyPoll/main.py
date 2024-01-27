# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  # The total number of votes cast

  # A complete list of candidates who received votes

  # The percentage of votes each candidate won

  # The total number of votes each candidate won

  # The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

  #```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

pollData = os.path.join(".","Resources","election_data.csv")
#currentDirectory = os.getcwd()
#print(currentDirectory)
#print(pollData)

# Open the CSV file
with open(pollData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of votes cast (row count after the header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # Create new list from CSV column "C" to get a complete list of candidates who received votes
    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)

  # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # The winner of the election based on popular vote.
    winner = votes.index(max(votes))    

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candilist[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candilist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))