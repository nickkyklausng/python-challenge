#PyPoll
import os
import csv

# set a csv file path for the data
csvpath = "/Users/sophia/Desktop/Python/Homework/python-challenge/Resources/PyPoll CSV File/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"
poll_csv = os.path.join('csvpath')

print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print("csvreader"+ str(csv_header))
    for row in csvreader: