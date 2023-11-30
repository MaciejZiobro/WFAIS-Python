import pytest
from rect import Rectangle
from ppoints import Point
from math import sqrt


class TestRect:
    @pytest.fixture
    def rectangles(self):
        zero = Rectangle(0, 0, 0, 0)
        r1 = Rectangle(0, 0, 2, 2)
        r1m1 = Rectangle(0.0, 0.0, 1.0, 1.0)
        r1m2 = Rectangle(1.0, 0.0, 2.0, 1.0)
        r1m3 = Rectangle(0.0, 1.0, 1.0, 2.0)
        r1m4 = Rectangle(1.0, 1.0, 2.0, 2.0)
        r1i = Rectangle(1, 1, 3, 3)
        r2 = Rectangle(-2, -2, -1, 1)
        r11 = Rectangle(0, 0, 2, 2)
        r0 = Rectangle(2, 2, 2, 2)
        rm = r1.move(1, -1)
    
        return [zero, r1, r1m1, r1m2, r1m3, r1m4, r1i, r2, r11, r0, rm]
    
    def test_from_points(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero == Rectangle.from_points(Point(0,0), Point(0,0))
        assert r1 == Rectangle.from_points(Point(0,0), Point(2,2))
        
    def test_top(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.top == 0
        assert r1.top == 2
        
    def test_bot(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.bot == 0
        assert r1.bot == 0
        
    def test_left(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.left == 0
        assert r1.left == 0
        
    def test_right(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.right == 0
        assert r1.right == 2
        
    def test_topleft(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.topleft == Point(0,0)
        assert r1.topleft == Point(0,2)
        
    def test_topright(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.topright == Point(0,0)
        assert r1.topright == Point(2,2)
        
    def test_botleft(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.botleft == Point(0,0)
        assert r1.botleft == Point(0,0)
        
    def test_botright(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.botright == Point(0,0)
        assert r1.botright == Point(2,0)
        
    def test_width(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.width == 0
        assert r1.width == 2
        
    def test_hight(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.hight == 0
        assert r1.hight == 2
        
    
    def test_center(self, rectangles):
        zero, r0, r1, r2, r11, rm = rectangles[0], rectangles[9], rectangles[1], rectangles[7], rectangles[8], rectangles[10]
        
        assert zero.center == Point(0.0, 0.0)
        assert r0.center == Point(2.0, 2.0)
        assert r1.center == Point(1.0, 1.0)
        assert r2.center == Point(-1.5, -0.5)
        assert r11.center == r1.center
        assert rm.center == Point(1.0 + 1, 1.0 - 1)
        
    def test_diagonal_lenght(self, rectangles):
        zero, r1 = rectangles[0], rectangles[1]
        
        assert zero.diagonal_lenght == 0
        assert round(r1.diagonal_lenght) == round(2*sqrt(2))
        
    def test_intersection(self, rectangles):
        zero, r1, r1i = rectangles[0], rectangles[1], rectangles[6]
        
        assert zero.intersection(r1) == r1.intersection(zero)
        assert zero.intersection(r1) == zero
        assert repr(r1.intersection(r1i)) == repr(Rectangle(1, 1, 2, 2))

    def test_cover(self, rectangles):
        zero, r1, r1i = rectangles[0], rectangles[1], rectangles[6]
        
        assert zero.cover(r1) == r1.cover(zero)
        assert zero.cover(r1) == r1
        assert repr(r1.cover(r1i)) == repr(Rectangle(0, 0, 3, 3))

    def test_make4(self, rectangles):
        zero, r1, r1m1, r1m2, r1m3, r1m4 = rectangles[0], rectangles[1], rectangles[2], rectangles[3], rectangles[4], rectangles[5]
        
        assert zero.make4() == (zero, zero, zero, zero)
        assert r1.make4()[0] == r1m1
        assert r1.make4()[1] == r1m2
        assert r1.make4()[2] == r1m3
        assert r1.make4()[3] == r1m4

    def test_str(self, rectangles):
        zero, r1, r2, r0 = rectangles[0], rectangles[1], rectangles[7], rectangles[9]
        
        assert str(zero) == "[(0,0), (0,0)]"
        assert str(r1) == "[(0,0), (2,2)]"
        assert str(r2) == "[(-2,-2), (-1,1)]"
        assert str(r0) == "[(2,2), (2,2)]"

    def test_repr(self, rectangles):
        zero, r1, r2, r0 = rectangles[0], rectangles[1], rectangles[7], rectangles[9]
        
        assert repr(zero) == "Rectangle[(0,0), (0,0)]"
        assert repr(r1) == "Rectangle[(0,0), (2,2)]"
        assert repr(r2) == "Rectangle[(-2,-2), (-1,1)]"
        assert repr(r0) == "Rectangle[(2,2), (2,2)]"

    def test_eq(self, rectangles):
        zero, r1, r2, r0, rm = rectangles[0], rectangles[1], rectangles[7], rectangles[9], rectangles[10]
        
        assert zero == zero
        assert r1 == r1
        assert bool(r2 == r0) == False
        assert r0 == r0
        assert bool(r1 == rm) == False

    def test_nq(self, rectangles):
        zero, r1, r2, r0 = rectangles[0], rectangles[1], rectangles[7], rectangles[9]
        
        assert bool(zero != zero) == False
        assert bool(r1 != r1) == False
        assert r1 != zero
        assert r2 != r1

    def test_area(self, rectangles):
        zero, r1, r11, rm, r2 = rectangles[0], rectangles[1], rectangles[8], rectangles[10], rectangles[7]
        
        assert zero.area() == 0
        assert r1.area() == r11.area()
        assert r1.area() == 4.0
        assert r1.area() == rm.area()
        assert r2.area() == 3.0

    def test_move(self, rectangles):
        r1 = rectangles[1]
        
        assert r1.move(0, 0) == r1
        assert r1.move(2, 2).move(-2, -2) == r1
        assert r1.move(2, 2).move(1, 1) == r1.move(3, 3)
        assert repr(r1.move(2, 1)) == "Rectangle[(2,1), (4,3)]"

if __name__ == "__main__":
    pytest.main()