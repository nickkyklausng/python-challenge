#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Import OS Module
import os

import csv

 #Define the variables of Pybank
    
months = []
changes_in_p_l = []

month_count = 0
net_profit_loss = 0
previous_month_p_l =0
current_month_p_l = 0
p_l_change = 0

csvpath = "/Users/sophia/Desktop/Python/Homework/python-challenge/Resources/PyBank CSV File/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)
    print("csvreader"+ str(csv_header))
    for row in csvreader:
    
    # Count Months
        month_count += 1

    # Net total of Profit and Loss over the entire period
        current_month_p_l = int(row[1])
        net_profit_loss += current_month_p_l

        if (month_count == 1):
        
    # Equalise values of previous months to current month
            previous_month_p_l = current_month_p_l

    else: 

    #Calculate change to  profit and loss
            p_l_change = current_month_p_l - previous_month_p_l

    #Append each month to Months[List]
            months.append(row[0])
    #Append each profit and loss change to the p_l_change[Lists]
            changes_in_p_l.append(p_l_change)
    #Reset loop by making current month's profit and loss to previous months' profit and loss.
            previous_month_p_l = current_month_p_l

#Calculate both the sum and average of "Profit and Losses"  over the reported period.
sum_p_l = sum(changes_in_p_l)
average_p_l = changes_in_p_l/(month_count-1)
#Highest and Lowest Changes over reported period
highest_change = max(changes_in_p_l)
lowest_change = min(changes_in_p_l)

#locate indexes of highest and lowest changes.

highest_month  =  changes_in_p_l.index(highest_change)
lowest_month = changes_in_p_l.index(lowest_change)

#Create and Assign Best and Worst months's performance.

best_month = months[highest_month]
worst_month = months[lowest_month]

#Print onto Terminal

print("Financial Analysis")

#print("------------------------------------------")

#print(f"Total Months:{month_count}")

#print(f"Total:${net_profit_loss}")

#print(f"Average Change:${average_p_l}")

#print(f"Greatest Increase in Profits:{best_month} (${highest_change})")

#print(f"Greatest Increase in Losses:{worst_month} (${lowest_change})")
