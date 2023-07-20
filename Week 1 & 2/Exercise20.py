def non_negative_integer(func):
    def wrapper(n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial can only be calculated for non-negative integers.")
        return func(n)
    return wrapper

@non_negative_integer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage:
try:
    print(factorial(1.354))
except ValueError as e:
    print(e)

try:
    print(factorial(-1))
except ValueError as e:
    print(e)

print(factorial(5))
