class NetworkNode:
    def __init__(self, numOfCalls):
        self.value = numOfCalls
        self.children = []


    def insert(self, NetworkNode):
        self.children.append(NetworkNode)

    def traverse(self):
        node = self # start from the head node
        if len(node.children) == 0:
            print(node.value)

def largestSectionalLoad(root):
    dic = {}
    findNumberofChild(root, dic)
    maxnode = None
    maxval = 0
    for key, value in dic.items():
        if value[0]/value[1] > maxval:
            maxval = value[0]/value[1]
            maxnode = key
    
    return maxnode

def findNumberofChild(root, dic):
    if len(root.children) == 0:
        return [root.value, 1]
        
    else:
        py = [root.value, 1]
        for child in root.children:
            py = [sum(x) for x in zip(py, findNumberofChild(child, dic))]
        dic[root] = py
        return dic[root]
    

i = NetworkNode(20)
j = NetworkNode(12)
i.insert(j)
k = NetworkNode(18)
k.insert(NetworkNode(15))
k.insert(NetworkNode(8))
i.insert(k)
j.insert(NetworkNode(11))
j.insert(NetworkNode(2))
j.insert(NetworkNode(3))

print(largestSectionalLoad(i))