from .quadrilateral import Quadrilateral


class ShapeSorter:

    @staticmethod
    def sort(*args: Quadrilateral) -> list:
        return sorted(args, key=lambda shape: shape.smallest_x())

