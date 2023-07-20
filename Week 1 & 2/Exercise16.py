def square_sequence_generator():
    number = 1
    while True:
        yield number ** 2
        number += 1

# Example usage:
square_gen = square_sequence_generator()

for _ in range(10):  # Print the first 10 square numbers
    print(next(square_gen))
