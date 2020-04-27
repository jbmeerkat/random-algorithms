from math import sqrt
from functools import reduce


class Point:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        coords = ', '.join(map(str, self.coordinates))

        return f"Point ({coords})"

    def distance_to(self, point):
        if len(self.coordinates) != len(point.coordinates):
            raise ValueError('Points must have the same number of dimensions.')

        coords_by_dimension = zip(self.coordinates, point.coordinates)
        distance = sqrt(
            sum(
                map(lambda p: pow((p[0] - p[1]), 2), coords_by_dimension)
            )
        )

        return distance


print("One dimensional points:")
p1 = Point(1)
p2 = Point(3)
distance = p1.distance_to(p2)
print(f"Distance between {p1} and {p2} is {distance}")


print("\n")
print("Multi dimensional points:")
p1 = Point(1, 2, 3, 4)
p2 = Point(5, 6, 7, 8)
distance = p1.distance_to(p2)
print(f"Distance between {p1} and {p2} is {distance}")
