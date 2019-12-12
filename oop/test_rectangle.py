from .rectangle import Rectangle
from unittest import TestCase
from .two_d_point import TwoDPoint


class TestRectangle(TestCase):

    def test_center(self):
        self.example = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.assertTrue(self.example.center() == TwoDPoint(1.5, 0.5))

    def test_area(self):
        self.example = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.assertEqual(self.example.area(), 3)

    def test_is_member_with_right_value(self):
        self.example = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.assertTrue(self.example.__str__().__contains__("Rectangle"))

    def test_is_member_with_wrong_value(self):
        self.assertRaises(TypeError, Rectangle, 0, 1, 2, 1, 3, 0, 0, 0)

    def test_equal(self):
        self.example_one = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        self.example_two = Rectangle(3, 1, 3, 0, 0, 0, 0, 1)
        self.assertTrue(self.example_one == self.example_two)

    def test_str(self):
        self.example = Rectangle(0, 1, 3, 1, 3, 0, 0, 0)
        print(self.example)
        self.assertTrue(self.example.__str__().__contains__('Rectangle with vertices:(0, 1) (3, 1) (3, 0) (0, 0)'))

