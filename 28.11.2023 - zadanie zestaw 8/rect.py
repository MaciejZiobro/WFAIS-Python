from ppoints import Point
from math import sqrt

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        if not (x2>=x1 and y2>=y1):
            raise ValueError("Podane punkty nie są poprawne")

    @classmethod
    def from_points(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        return Rectangle(p1.x, p1.y, p2.x, p2.y)
    @property
    def top(self):
        return self.p2.y
    
    @property
    def bot(self):  
        return self.p1.y
    
    @property
    def left(self):
        return self.p1.x
    
    @property
    def right(self):
        return self.p2.x
    
    @property
    def topleft(self):
        return Point(self.p1.x, self.p2.y)
    
    @property
    def topright(self):
        return self.p2
    
    @property
    def botleft(self):
        return self.p1
    
    @property
    def botright(self):
        return Point(self.p2.x, self.p1.y)
    
    @property
    def width(self):
        return self.p2.x-self.p1.x
    
    @property
    def hight(self):
        return self.p2.y-self.p1.y
    
    @property
    def center(self):
        return Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
    
    @property
    def diagonal_lenght(self):
        return sqrt(self.hight**2 + self.width**2) 
    
    
    def diagonal_angle_sin(self):
        return self.hight()/self.width()
    
    def __str__(self):
        return "["+str(self.p1)+", "+str(self.p2)+"]"

    def __repr__(self): 
        return "Rectangle" + str(self)

    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2: 
            return True
        return False
    
    def __ne__(self, other):
        return not self == other

    def area(self):
        return (self.p2.x-self.p1.x)*(self.p2.y-self.p1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.p1.x+x, self.p1.y+y, self.p2.x+x, self.p2.y+y)
    
    def intersection(self, other):
        try: 
            Rectangle(max(self.p1.x, other.p1.x), max(self.p1.y, other.p1.y), min(self.p2.x, other.p2.x), min(self.p2.y, other.p2.y))
            return Rectangle(max(self.p1.x, other.p1.x), max(self.p1.y, other.p1.y), min(self.p2.x, other.p2.x), min(self.p2.y, other.p2.y))
        except:
            raise ValueError("Rectangles do not intersect")
           
    def cover(self, other):
        return Rectangle(min(self.p1.x, other.p1.x), min(self.p1.y, other.p1.y), max(self.p2.x, other.p2.x), max(self.p2.y, other.p2.y))
    
    def make4(self):
        r1 = Rectangle(self.p1.x, self.p1.y, self.center.x, self.center.y)
        r2 = Rectangle(self.center.x, self.p1.y, self.p2.x, self.center.y)
        r3 = Rectangle(self.p1.x, self.center.y, self.center.x, self.p2.y)
        r4 = Rectangle(self.center.x, self.center.y, self.p2.x, self.p2.y)
        return (r1, r2, r3, r4)

rect1 = Rectangle(0,0,2,2)
print(rect1.bot, rect1.topleft, rect1.hight)

######################################################################
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.zero = Rectangle(0,0,0,0)
        self.r1 = Rectangle(0,0,2,2)
        self.r1m1 = Rectangle(0.0,0.0,1.0,1.0)
        self.r1m2 = Rectangle(1.0,0.0,2.0,1.0)
        self.r1m3 = Rectangle(0.0,1.0,1.0,2.0)
        self.r1m4 = Rectangle(1.0,1.0,2.0,2.0)
        self.r1i = Rectangle(1,1,3,3)
        self.r2 = Rectangle(-2,-2,-1,1)
        self.r11 = Rectangle(0,0,2,2)
        self.r0 = Rectangle(2,2,2,2)
        self.rm = self.r1.move(1,-1)
        
    def test_intersection(self):
        self.assertEqual(self.zero.intersection(self.r1), self.r1.intersection(self.zero))
        self.assertEqual(self.zero.intersection(self.r1), self.zero)
        self.assertEqual(repr(self.r1.intersection(self.r1i)), repr(Rectangle(1,1,2,2)))
        
    def test_cover(self):
        self.assertEqual(self.zero.cover(self.r1), self.r1.cover(self.zero))
        self.assertEqual(self.zero.cover(self.r1), self.r1)
        self.assertEqual(repr(self.r1.cover(self.r1i)), repr(Rectangle(0,0,3,3)))
        
    def test_make4(self):
        self.assertEqual(self.zero.make4(), (self.zero, self.zero, self.zero, self.zero))
        self.assertEqual(self.r1.make4()[0], self.r1m1)
        self.assertEqual(self.r1.make4()[1], self.r1m2)
        self.assertEqual(self.r1.make4()[2], self.r1m3)
        self.assertEqual(self.r1.make4()[3], self.r1m4)
        
    def test_str(self):
        self.assertEqual(str(self.zero),"[(0,0), (0,0)]")
        self.assertEqual(str(self.r1),"[(0,0), (2,2)]")
        self.assertEqual(str(self.r2),"[(-2,-2), (-1,1)]")
        self.assertEqual(str(self.r0), "[(2,2), (2,2)]")

        
    def test_repr(self):
        self.assertEqual(repr(self.zero),"Rectangle[(0,0), (0,0)]")
        self.assertEqual(repr(self.r1),"Rectangle[(0,0), (2,2)]")
        self.assertEqual(repr(self.r2),"Rectangle[(-2,-2), (-1,1)]")
        self.assertEqual(repr(self.r0), "Rectangle[(2,2), (2,2)]")
        
    def test_eq(self):
        self.assertEqual(self.zero == self.zero, True)
        self.assertEqual(self.r1 == self.r1, True)
        self.assertEqual(self.r1 == self.zero, False)
        self.assertEqual(self.r2 == self.r11, False)
        self.assertEqual(self.r0 == self.r0, True)
        self.assertEqual(self.r1 == self.rm, False)
        
    def test_nq(self):
        self.assertEqual(self.zero != self.zero, False)
        self.assertEqual(self.r1 != self.r1, False)
        self.assertEqual(self.r1 != self.zero, True)
        self.assertEqual(self.r2 != self.r11, True)
        self.assertEqual(self.r0 != self.r0, False)
        self.assertEqual(self.r1 != self.r1, not self.r1 == self.r1)
        
    def test_center(self):
        self.assertEqual(self.zero.center, Point(0.0,0.0))
        self.assertEqual(self.r0.center, Point(2.0,2.0))
        self.assertEqual(self.r1.center, Point(1.0,1.0))
        self.assertEqual(self.r2.center,Point(-1.5,-0.5))
        self.assertEqual(self.r11.center, self.r1.center)
        self.assertEqual(self.rm.center,Point(1.0+1,1.0-1))
        
    def test_area(self):
        self.assertEqual(self.zero.area(),0)
        self.assertEqual(self.r1.area(),self.r11.area())
        self.assertEqual(self.r1.area(),4.0)
        self.assertEqual(self.r1.area(), self.rm.area())
        self.assertEqual(self.r2.area(),3.0)
        
    def test_move(self):
        self.assertEqual(self.r1.move(0,0), self.r1)
        self.assertEqual(self.r1.move(2,2).move(-2,-2), self.r1)
        self.assertEqual(self.r1.move(2,2).move(1,1), self.r1.move(3,3))
        self.assertEqual(repr(self.r1.move(2,1)), "Rectangle[(2,1), (4,3)]")
        
        

if __name__ == "__main__":
    unittest.main()
