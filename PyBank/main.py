import csv
import os
import pandas as pd

csvpath = os.path.join("Resources", "budget_data.csv")
total_months = 0
total_profit_loss = 0 
previous_profit_loss = 0 


with open(csvpath, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:

        total_months += 1 

        total_profit_loss += int(row[1])
    
df = pd.read_csv(csvpath)
df['diff'] = df['Profit/Losses'].diff()
average_change = round(df['diff'].mean(),4)
  
greatest_increase_index = df['diff'].idxmax()
greatest_increase_date = df.loc[greatest_increase_index, 'Date']
greatest_increase_amount = int(df.loc[greatest_increase_index, 'diff'])

greatest_decrease_index = df['diff'].idxmin()
greatest_decrease_date = df.loc[greatest_decrease_index, 'Date']
greatest_decrease_amount = int(df.loc[greatest_decrease_index, 'diff'])

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average change in Profit/Losses:, ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date}  ${greatest_increase_amount} ")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}  ${greatest_decrease_amount} ")



output_path = os.path.join("Analysis", "Financial_Analysis.txt")


with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average change in Profit/Losses:, ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date}  ${greatest_increase_amount}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date}  ${greatest_decrease_amount}\n")

