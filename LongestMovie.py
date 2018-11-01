import unittest

def longestMovie(flightDuration, movieDuration):
    target = flightDuration - 30
    dic ={}
    for i in range(len(movieDuration)):
        
        if target - movieDuration[i] in dic:
            print([dic[target - movieDuration[i]], i])
            return [dic[target - movieDuration[i]], i]
        else:
            dic[movieDuration[i]] = i



class MovieTest(unittest.TestCase):
    def test_reg(self):
        self.assertEqual(longestMovie(90, [1, 10, 25, 35, 60]), [2, 3])
        self.assertEqual(longestMovie(120, [1, 10, 15, 25, 60, 60, 80, 70, 20]), [1, 6])
        self.assertEqual(longestMovie(60, [1, 10, 20, 30, 40]), [1, 2])
        self.assertEqual(longestMovie(90, [1, 10, 25, 35, 60]), [2, 3])
        self.assertEqual(longestMovie(100, [20, 10, 60, 50]), [1, 2])

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(MovieTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)