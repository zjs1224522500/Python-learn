import math
from typing import List


class TwoDPoint:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TwoDPoint) and self.x == other.x and self.y == other.y  # TODO

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '(%g, %g)' % (self.__x, self.__y)

    # TODO: add magic methods such that two TwoDPoint objects can be added and subtracted coordinate-wise just by using
    #  syntax of the form p + q or p - q
    def __add__(self, other: object) -> object:
        return TwoDPoint(self.x + object.x, self.y + object.y)

    def __sub__(self, other: object) -> object:
        return TwoDPoint(self.x - object.x, self.y - object.y)

    # Construct the TwoDPoint with coordinates
    @staticmethod
    def from_coordinates(coordinates: List[float]):
        if len(coordinates) % 2 != 0:
            raise Exception("Odd number of floats given to build a list of 2-d points")
        points = []
        it = iter(coordinates)
        for x in it:
            points.append(TwoDPoint(x, next(it)))
        return points

    # Get length of the line with two coordinates
    @staticmethod
    def get_length_from_coordinates(c1, c2):
        x_diff = c1.x - c2.x
        y_diff = c1.y - c2.y
        return math.sqrt((x_diff**2) + (y_diff**2))
