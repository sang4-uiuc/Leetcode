import unittest


class IdManager(object):
    def __init__(self, n):
        self.count = n
        self.ids = set(range(1, n+1))
        
    def get_id(self):
        try:
            return self.ids.pop()
        except KeyError:
            raise Exception("no available Ids")
    
    def free_id(self, n):
        if n > self.count:
            raise Exception("id out of range)")
        self.ids.add(n)
        
class TestIdManager(unittest.TestCase):
    def setUp(self):
        self.manager = IdManager(100)
    
    def test_get_id(self):
        length = len(self.manager.ids)
        random = self.manager.get_id()
        self.assertEqual(len(self.manager.ids), length - 1)
        
    def test_free_id(self):
        random = self.manager.get_id()
        length = len(self.manager.ids)
        self.manager.free_id(random)
        self.assertEqual(len(self.manager.ids), length + 1)

    def test_invalid_value(self):
        self.assertRaises(Exception, lambda: IdManager(1.4))

    def test_free_free(self):

        
        self.assertRaises(Exception, lambda: self.manager.free_id(101))
if __name__ == '__main__':
    unittest.main()
# a = IdManager(1)
# b = a.get_id()
# c = a.get_id()
# a.free_id(b)
