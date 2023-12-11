from ..utils import distance

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: "Point", p2: "Point") -> None:
        self.p1 = p1
        self.p2 = p2

    def length(self) -> float:
        """Calculates the length of the line.

        Args:

        Returns:
            float: The length of the line.
        """
        return distance(self.p1, self.p2)
