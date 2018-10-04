import unittest

def findMaxSum(nums):

    if nums == [] or nums is None:
        return 0
    elif len(nums) < 3:
        return nums
    else:
        nums = sorted(nums)
        print(nums[len(nums): len(nums) - 2: -1])
        return sum(nums[len(nums): len(nums) - 4: -1])




class IntegerArithmeticTestCase(unittest.TestCase):
    def testMaxSum(self):  # test method names begin with 'test'
        self.assertEqual(findMaxSum([-1,-9,9,4,5,19,6]), 34)
        self.assertEqual(findMaxSum([0,4,2,200,26,4]), 230)
        self.assertEqual(findMaxSum([]), 0)
        self.assertEqual(findMaxSum([1,2]), [1,2])
    

if __name__ == '__main__':
    unittest.main()