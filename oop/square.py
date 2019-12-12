from .rectangle import Rectangle
from .quadrilateral import Quadrilateral
from .two_d_point import TwoDPoint


class Square(Rectangle):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def __is_member(self) -> bool:
        """Returns True if the given coordinates form a valid square, and False otherwise."""
        lengths = self.side_lengths()
        length_set = set(lengths)
        return len(length_set) == 1

    def __eq__(self, other: object) -> bool:
        self_length_set = self.side_lengths()
        cmp_length_set = other.side_lengths()
        self_point_set = self.x_and_y_of_points()
        cmp_point_set = other.x_and_y_of_points()
        return isinstance(other, Square) and self_length_set.__eq__(cmp_length_set) and self.center() == other.center() and self.area() == other.area()

    def __str__(self) -> str:
        output = 'Square with vertices:'
        for single_vertice in self.vertices:
            output += '(%g, %g) ' % (single_vertice.x, single_vertice.y)
        output += '; center is (%g, %g) and area is %g' % (self.center().x, self.center().y, self.area())
        output += '\n'
        return output

    def snap(self) -> Quadrilateral:
        """Snaps the sides of the square such that each corner (x,y) is modified to be a corner (x',y') where x' is the
        integer value closest to x and y' is the integer value closest to y. This, of course, may change the shape to a
        general quadrilateral, hence the return type. The only exception is when the square is positioned in a way where
        this approximation will lead it to vanish into a single point. In that case, a call to snap() will not modify
        this square in any way."""
        new_vertices = []
        for single in self.vertices:
            new_vertices.append(TwoDPoint(round(single.x), round(single.y)))

        if (new_vertices[0].x == new_vertices[1].x and new_vertices[1].x == new_vertices[2].x and new_vertices[2].x == \
                new_vertices[3].x and new_vertices[0].y == new_vertices[1].y and new_vertices[1].y == new_vertices[
                    2].y and new_vertices[2].y == new_vertices[3].y):
            return self
        else:
            return Quadrilateral(new_vertices[0].x, new_vertices[0].y, new_vertices[1].x, new_vertices[1].y,
                                 new_vertices[2].x, new_vertices[2].y, new_vertices[3].x, new_vertices[3].y)
