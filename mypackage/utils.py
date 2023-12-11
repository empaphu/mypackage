import math

def distance(p1: "Point", p2: "Point") -> float:
    """Calculates the distance between two points.

    Args:
        p1 (Point): The first point.
        p2 (Point): The second point.

    Returns:
        float: The distance between the two points.
    """
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
