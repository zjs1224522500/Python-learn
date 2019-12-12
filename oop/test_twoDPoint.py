from .two_d_point import TwoDPoint
from unittest import TestCase


class TestTwoDPoint(TestCase):

    def test_from_coordinates(self):
        self.c1 = TwoDPoint.from_coordinates([0, 2]).pop()
        self.vertices = TwoDPoint.from_coordinates([0, 2, 2, 2])
        self.assertEqual(self.c1.x, 0)
        self.assertEqual(self.c1.y, 2)
        self.assertTrue(self.c1 == TwoDPoint(0, 2))
        self.assertTrue(self.vertices[0] == TwoDPoint(0, 2))
        self.assertTrue(self.vertices[1] == TwoDPoint(2, 2))

    def test_get_length_from_coordinates(self):
        self.c1 = TwoDPoint.from_coordinates([0, 2]).pop()
        self.c2 = TwoDPoint.from_coordinates([2, 2]).pop()
        print(TwoDPoint.get_length_from_coordinates(self.c1, self.c2))
        self.assertEqual(TwoDPoint.get_length_from_coordinates(self.c1, self.c2), 2)
