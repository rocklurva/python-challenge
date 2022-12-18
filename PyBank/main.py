import csv

#to load up data into a list
with open("Resources/budget_data.csv", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data=[]
    next(rows)
    for row in rows:
        data.append(row)

#initialising total_months count
total_months = 0

for month in data:
    #tally up total_months for each row
    total_months+=1

print(f"Total Months: {total_months}\n") 

#initialising net_total
net_total = 0

for amount in data:
    #cumulatively add the profit or loss to net_total
    net_total=net_total+int(amount[1])

print(f"Total: ${net_total}\n")

#initialise profit loss list
profit_loss_difference = []
profit_loss_dict = {}

#for this for loop, we will start from second record as first record does not have anything to compare with
for i in range(1, len(data)):
    difference = int(data[i][1]) - int(data[i-1][1])
    
    #add date and difference as key value pairs in profit_loss_dict
    profit_loss_dict.update({data[i][0]: difference})
    profit_loss_difference.append(difference)

average_profit_loss = sum(profit_loss_difference)/len(profit_loss_difference)
print(f"Average Change: ${round(average_profit_loss, 2)}\n")

# The greatest increase in profits (data and amount) over the entire period
greatest_increase_date = max(profit_loss_dict, key=profit_loss_dict.get)
greatest_increase = max(profit_loss_dict.values())

print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease_date = min(profit_loss_dict, key=profit_loss_dict.get)
greatest_decrease = min(profit_loss_dict.values())

print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")