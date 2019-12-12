from unittest import TestCase
from .square import Square


class TestSquare(TestCase):

    def test_snap_with_ordinary_square(self):
        self.square_one = Square(0, 2.1, 2.1, 2.1, 2.1, 0, 0, 0)
        self.shape_one = self.square_one.snap()
        self.assertEqual(self.shape_one.smallest_x(), 0)
        self.assertEqual(self.shape_one.side_lengths(), (2.0, 2.0, 2.0, 2.0))

    def test_snap_with_special_square(self):
        self.square_two = Square(-0.4, 0.4, 0.4, 0.4, 0.4, -0.4, -0.4, -0.4)
        self.shape_two = self.square_two
        self.assertEqual(self.shape_two.side_lengths(), (0.8, 0.8, 0.8, 0.8))

    def test_is_member_with_right_value(self):
        self.square_one = Square(0, 2.1, 2.1, 2.1, 2.1, 0, 0, 0)
        print(self.square_one.__str__().__contains__("Square"))

    def test_is_member_with_wrong_value(self):
        self.assertRaises(TypeError, Square, 0, 1, 3, 1, 3, 0, 0, 0)

    def test_equal(self):
        self.square_one = Square(0, 2.1, 2.1, 2.1, 2.1, 0, 0, 0)
        self.square_two = Square(2.1, 2.1, 2.1, 0, 0, 0, 0, 2.1)
        self.assertTrue(self.square_one == self.square_two)

    def test_str(self):
        self.square_one = Square(0, 2.1, 2.1, 2.1, 2.1, 0, 0, 0)
        print(self.square_one)
        self.assertTrue(self.square_one.__str__().__contains__('Square with vertices:(0, 2.1) (2.1, 2.1) (2.1, 0) (0, 0)'))