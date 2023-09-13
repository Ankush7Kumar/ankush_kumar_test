import unittest
from compare import compare

# We test compare with TestCompare.

# 2 tests for checking equal
# 3 tests for checking greater
# 3 tests for checking lesser


class TestCompare(unittest.TestCase):
    def test1(self):
        result = compare("1.2.3","1.2.3")
        self.assertEqual(result, "equal")
        
    def test2(self):
        result = compare("4","4")
        self.assertEqual(result, "equal")
        
    def test3(self):
        result = compare("1.2.3","1.2.2")
        self.assertEqual(result, "greater")
 
    def test4(self):
        result = compare("4.1","3.4.5.6.7.8.9")
        self.assertEqual(result, "greater")
    
    def test5(self):
        result = compare("6","5.9.9.9.9.9")
        self.assertEqual(result, "greater")
    
    def test6(self):
        result = compare("1.2.2","1.2.3")
        self.assertEqual(result, "lesser")
        
    def test7(self):
        result = compare("3.4.5.6.7.8.9","4.1")
        self.assertEqual(result, "lesser")
        
    def test8(self):
        result = compare("5.9.9.9.9.9","6")
        self.assertEqual(result, "lesser")
        
           

if __name__ == '__main__':
    unittest.main()


