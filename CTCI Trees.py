class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val)
		printInorder(root.right) 

def printPostorder(root): 

	if root: 
		printPostorder(root.left) 
		printPostorder(root.right) 
		print(root.val)

def printPreorder(root): 
	if root: 
		print(root.val), 
		printPreorder(root.left) 
		printPreorder(root.right) 



def rightViewUtil(root, level, max_level, res): 
    if root is None: 
        return
    if (max_level[0] < level): 
        res.append(root.val)
        max_level[0] = level 

    rightViewUtil(root.left, level+1, max_level, res) 
    rightViewUtil(root.right, level+1, max_level, res) 
    
  
def rightView(root): 
    max_level = [0] 
    res= []
    rightViewUtil(root, 1, max_level, res) 
    print(res)
    return res.pop()
  

# 4.2
# time complexity is linear
def createMinimalBST(l):
	return createMinimalBSTHelper(l, 0, len(l) -1)

def createMinimalBSTHelper(l, start, end):
	if end < start:
		return None
	mid = (start + end) // 2
	n = Node(l[mid])
	n.left = createMinimalBSTHelper(l, start, mid - 1)
	n.right = createMinimalBSTHelper(l, mid + 1, end)
	return n

def printLevelOrder(root): 
    if root is None: 
        return
      
    queue = [] 
    queue.append(root) 
  
    while(len(queue) > 0): 
        print(queue[0].val)
        node = queue.pop(0) 
  
        if node.left is not None: 
            queue.append(node.left) 
  
        if node.right is not None: 
            queue.append(node.right) 


# 4.4 check if binary tree is balanced
def isBalanced(root):
	if checkHeight(root) == -1:
		return False
	else:
		return True

def checkHeight(root):
	if root == None:
		return 0
	leftHeight = checkHeight(root.left)
	rightHeight = checkHeight(root.right)
	if leftHeight == -1:
		return -1
	if rightHeight == -1:
		return -1

	heightDiff = abs(leftHeight - rightHeight)
	if heightDiff > 1:
		return -1
	else:
		return max(leftHeight, rightHeight) + 1

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.left.right.right = Node(9) 
  
# print(rightView(root))
print(isBalanced(root))
# arr = [1, 2, 3, 4, 5, 6, 7] 
# root = createMinimalBST(arr)
# printPreorder(root)
# printLevelOrder(root)