class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.prev, self.curr = 0, 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration

        if self.counter == 0:
            self.counter += 1
            return self.prev
        elif self.counter == 1:
            self.counter += 1
            return self.curr
        else:
            self.prev, self.curr = self.curr, self.prev + self.curr
            self.counter += 1
            return self.curr


# Example usage:
fibonacci_limit = 10  # Set the limit for the Fibonacci series
fibonacci_iter = FibonacciIterator(fibonacci_limit)

for num in fibonacci_iter:
    print(num)
