import unittest

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # if len(s) != len(t):
    #     return False
    # s = sorted([i for i in s])
    # t = sorted([i for i in t])
    # print(s)
    # print(t)
    # for i in range(len(s)):
    #     if s[i] == t[i]:
    #         return True
    #     else:
    #         return False
    if len(s) != len(t):
        return False
    s = sorted([i for i in s])
    t = sorted([i for i in t])
    print(s)
    print(t)
    if s == t:
        return True
    else:
        return False
print(isAnagram("a", "b"))
# class AnagramTestCase(unittest.TestCase):
#     def testMaxSum(self):  # test method names begin with 'test'
#         self.assertEqual("ab", "ba")
#         self.assertEqual("anagram", "margana")
#         self.assertEqual("run", "urn")
        
    

# if __name__ == '__main__':
#     unittest.main()