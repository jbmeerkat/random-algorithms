# Naive gradient descent implementation
# Line equation is `y = mx + b`, where `m` is a slope and `b` is y-intercept

import itertools
import csv

def cost(b, m, points):
    """Calculates error (or cost) for given line and set of points"""
    total_error = 0
    for point in points:
        x = float(point[0])
        y = float(point[1])
        total_error += (y - (m * x + b)) ** 2

    return total_error / float(len(points))

def step_gradient(b, m, points, learning_rate):
    """Calculates step using partial derivatives"""
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for point in points:
        x = float(point[0])
        y = float(point[1])
        b_gradient += -(2/N) * (y - ((m * x) + b))
        m_gradient += -(2/N) * x * (y - ((m * x) + b))
    new_b = b - (learning_rate * b_gradient)
    new_m = m - (learning_rate * m_gradient)

    return [new_b, new_m]

def gradient_descent(points, b, m, learning_rate, iterations):
    for _ in itertools.repeat(None, iterations):
        b, m = step_gradient(b, m, points, learning_rate)

    return [b, m]

def start_descent():
    points = list(csv.reader(open('points.csv', newline='')))
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    iterations = 1000

    initial_error = cost(initial_b, initial_m, points)
    print(f"Starting gradient descent at b = {initial_b}, m = {initial_m}, error = {initial_error}")

    print ("Running...")
    [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, iterations)

    resulting_error = cost(b, m, points)
    print(f"After {iterations} iterations b = {b}, m = {m}, error = {resulting_error}")

if __name__ == '__main__':
    start_descent()
