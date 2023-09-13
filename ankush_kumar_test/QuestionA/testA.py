import unittest
from overlap import overlap

# We test overlap with TestOverlap.
# We have five tests for checking overlap and five for do not overlap.

class TestOverlap(unittest.TestCase):
    def test1(self):
        result = overlap(1, 3, 2, 4)
        self.assertEqual(result, "overlap") 

    def test2(self):
        result = overlap(2, 4, 1, 3)
        self.assertEqual(result, "overlap")

    def test3(self):
        result = overlap(1, 4, 2, 3)
        self.assertEqual(result, "overlap")
        
    def test4(self):
        result = overlap(2, 3, 1, 4)
        self.assertEqual(result, "overlap")

    def test5(self):
        result = overlap(1, 2, 1, 4)
        self.assertEqual(result, "overlap")

    def test6(self):
        result = overlap(1, 2, 3, 4)
        self.assertEqual(result, "do not overlap") 

    def test7(self):
        result = overlap(3, 4, 1, 2)
        self.assertEqual(result, "do not overlap") 
    
    def test8(self):
        result = overlap(1, 2, 2, 3)
        self.assertEqual(result, "do not overlap") 
    
    def test9(self):
        result = overlap(2, 3, 1, 2)
        self.assertEqual(result, "do not overlap") 
    
    def test10(self):
        result = overlap(2, 4, 1, 2)
        self.assertEqual(result, "do not overlap") 
    

if __name__ == '__main__':
    unittest.main()

