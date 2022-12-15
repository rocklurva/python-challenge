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

print(f"Total Months: {total_months}") 

#initialising net_total
net_total = 0

for amount in data:
    #cumulatively add the profit or loss to net_total
    net_total=net_total+int(amount[1])

print(f"Total: ${net_total}")

changes = []

# for changes in data:
    # print(change)
