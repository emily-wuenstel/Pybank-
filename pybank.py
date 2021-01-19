#Basics - import OS and CSV
import os
import csv

#create path to the file we will be using and open the file
budget_data =  os.path.join('Resources/budget_data.csv')

#Print the header information
print("Financial Analysis")
print("------------------------------")

#open the file as a CSV so we can read it
with open(budget_data) as csvfile:
    pybank_csv = csv.reader(csvfile, delimiter = ',')


#The total number of months included in the dataset - count how many rows, without the header
#Also calculate the net total and report out
#Also keep track of the average change 
#Also keep track of greatest increase day and greatest decrease day 

    #define header and variables to be used 
    header = next(pybank_csv)
    total_months = 0 
    net_total = 0
    greatest_increase = 0
    greatest_decrease = 0 
    change_total = 0 
    first_row = 1 
    running_total = 0

    #for each row, count the row and add the total
    if header != None:
        for row in pybank_csv:
            profitloss = int(row[1])
            total_months = total_months + 1
            net_total = net_total + profitloss

            #keep track of the greatest increase, store date and value to print later
            if int(row[1]) > int(greatest_increase):
                inc_date = row[0]
                greatest_increase = row[1]

            #keep track of the greatest decrease, store date and value to print later
            if int(row[1]) < int(greatest_decrease):
                dec_date = row[0]
                greatest_decrease = row[1]

            #Keep track of the increase / decrease change - take the current line and subtract the one before it
            if first_row != 1:
                running_total = running_total + (int(row[1]) - first_value)
                first_value = int(row[1])

            if first_row == 1:
                first_value = int(row[1])
                first_row = 2
    
    average_change = "{:.2f}".format(running_total / (total_months-1))

    #print data out with requested format
    print(f"Total Months:  {total_months}")
    print(f"Total: ${net_total}")
    print(f'Average Change: {average_change}')
    print(f"Greatest Increase in Profits: {inc_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {dec_date} (${greatest_decrease})")

#Qrite output to a txt file in the same folder
output_file = os.path.join("pybank_output.txt")

text_file = open(output_file, 'w')
text_file.write("Financial Analysis \n")  
text_file.write("------------------------------ \n")  
text_file.write(f"Total Months:  {total_months} \n")
text_file.write(f"Total: ${net_total} \n")
text_file.write(f'Average Change: {average_change} \n')
text_file.write(f"Greatest Increase in Profits: {inc_date} (${greatest_increase}) \n")
text_file.write(f"Greatest Decrease in Profits: {dec_date} (${greatest_decrease})")

text_file.close()

