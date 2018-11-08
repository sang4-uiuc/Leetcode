class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None # the pointer initially points to nothing
    
class LinkedList:
    def __init__(self, val=None):
        self.head = Node(val)
    
    def insertEnd(self, val):
        n = self.head
        while n.next:
            n = n.next
        n.next = Node(val)
    
    def insertNode(self, node):
        n = self.head
        while n.next:
            n = n.next
        n.next = node

    def traverse(self):
        n = self.head
        while n:
            print(n.val, end = " -> ")
            n = n.next
        print("Null")

    def insert(self, val):
        n = Node(val)
        if self.head == None:
            self.head = n
            return
        n.next = self.head
        self.head = n
    
    # 2.1
    # Remove doplicates from an unsorted list
    def removeDuplicates(self):
        s = set()
        n = self.head
        prev = None
        if n == None:
            return
        while n:
            if n.val in s:
                prev.next = n.next
            else:
                s.add(n.val)
                prev = n
            n = n.next

    # 2.2
    # find kth to last element of a single linked list
    def removeKthToLast(self, k):
        p1 = self.head
        p2 = self.head
        if p1 == None:
            return
        for i in range(k - 1):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        
        n = self.head
        while n.next:
            if n.next == p2:
                n.next = n.next.next
                return
            n = n.next
    
    # 2.6
    # check palindrome linked list
    def checkPalindrome(self):
        l = []
        n = self.head
        if n == None:
            return True
        while n:
            l.append(n.val)
            n = n.next
        return True if l == l[::-1] else False
    
    # 2.8
    # check if circular linked list, if is return node at the beginning of the loop
    def checkCircular(self):
        s = set()
        n = self.head
        if n == None:
            return
        while n:
            if n in s:
                return n, n.val
            else:
                s.add(n)
                n = n.next



    # 2.5
    # sum lists
    # input: (7 -> 1 -> 6) + (5 -> 9 -> 2) is 617 + 295 = 912 (2 -> 1 -> 9)
def sumLists(l1, l2):
    num1 = []
    num2 = []
    p1 = l1.head
    p2 = l2.head
    while p1 and p2:
        num1.append(str(p1.val))
        num2.append(str(p2.val))
        p1 = p1.next
        p2 = p2.next
    n1 = "".join(num1[::-1])
    n2 = "".join(num2[::-1])
    n3 = int(n1) + int(n2)
    num3 = list(str(n3))
    l3 = LinkedList(num3.pop())
    while len(num3) != 0:
        l3.insertEnd(num3.pop())
    return l3
        
                

    # test removeDuplicates and removeKthToLast
# t = LinkedList(1)
# t.insertEnd(2)
# t.insertEnd(3)
# t.insertEnd(4)
# t.insert(5)
# t.insertEnd(2)
# t.insertEnd(1)
# t.insertEnd(5)
# t.insert(5)
# t.insert(1)
# t.removeDuplicates()
# t.traverse()
# t.removeKthToLast(1)
# t.traverse()

    # test sumLists
# l1 = LinkedList(7)
# l1.insertEnd(1)
# l1.insertEnd(6)
# l2 = LinkedList(5)
# l2.insertEnd(9)
# l2.insertEnd(2)
# l3 = sumLists(l1, l2)
# l3.traverse()

    # test checkPalimdrome
# t = LinkedList(1)
# t.insertEnd(2)
# t.insertEnd(1)
# t.traverse()
# print(t.checkPalindrome())

    # test checkCircular
t = LinkedList(1)
t.insertEnd(2)
l = Node(3)
t.insertNode(l)
t.insertEnd(4)
t.insertEnd(5)
t.insertEnd(6)
t.insertNode(l)
print(t.checkCircular())
