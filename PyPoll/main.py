import csv

#to load up data into a list
with open("Resources/election_data.csv", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data=[]
    next(rows)
    for row in rows:
        data.append(row)

print('Election Results')
print('------------------------------\n')

#get the total amout using len and print results
total = len(data)
print(f'Total Votes: {total}')
print('------------------------------\n')

#using list comprehension to get the candidate name
candidates = [candidate[2] for candidate in data]
distinct_candidates = list(set(candidates))

#define a custom function for calculating total votes for each matching candidate
def total_votes(candidate):
    total = 0
    for i in range(0, len(candidates)):
        if candidate == candidates[i]:
            total+=1
    return total

#using the function above, show the total votes for each candidate and the percentage of it

election_results= []

for j in range(0, len(distinct_candidates)):
    total_vote_candidate = total_votes(distinct_candidates[j])
    percentage = round(total_vote_candidate/total*100, 3)
    print(f'{distinct_candidates[j]}: {percentage}% ({total_vote_candidate})')
    election_results.append([distinct_candidates[j], total_vote_candidate])

print('------------------------------\n')

#initialise dictionary for election results
election_dict = {}

print(f'{election_results}')

for i in range(0, len(election_results)):
    #add election results to dictionary
    election_dict.update({election_results[i][0]: election_results[i][1]})

#find the maximum vote count, and show who is the winner
election_winner = max(election_dict, key=election_dict.get)
print(f'The winner is: {election_winner}')
