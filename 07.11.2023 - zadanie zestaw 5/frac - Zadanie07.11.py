from math import lcm, gcd

def add_frac(frac1, frac2):
    return [frac1[0]*frac2[1]+frac1[1]*frac2[0],frac1[1]*frac2[1]]
    
def sub_frac(frac1, frac2):
    return [frac1[0]*frac2[1]-frac1[1]*frac2[0],frac1[1]*frac2[1]]

def mul_frac(frac1, frac2):
    return [frac1[0]*frac2[0],frac1[1]*frac2[1]]

def div_frac(frac1, frac2):
    return mul_frac(frac1, [frac2[1], frac2[0]])

def is_positive(frac):
    if frac[0]*frac[1]>0:
        return True
    return False

def is_zero(frac):
    if frac[0] == 0:
        return True
    return False

def extend_cmm(frac1, frac2):
    m = lcm(frac1[1],frac2[1])
    return [frac1[0]*m/frac1[1], m], [frac2[0]*m/frac2[1], m]

def simplify(frac):
    return [frac[0]/gcd(frac[0],frac[1]), frac[1]/gcd(frac[0],frac[1])]

def cmp_frac(frac1, frac2):
    if extend_cmm(frac1, frac2)[0][0]>extend_cmm(frac1, frac2)[1][0]:
        return 1
    if extend_cmm(frac1, frac2)[0][0]<extend_cmm(frac1, frac2)[1][0]:
        return -1
    else:
        return 0

def frac2float(frac):
    return float(frac[0]/frac[1])


##############################

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.one = [1,1]
        self.frac1 = [3,5]
        self.frac1e = [12,20]
        self.frac1p = [-3,5]
        self.frac1o = [5,3]
        self.frac2 = [1,2]
        self.frac2e = [4,8]
        self.fracinf = [1,3]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.frac1, self.zero), self.frac1)
        self.assertEqual(add_frac(self.frac1, self.frac2), [11,10])
        self.assertEqual(add_frac(self.zero, self.zero), self.zero)
        self.assertEqual(add_frac(self.zero, self.frac1), self.frac1)
        self.assertEqual(simplify(add_frac(self.frac1e, self.frac2e)), simplify(add_frac(self.frac1, self.frac2)))
        self.assertEqual(is_zero(add_frac(self.frac1, self.frac1p)), True)
        self.assertEqual(add_frac(self.frac2, self.frac1p), sub_frac(self.frac2, self.frac1))

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.frac1, self.zero), self.frac1)
        self.assertEqual(sub_frac(self.frac1, self.frac2), [1,10])
        self.assertEqual(sub_frac(self.zero, self.zero), self.zero)
        self.assertEqual(sub_frac(self.zero, self.frac1), [-self.frac1[0], self.frac1[1]])
        self.assertEqual(simplify(sub_frac(self.frac1e, self.frac2e)), simplify(sub_frac(self.frac1, self.frac2)))
        self.assertEqual(is_zero(sub_frac(self.frac1, self.frac1)), True)
        self.assertEqual(sub_frac(self.frac2, self.frac1p), add_frac(self.frac2, self.frac1))

    def test_mul_frac(self):
        self.assertEqual(is_zero(mul_frac(self.frac1, self.zero)), True)
        self.assertEqual(mul_frac(self.frac1, self.frac2), [3,10])
        self.assertEqual(mul_frac(self.zero, self.zero), self.zero)
        self.assertEqual(is_zero(mul_frac(self.zero, self.frac1)), True)
        self.assertEqual(simplify(mul_frac(self.frac1e, self.frac2e)), simplify(mul_frac(self.frac1, self.frac2)))
        self.assertEqual(simplify(mul_frac(self.frac1, self.frac1o)), self.one)
        self.assertEqual(mul_frac(self.frac2, self.frac1o), div_frac(self.frac2, self.frac1))

    def test_div_frac(self):
        self.assertEqual(div_frac(self.frac1, self.frac2), [6,5])
        self.assertEqual(is_zero(div_frac(self.zero, self.frac1)), True)
        self.assertEqual(simplify(div_frac(self.frac1e, self.frac2e)), simplify(div_frac(self.frac1, self.frac2)))
        self.assertEqual(simplify(div_frac(self.frac1, self.frac1)), self.one)
        self.assertEqual(div_frac(self.frac2, self.frac1o), mul_frac(self.frac2, self.frac1))

    def test_is_positive(self):
        self.assertEqual(is_positive(self.zero), False)
        self.assertEqual(is_positive(self.frac1), True)
        self.assertEqual(is_positive(self.frac1p), False)

    def test_is_zero(self):
        self.assertEqual(is_zero(self.zero), True)
        self.assertEqual(is_zero(self.frac1), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.frac1, self.zero), 1)
        self.assertEqual(cmp_frac(self.zero, self.frac1), -1)
        self.assertEqual(cmp_frac(self.frac1, self.frac1p), 1)
        self.assertEqual(cmp_frac(self.frac1, self.frac1e), 0)
        self.assertEqual(cmp_frac(self.zero, self.zero), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.zero), 0.0)
        self.assertEqual(frac2float(self.frac1), 0.6)
        self.assertEqual(round(frac2float(self.fracinf), 3), round(0.33333, 3))
        
    def test_extend_cmm(self):
        self.assertEqual(extend_cmm(self.frac1, self.frac1e), (self.frac1e, self.frac1e))
        self.assertEqual(extend_cmm(self.frac1e, self.frac1e), extend_cmm(self.frac1, self.frac1e))
        self.assertEqual(extend_cmm(self.zero, self.frac1e), extend_cmm(self.zero, self.frac1e))
        
    def test_simplify(self):
        self.assertEqual(simplify(self.zero), self.zero)
        self.assertEqual(simplify(self.frac1e), self.frac1)
        self.assertEqual(simplify(self.frac1), self.frac1)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
    
