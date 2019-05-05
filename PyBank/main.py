# Import dependencies
import os
import csv

# Assign value to variable
total_months = 0
total_revenue = 0


# Set a a path for the file
budget_summary = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_summary, newline="") as csv_file:

    #Split the data 
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row
    csv_header = next(csv_file)

    # Read each row of data
    for row in csv_reader: 

    # Total months can be found by counting the number of rows after the header
        total_months += 1

    # Total can be found by summing up the Profit/Loss column
        total_revenue += int(row[1])

    # Average Change can be found by dividing the total by total months 
        average_change = (total_revenue/total_months)

    # Greatest Increase can be found by locating the row with the highest (max) value then the relating month
        greatest_increase_amount = max(row[1])
        #greatest_increase_month = 
    # Greatest Decrease can be found by locating the the lowest (min) value then the relating month
        greatest_decrease_amount = min(row[1])
        #greatest_decrease_month = 

# Print out the Summary
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: ${greatest_increase_amount}")
print(f"Greatest Decrease: ${greatest_decrease_amount}")

# Set a path to the output file
analysis_output = os.path.join("analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(analysis_output, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows of data to a csv
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total Revenue: ${total_revenue}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase: ${greatest_increase_amount}"])
    csvwriter.writerow([f"Greatest Decrease: ${greatest_decrease_amount}"])



    
      

