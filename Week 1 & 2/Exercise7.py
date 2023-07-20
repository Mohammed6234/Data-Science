# Flipping coin results
result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]

# Counting the number of times you got heads
heads_count = 0
for flip in result:
    if flip == "heads":
        heads_count += 1

print("Number of times you got heads:", heads_count)



# Printing square of all numbers between 1 to 10, except even numbers
for num in range(1, 11):
    if num % 2 != 0:
        print(num ** 2)



# Monthly expense list (from Jan to May)
expense_list = [2340, 2500, 2100, 3100, 2980]

# Program to find the month for a given expense amount
def find_month(expense_amount):
    for i, expense in enumerate(expense_list):
        if expense == expense_amount:
            return i + 1
    return None

# Asking user to enter an expense amount
user_expense = int(input("Enter an expense amount: "))
month = find_month(user_expense)

if month:
    print(f"The expense occurred in month {month}.")
else:
    print("Expense not found in the monthly list.")



# Program for the 5 km race simulation
for distance in range(1, 6):
    response = input(f"Upon completing {distance} km, are you tired? (yes/no): ")
    if response.lower() == "yes":
        print("You didn't finish the race.")
        break
else:
    print("Congratulations! You finished the race.")



# Printing the shape
for i in range(1, 6):
    print('*' * i)
