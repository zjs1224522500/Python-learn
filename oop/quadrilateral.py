from .two_d_point import TwoDPoint
from typing import Tuple


class Quadrilateral:

    def __init__(self, *floats: float):
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])

    @property
    def vertices(self):
        return self.__vertices

    def __eq__(self, other: object) -> bool:
        self_length_set = set(self.side_lengths())
        cmp_length_set = set(other.side_lengths())
        self_point_set = set(self.x_and_y_of_points())
        cmp_point_set = set(other.x_and_y_of_points())
        return isinstance(other, Quadrilateral) and self_length_set.__eq__(cmp_length_set) and self.smallest_x() == \
               other.smallest_x() and self_point_set.__eq__(cmp_point_set)

    def __str__(self) -> str:
        output = 'Quadrilateral with vertices:'
        for single_vertice in self.vertices:
            output += '(%g, %g) ' % (single_vertice.x, single_vertice.y)
        output += '\n'
        return output

    def side_lengths(self) -> Tuple:
        """Returns a tuple of four floats, each denoting the length of a side of this quadrilateral. The value must be
        ordered clockwise, starting from the top left corner."""
        first_length = TwoDPoint.get_length_from_coordinates(self.vertices[0], self.vertices[1])
        second_length = TwoDPoint.get_length_from_coordinates(self.vertices[1], self.vertices[2])
        third_length = TwoDPoint.get_length_from_coordinates(self.vertices[2], self.vertices[3])
        forth_length = TwoDPoint.get_length_from_coordinates(self.vertices[3], self.vertices[0])
        return first_length, second_length, third_length, forth_length

    def smallest_x(self) -> float:
        """Returns the x-coordinate of the vertex with the smallest x-value of the four vertices of this
        quadrilateral."""
        return min(self.vertices[0].x, self.vertices[1].x, self.vertices[2].x, self.vertices[3].x)

    def x_and_y_of_points(self) -> set:
        result = []
        for single in self.__vertices:
            single_point = str(single.x) + "-" + str(single.y)
            result.append(single_point)
        return set(result)

