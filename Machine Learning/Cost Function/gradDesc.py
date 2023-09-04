import numpy as np  # Import the numpy library for numerical operations

def gradient_descent(x, y):
    m_curr = b_curr = 0  # Initialize the slope (m) and intercept (b) to zero
    iterations = 10000  # Number of iterations for the gradient descent algorithm
    n = len(x)  # Number of data points
    learning_rate = 0.08  # Learning rate for gradient descent

    for i in range(iterations):
        # Calculate the predicted values of y using the current m and b
        y_predicted = m_curr * x + b_curr

        # Calculate the cost, which is the mean squared error
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])

        # Calculate the partial derivatives of the cost function with respect to m and b
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)

        # Update the values of m and b using gradient descent
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        # Print the current values of m, b, cost, and iteration number
        print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

# Call the gradient_descent function with the provided data
gradient_descent(x, y)
