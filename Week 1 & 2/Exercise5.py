# Monthly expenses list
expenses = [2200, 2350, 2600, 2130, 2190]

# Task 1: In Feb, how many dollars you spent extra compared to January?
extra_spent_in_feb = expenses[1] - expenses[0]
print("Extra dollars spent in Feb compared to January:", extra_spent_in_feb)

# Task 2: Find out your total expense in the first quarter (first three months) of the year.
total_expense_first_quarter = sum(expenses[:3])
print("Total expense in the first quarter:", total_expense_first_quarter)

# Task 3: Find out if you spent exactly 2000 dollars in any month.
spent_2000_dollars = 2000 in expenses
print("Did you spend exactly 2000 dollars in any month?", spent_2000_dollars)

# Task 4: June month just finished, and your expense is 1980 dollars. Add this item to our monthly expense list.
expenses.append(1980)
print("Updated monthly expenses list with June:", expenses)

# Task 5: You returned an item that you bought in the month of April and got a refund of 200 dollars. Make a correction to your monthly expense list based on this.
refund_amount = 200
expenses[3] -= refund_amount
print("Updated monthly expenses list after the refund in April:", expenses)

# List of favorite Marvel superheroes
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Task 1: Length of the list
length_of_list = len(heroes)
print("Length of the heroes list:", length_of_list)

# Task 2: Add 'black panther' at the end of this list
heroes.append('black panther')
print("Updated heroes list with 'black panther' at the end:", heroes)

# Task 3: Move 'black panther' after 'hulk'
heroes.remove('black panther')
index_of_hulk = heroes.index('hulk')
heroes.insert(index_of_hulk + 1, 'black panther')
print("Updated heroes list with 'black panther' after 'hulk':", heroes)

# Task 4: Replace thor and hulk with doctor strange
heroes[1:3] = ['doctor strange']
print("Updated heroes list with thor and hulk replaced by doctor strange:", heroes)

# Task 5: Sort the heroes list in alphabetical order
heroes.sort()
print("Sorted heroes list in alphabetical order:", heroes)

