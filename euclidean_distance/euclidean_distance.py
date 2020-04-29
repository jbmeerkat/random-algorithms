from math import sqrt


def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vector must be of the same length.')

    distance = sqrt(
        sum(
            (v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)
        )
    )

    return distance


vector1 = [1, 2, 3, 4]
vector2 = [5, 6, 7, 8]

distance = euclidean_distance(vector1, vector2)

print(f"Distance between vectors {vector1} and {vector2} is {distance}")
