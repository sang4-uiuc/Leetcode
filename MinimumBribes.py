# Sample Input

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# Sample Output

# 3
# Too chaotic
import unittest

def minimumBribes(q):
    count = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            return "Too chaotic"
            
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                count += 1
    return count


class BribeTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(minimumBribes([2,1,5,3,4]), 3)
        self.assertEqual(minimumBribes([2,5,1,3,4]), "Too chaotic")

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(BribeTest))
    return test_suite

mySuit=suite()
runner=unittest.TextTestRunner()
runner.run(mySuit)