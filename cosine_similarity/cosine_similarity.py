from math import sqrt


def cosine_similarity(x, y):
    """Calculates cosine similarity between vectors"""
    product = sum([x_i * y_i for x_i, y_i in zip(x, y)])
    similarity = product / (norm(x) * norm(y))

    return similarity


def norm(vector):
    """Calculates vector norm"""
    vector_norm = sqrt(sum([element * element for element in vector]))

    return vector_norm


if __name__ == '__main__':
    x = [5, 0, 3, 0, 2, 0, 0, 2, 0, 0]
    y = [3, 0, 2, 0, 1, 1, 0, 1, 0, 1]
    print(cosine_similarity(x, y))
