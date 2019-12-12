from unittest import TestCase
from .rectangle import Rectangle
from .square import Square
from .sorter import ShapeSorter
from .quadrilateral import Quadrilateral
from .two_d_point import TwoDPoint


class TestSorter(TestCase):

    def test_sorted_with_normal_value_multi_shape(self):
        self.rectangle_one = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.rectangle_two = Rectangle(-1, 2, 3, 2, 3, 0, -1, 0)
        self.square_one = Square(0, 2.1, 2.1, 2.1, 2.1, 0, 0, 0)
        self.square_two = Square(-0.4, 0.4, 0.4, 0.4, 0.4, -0.4, -0.4, -0.4)
        result = ShapeSorter.sort(self.rectangle_one, self.rectangle_two, self.square_one, self.square_two)
        for r in result:
            print(r)
        self.assertTrue(self.rectangle_two == result[0])

    def test_sorted_with_normal_value_single_shape(self):
        self.quadrilateral_one = Quadrilateral(0, 1, 3, 1, 3, 0, 0, -2)
        self.quadrilateral_two = Quadrilateral(0, 1, 3, 1, 5, 0, 0, -2)
        result = ShapeSorter.sort(self.quadrilateral_one, self.quadrilateral_two)
        for r in result:
            print(r)
        self.assertTrue(self.quadrilateral_one == result[0])

    def test_sorted_with_boundary_value_no_attribute(self):
        self.rectangle_one = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.quadrilateral = Quadrilateral(0, 1, 3, 1, 3, 0, 0, -2)
        self.example = TwoDPoint(-5, 2)
        self.assertRaises(AttributeError, ShapeSorter.sort, self.rectangle_one, self.quadrilateral, self.example)

    def test_sorted_with_boundary_value_no_object(self):
        ShapeSorter.sort()
