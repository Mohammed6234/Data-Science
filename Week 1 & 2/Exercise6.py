# City lists per country
india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Program to find the country of a given city
def find_country(city):
    if city.lower() in india:
        return "India"
    elif city.lower() in pakistan:
        return "Pakistan"
    elif city.lower() in bangladesh:
        return "Bangladesh"
    else:
        return "City not found in the list."

# Asking user to enter a city name
user_city = input("Enter a city name: ")
country = find_country(user_city)
print(f"The city '{user_city}' belongs to {country}.")

#p2
# Program to check if two cities belong to the same country
def check_same_country(city1, city2):
    country1 = find_country(city1)
    country2 = find_country(city2)
    
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country.")

# Asking user to enter two cities
user_city1 = input("Enter the first city name: ")
user_city2 = input("Enter the second city name: ")

check_same_country(user_city1, user_city2)



#p3

# Program to check if the fasting sugar level is normal, low, or high
def check_sugar_level(sugar_level):
    if sugar_level < 80:
        print("Sugar level is low.")
    elif sugar_level > 100:
        print("Sugar level is high.")
    else:
        print("Sugar level is normal.")

# Asking user to enter the fasting sugar level
user_sugar_level = float(input("Enter your fasting sugar level: "))
check_sugar_level(user_sugar_level)
