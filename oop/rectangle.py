from .quadrilateral import Quadrilateral
from .two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __eq__(self, other: object) -> bool:
        self_length_set = set(self.side_lengths())
        cmp_length_set = set(other.side_lengths())
        self_point_set = set(self.x_and_y_of_points())
        cmp_point_set = set(self.x_and_y_of_points())
        return isinstance(other, Rectangle) and self_point_set.__eq__(cmp_point_set) and self_length_set.__eq__(cmp_length_set) and self.center() == other.center() and self.area() == other.area()

    def __str__(self) -> str:
        output = 'Rectangle with vertices:'
        for single_vertice in self.vertices:
            output += '(%g, %g) ' % (single_vertice.x, single_vertice.y)
        output += '; center is (%g, %g) and area is %g' % (self.center().x, self.center().y, self.area())
        output += '\n'
        return output

    def __is_member(self) -> bool:
        """Returns True if the given coordinates form a valid rectangle, and False otherwise."""
        lengths = self.side_lengths()
        length_set = set(lengths)
        return (len(length_set) >= 1) and (len(length_set) <= 2)

    def center(self) -> TwoDPoint:
        """Returns the center of this rectangle, calculated to be the point of intersection of its diagonals."""
        center_x = (self.vertices[0].x + self.vertices[2].x) / 2
        center_y = (self.vertices[0].y + self.vertices[2].y) / 2
        return TwoDPoint(center_x, center_y)

    def area(self) -> float:
        """Returns the area of this rectangle. The implementation invokes the side_lengths() method from the superclass,
        and computes the product of this rectangle's length and width."""
        lengths = self.side_lengths()
        return lengths[0] * lengths[1]
