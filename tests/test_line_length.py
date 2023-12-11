from mypackage.geometry import Line, Point



def test_line_length():
    line_lengt = 4.0
    p1_x = 1.0
    p2_x = p1_x + line_lengt
    test_line = Line(Point(p1_x,0.0), Point(p2_x, 0.0))
    assert test_line.length() == line_lengt
