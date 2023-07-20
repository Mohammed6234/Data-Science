population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
    
    
    
    
# Initial stock data
stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

# Function to calculate the average of a list of prices
def calculate_average(prices):
    return sum(prices) / len(prices)

# Program to handle stock operations
while True:
    operation = input("Enter operation (print/add/exit): ")
    
    if operation == 'print':
        for stock, prices in stocks.items():
            avg_price = calculate_average(prices)
            print(f"{stock} ==> {prices} ==> avg: {avg_price:.2f}")
    elif operation == 'add':
        stock_ticker = input("Enter stock ticker: ")
        price = float(input("Enter price: "))
        if stock_ticker in stocks:
            stocks[stock_ticker].append(price)
        else:
            stocks[stock_ticker] = [price]
    elif operation == 'exit':
        break
    else:
        print("Invalid operation. Try again.")
        
        
        
import math

def circle_calc(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

# Example usage:
radius_input = float(input("Enter the radius of the circle: "))
area, circumference, diameter = circle_calc(radius_input)
print("Area:", area)
print("Circumference:", circumference)
print("Diameter:", diameter)
