import unittest
import aufg31

class test31(unittest.TestCase):

    def test_megativeAmount(self):
        self.failUnlessRaises(Exception, aufg31.getCoins, -100);
    
    def test_onePence(self):
        self.assertEqual(1, aufg31.getCoins(1))
        
    def test_twoPence(self):
        self.assertEqual(2, aufg31.getCoins(2))
        
    def test_fourPence(self):
        self.assertEqual(3, aufg31.getCoins(4))
        
    def test_fivePence(self):
        self.assertEqual(4, aufg31.getCoins(5))
    
    def test_sixPence(self):
        self.assertEqual(5, aufg31.getCoins(6))
    
    def test_sevenPence(self):
        self.assertEqual(6, aufg31.getCoins(7))
        
    def test_tenPence(self):
        #1x10
        #2x5
        #1x5, 2x2, 1x1
        #1x5, 1x2, 3x1
        #1x5, 5x1
        #5x2
        #4x2, 2x1
        #3
        #2
        #1
        #0
        self.assertEqual(11, aufg31.getCoins(10))
  
    def test_twohundredPence(self):
        print aufg31.getCoins(200)
        #self.assertTrue(aufg31.getCoins(200)> 10)
        self.assertEqual(73682, aufg31.getCoins(200));
if __name__ == '__main__':
    unittest.main()

