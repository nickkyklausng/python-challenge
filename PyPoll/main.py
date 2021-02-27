#PyPoll
import os
import csv

# set a csv file path for the data
csvpath = "/Users/sophia/Desktop/Python/Homework/python-challenge/Resources/PyPoll CSV File/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
poll_csv = os.path.join('csvpath')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
#The total number of votes cast
#Read Header Row  
    csv_header = next(csvfile)
    
    #Number of rows 
    num_row = 0

    #Each candidate's total votes
    total_votes_dict = {}

    results[]

    for row in csvreader:
        
        #Total number of votes casted

        num_rows += 1

        if row[2] not in totalvotesDic.keys():
            totalvotesDic[row[2]] = 1
        else:
            totalvotesDic[row[2]] += 1

print("Election Results")
print("-----------------------")
print(f"Total Votes: {(num_rows)}")
print("-----------------------")



print(csvpath)



#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.