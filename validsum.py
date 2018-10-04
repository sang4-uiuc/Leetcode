import unittest

def validsum(s):
    close = [')', '}', ']']
    stack = []
    for p in s:
        if p in close:
            if not stack:
                return False    
            stack.pop()
            
        else:
            stack.append(p)
    if not stack:
        return True
    return False

# print(validsum("()"))
class MyTest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(validsum("()"))
        self.assertTrue(validsum("({})"))
        self.assertTrue(validsum("[](){[]()}"))
    def testFalse(self):
        self.assertFalse(validsum(")("))
        self.assertFalse(validsum(")"))
        self.assertFalse(validsum("("))
        self.assertFalse(validsum("]["))
if __name__ == '__main__':
    unittest.main()