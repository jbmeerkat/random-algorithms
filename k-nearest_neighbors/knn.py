import pandas as pd
from math import sqrt
from collections import Counter


def load_dataset(file):
    dataset = pd.read_csv(file).to_numpy().tolist()

    print(f"Dataset sample:")
    print(*dataset[:5], sep="\n")
    print()

    return dataset


def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError(
            f"Vectors must be of the same length. Got {vector1} and {vector2}."
        )

    distance = sqrt(
        sum(
            (v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)
        )
    )

    return distance


def knn(train, test, k):
    distances = [(row, euclidean_distance(row[1:], test)) for row in train]
    distances.sort(key=lambda distance: distance[1])

    return distances[0:k]


def predict_class(train, test, k):
    neighbors = knn(train, test, k)
    classes = [neighbor[0][0] for neighbor in neighbors]

    prediction = Counter(classes).most_common(1)[0][0]

    return prediction


train = load_dataset('cats_dataset.csv')
test = [27, 51, 3.7]
number_of_neighbors = 20

print(f"Classifying a cat with height, length and weight {test}")
print()

prediction = predict_class(train, test, number_of_neighbors)
print(f"Breed prediction for the cat is {prediction}")
