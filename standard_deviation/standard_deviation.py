from math import sqrt


def standard_deviation(values):
    """Calculates standard deviation from a list of values"""
    mean = sum(values) / len(values)
    squared_deviations = [(mean - value) ** 2 for value in values]
    result = sqrt(
        sum(squared_deviations) / (len(values) - 1)
    )

    return result


if __name__ == '__main__':
    print(standard_deviation([1, 5, 2, 7, 1, 9, 3, 8, 5, 9]))
