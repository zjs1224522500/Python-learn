from unittest import TestCase
from .quadrilateral import Quadrilateral


class TestQuadrilateral(TestCase):

    def test_side_lengths(self):
        self.quadrilateral_one = Quadrilateral(0, 2, 2, 2, 2, 0, 0, 0)
        print(self.quadrilateral_one.side_lengths())
        self.assertEqual(self.quadrilateral_one.side_lengths(), (2.0, 2.0, 2.0, 2.0))
        self.quadrilateral_two = Quadrilateral(0, 3, 4, 3, 4, 0, 0, 0)
        self.assertEqual(self.quadrilateral_two.side_lengths(), (4.0, 3.0, 4.0, 3.0))

    def test_smallest_x(self):
        self.quadrilateral_one = Quadrilateral(0, 2, 2, 2, 2, 0, 0, 0)
        print('Smallest x coordinate: ', self.quadrilateral_one.smallest_x())
        self.assertEqual(self.quadrilateral_one.smallest_x(), 0.0)
        self.quadrilateral_two = Quadrilateral(-3, 2, 4, 1.5, 6.3, 0, 2.0, -1)
        self.assertEqual(self.quadrilateral_two.smallest_x(), -3)

    def test_equal(self):
        self.quadrilateral_one = Quadrilateral(0, 2, 2, 2, 2, 0, 0, 0)
        self.quadrilateral_two = Quadrilateral(2, 2, 2, 0, 0, 0, 0, 2)
        self.assertTrue(self.quadrilateral_one == self.quadrilateral_two)

    def test_str(self):
        self.quadrilateral_one = Quadrilateral(0, 2, 2, 2, 2, 0, 0, 0)
        print(self.quadrilateral_one)
        self.assertTrue(self.quadrilateral_one.__str__().__contains__('Quadrilateral with vertices:(0, 2) (2, 2) (2, 0) (0, 0)'))