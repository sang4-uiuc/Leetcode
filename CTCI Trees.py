# Python program to for tree traversals 

# A class that represents an individual node in a 
# Binary Tree 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


# A function to do inorder tree traversal 
def printInorder(root): 

	if root: 

		# First recur on left child 
		printInorder(root.left) 

		# then print the val of node 
		print(root.val)

		# now recur on right child 
		printInorder(root.right) 



# A function to do postorder tree traversal 
def printPostorder(root): 

	if root: 

		# First recur on left child 
		printPostorder(root.left) 

		# the recur on right child 
		printPostorder(root.right) 

		# now print the val of node 
		print(root.val)


# A function to do preorder tree traversal 
def printPreorder(root): 

	if root: 

		# First print the val of node 
		print(root.val), 

		# Then recur on left child 
		printPreorder(root.left) 

		# Finally recur on right child 
		printPreorder(root.right) 


# Driver code 
# root = Node(1) 
# root.left	 = Node(2) 
# root.right	 = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 
# print("Preorder traversal of binary tree is")
# printPreorder(root) 

# print("\nInorder traversal of binary tree is")
# printInorder(root) 

# print("\nPostorder traversal of binary tree is")
# printPostorder(root) 

def rightViewUtil(root, level, max_level, res): 
      
    # Base Case 
    if root is None: 
        return
      
    # If this is the last node of its level 
    if (max_level[0] < level): 
        res.append(root.val)
        max_level[0] = level 
  
    # Recur for right subtree first, then left subtree 
    rightViewUtil(root.left, level+1, max_level, res) 
    rightViewUtil(root.right, level+1, max_level, res) 
    
  
def rightView(root): 
    max_level = [0] 
    res= []
    rightViewUtil(root, 1, max_level, res) 
    print(res)
    return res.pop()
  

# 4.2

# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
  
print(rightView(root))