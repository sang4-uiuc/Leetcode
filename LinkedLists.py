class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self # start from the head node
        while node != None:
            print(node.val) # access the node value
            node = node.next # move on to the next node
    
    # with hash table/easier version
    def deleteDup(self):
        node = self
        previous = Node
        check = set()
        while node != None:
            if node.val in check:
                # print(node.val)
                previous.next = node.next
            else:
                check.add(node.val)
                previous.next = node
            node = node.next
        return node
node1 = Node(12) 
node2 = Node(99) 
node3 = Node(37) 
node4 = Node(37)
node5 = Node(89)
node6 = Node(50)
node7 = Node(29)
node8 = Node(48)
node9 = Node(30)

node1.next = node2 # 12->99
node2.next = node3 # 99->37
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9


# node1.traverse()
print(node1.deleteDup())
# node1.traverse()