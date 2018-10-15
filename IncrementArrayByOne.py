# [1,3,5] -> [1,3,6]
# [9,9,9] -> [1,0,0,0]
import unittest


def incrementArray(n):
    num = int(''.join(str(e) for e in n))
    num += 1
    return [int(x) for x in str(num)]


class IncrementTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(incrementArray([1, 3, 5]), [1, 3, 6])
        self.assertEqual(incrementArray([1]), [2])
        self.assertEqual(incrementArray([9]), [1, 0])
        self.assertEqual(incrementArray([4, 9, 9]), [5, 0, 0])
        self.assertEqual(incrementArray([9, 9, 9]), [1, 0, 0, 0])


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(IncrementTest))
    return test_suite


unittest.TextTestRunner().run(suite())
