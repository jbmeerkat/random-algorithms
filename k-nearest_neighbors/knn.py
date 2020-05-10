"""Simple KNN implementation"""

from math import sqrt
from collections import Counter
from itertools import chain
import pandas as pd


def load_dataset(file):
    """Loads dataset from file and prints a sample"""

    dataset = pd.read_csv(file).to_numpy().tolist()

    print("Dataset sample:")
    print(*dataset[:5], sep="\n")
    print()

    return dataset


def euclidean_distance(vector1, vector2):
    """Calculates Euclidean distance for two vectors"""

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


def split_in_folds(data, folds_number):
    """Split uniform datasets to specified number of groups"""

    folds = list()
    data_size = len(data)
    fold_size = data_size // folds_number + 1

    for fold_index in range(folds_number):
        start = fold_index * fold_size
        end = start + fold_size
        folds.append(data[start:end])

    return folds


def flatten(list_of_lists):
    """Flattens a list of lists"""

    return list(chain.from_iterable(list_of_lists))


def cross_validation_sets(folds):
    """Makes sets for cross validation from specified list of groups"""

    sets = list()

    for fold in folds:
        test_set = list(fold)

        train_set = list(folds)
        train_set.remove(fold)
        train_set = flatten(train_set)

        sets.append((train_set, test_set))

    return sets


def cross_validation_split(data, folds_number):
    """Produces sets for crossvalidation from dataset"""

    folds = split_in_folds(data, folds_number)
    sets = cross_validation_sets(folds)

    return sets


def knn(train, test, k):
    """Calcualtes specified number of nearest neighbors"""

    distances = [(row, euclidean_distance(row[:-1], test)) for row in train]
    distances.sort(key=lambda distance: distance[1])

    return distances[0:k]


def predict_class(train, test, k):
    """Predicts class for test data based on it's neighbors"""

    neighbors = knn(train, test, k)
    classes = [neighbor[0][-1] for neighbor in neighbors]

    prediction = Counter(classes).most_common(1)[0][0]

    return prediction


train_set = load_dataset('cats_dataset.csv')
test_object = [27, 51, 3.7]
number_of_neighbors = 20

print(f"Classifying a cat with height, length and weight {test_object}")
print()

predicted_class = predict_class(train_set, test_object, number_of_neighbors)
print(f"Breed prediction for the cat is {predicted_class}")
