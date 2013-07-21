import unittest
import aufg76

class test76(unittest.TestCase):
    
    def test_99(self):
        self.assertEqual(1, aufg76.getCount(100, 99))
        
    def test_98(self):
        self.assertEqual(2, aufg76.getCount(100, 98))
        
    def test_97(self):
        self.assertEqual(3, aufg76.getCount(100, 97))
        
    def test_96(self):
        #4
        #3+1
        #2+2
        #2+1+1
        #1+1+1+1
        self.assertEqual(5, aufg76.getCount(100, 96))

    def test_100 (self):
        number = aufg76.getNumber(100)
        print number
        self.assertTrue(number > 100)      


if __name__ == '__main__':
    unittest.main()

