# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(str(l1.val))
            l1 = l1.next
            
        while l2:
            stack2.append(str(l2.val))
            l2 =l2.next
    
        n1 = int(''.join(stack1[::-1])) 
        n2 = int(''.join(stack2[::-1]))
        
        num = str(n1 + n2)[::-1]
        if len(num) == 0:
            return 0
        
        head = None
        curr = None
        for c in num:
            if head == None:
                head = ListNode(c)
                curr = head
            else:
                curr.next = ListNode(c)
                curr = curr.next
        return head