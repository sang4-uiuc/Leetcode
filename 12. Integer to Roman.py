import unittest

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        letters = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        output = ""
        for val, let in zip(values, letters):
            n = num//val
            output += n*let
            num = num%val
        return output


class SolutionTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(Solution.intToRoman(self, 10), "X")
        self.assertEqual(Solution.intToRoman(self, 1001), "MI")
        self.assertEqual(Solution.intToRoman(self, 40), "XL")
        self.assertEqual(Solution.intToRoman(self, 8), "VIII")
        # self.assertEqual(Solution.intToRoman(self, 10), "X")
    
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SolutionTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)