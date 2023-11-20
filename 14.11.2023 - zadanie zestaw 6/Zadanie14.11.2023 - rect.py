from ppoints import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        return "["+str(self.p1)+", "+str(self.p2)+"]"

    def __repr__(self): 
        return "Rectangle" + str(self)

    def __eq__(self, other):
        if str(self) == str(other): return True
        return False
    
    def __ne__(self, other):
        return not self == other

    def center(self): # zwraca środek prostokąta
        return Point((self.x1+self.x2)/2, (self.y1+self.y2)/2)

    def area(self):
        return (self.x2-self.x1)*(self.y2-self.y1)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.x1+x, self.y1+y, self.x2+x, self.y2+y)
# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.zero = Rectangle(0,0,0,0)
        self.r1 = Rectangle(0,0,2,2)
        self.r2 = Rectangle(-2,-2,-1,1)
        self.r11 = Rectangle(0,0,2,2)
        self.r0 = Rectangle(2,2,2,2)
        self.rm = self.r1.move(1,-1)
        
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
        self.assertEqual(self.zero.center(), Point(0.0,0.0))
        self.assertEqual(self.r0.center(), Point(2.0,2.0))
        self.assertEqual(self.r1.center(), Point(1.0,1.0))
        self.assertEqual(self.r2.center(),Point(-1.5,-0.5))
        self.assertEqual(self.r11.center(), self.r1.center())
        self.assertEqual(self.rm.center(),Point(1.0+1,1.0-1))
        
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

