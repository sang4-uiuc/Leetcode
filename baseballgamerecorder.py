import unittest

def gameRecorder(l):
    vl = []
    for i in range(len(l)):
        if l[i] == 'C':
            del vl[-1]
        elif l[i] == 'D':
            vl.append(vl[-1] * 2)
        elif l[i] == '+':
            vl.append(vl[-1] + vl[-2])
        else:
            vl.append(int(l[i]))
    return sum(vl)



class IntegerArithmeticTestCase(unittest.TestCase):
    def testMaxSum(self):  # test method names begin with 'test'
        self.assertEqual(gameRecorder(["5", "2", "C", "D", "+"]), 30)
        self.assertEqual(gameRecorder(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)
        self.assertEqual(gameRecorder(["4", "D", "+", "8", "C"]), 24)
        
    

if __name__ == '__main__':
    unittest.main()