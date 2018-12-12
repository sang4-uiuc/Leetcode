import unittest

# 1.1
# hash table with value being the count
# Linear time complexity, and linear space complexity
# time and space can be said as constant since it can't go past 128 characters
def isUnique(s):
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
        if dic[c] > 1:
            return False
    return True

# 1.2
# converting both strings to lists and sorting them
# Linear time to lists and checking if equal, Linear space as well
def checkPermutation(s1, s2):
    if len(s1) != len(s1):
        return False
    a = list(s1)
    b = list(s2)
    a.sort()
    b.sort()
    # list(s1).sort() == list(s2).sort() doesn't work?? most likely because sort() doesn't return anything
    # and thus its comparing two Nones
    return True if a == b else False

# 1.3
# O(n^2) time if using strings. String concatenation in python is actually O(n) where they do optimization when it detects
# the same variable name and avoids a copy by resizing the string in place.
# To optimize to O(n) it's easier to just use lists where append is O(1)
def urlify(s):
    res = ""
    for i in s:
        if i == " ":
            res+= "%20"
        else:
            res += i
    return res

# 1.4
# so basically a palindrome(both even length and odd length) cannot have more than 1 character that has an odd count
# knowing this, it's easy to just loop through the string and count the counts
# at the end if there is more than one that is odd return false, else return true
# linear time, linear space
def palindromePermutation(s):
    dic = {}
    count = 0
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    for key, value in dic.items():
        if value %2 ==1:
            count += 1
    if count > 1:
        return False
    return True


# 1.5
def oneAway(s1, s2):
    if len(s1) == len(s2):
        return oneEdit(s1, s2)
    elif len(s1) + 1 == len(s2):
        return oneInsert(s1, s2)
    elif len(s2) + 1 == len(s1):
        return oneInsert(s2, s1)
    else:
        return False

def oneEdit(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def oneInsert(s1, s2):
    i = 0
    j = 0

    while i < len(s1) and i < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


# 1.6
# linear time looping through the string, and constant space
def stringCompression(s):
    count = 1
    output = ''
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            output += s[i] + str(count)
            count = 1
        else:
            count +=1
    output += s[len(s) - 1] + str(count)
    if len(output) < len(s):
        return output
    return s


class ArraysTest(unittest.TestCase):
    def test_isUnique(self):
        self.assertTrue(isUnique("abcdefg"))
        self.assertTrue(isUnique("a"))
        self.assertTrue(isUnique("plmsidox"))
        self.assertTrue(isUnique(""))
        self.assertFalse(isUnique("acbnss"))
        self.assertFalse(isUnique("acbnsa"))
        self.assertFalse(isUnique("uielammsdkflf"))

    def test_checkPermutation(self):
        self.assertTrue(checkPermutation("acbdefg","gfedbca"))
        self.assertTrue(checkPermutation("true","etru"))
        self.assertTrue(checkPermutation("newjersey","jerseynew"))
        self.assertFalse(checkPermutation("asdf", "kjlzvcmx"))
        self.assertFalse(checkPermutation("aa", "ba"))
        self.assertFalse(checkPermutation("illinois", "illinoiss"))
        self.assertFalse(checkPermutation("1234", "1235"))

    def test_urlify(self):
        self.assertEqual(urlify("how are you"), "how%20are%20you")
        self.assertEqual(urlify("Mr John Smith"), "Mr%20John%20Smith")
        self.assertEqual(urlify("i am"), "i%20am")

    def test_palindromePermutation(self):
        self.assertTrue(palindromePermutation("tacocoa"))
        self.assertTrue(palindromePermutation("racecra"))
        self.assertTrue(palindromePermutation("bba"))
        self.assertTrue(palindromePermutation("aabbccccddd"))
        self.assertFalse(palindromePermutation("aabbcccddd"))
        self.assertFalse(palindromePermutation("acsad"))
        self.assertFalse(palindromePermutation("lkasdjlfkasj"))
        self.assertFalse(palindromePermutation("racecarr"))
    
    def test_oneAway(self):
        self.assertEqual(oneAway("bale", "pale"), True)
        self.assertEqual(oneAway("bale", "ble"), True)
        self.assertEqual(oneAway("ba", "pa"), True)
        self.assertEqual(oneAway("balettt", "pale"), False)
        self.assertEqual(oneAway("bale", "bdme"), False)
        self.assertEqual(oneAway("bale", "pal"), False)
        self.assertEqual(oneAway("bal", "bale"), True)

    def test_stringCompression(self):
        self.assertEqual(stringCompression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(stringCompression("nnnmmmlll"), "n3m3l3")
        self.assertEqual(stringCompression("bbttbbbbyyt"), "b2t2b4y2t1")
        self.assertEqual(stringCompression("aabbccdd"), "aabbccdd")
        self.assertEqual(stringCompression("ab"), "ab")
        
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ArraysTest))
    return test_suite

suite = suite()
unittest.TextTestRunner().run(suite)

            