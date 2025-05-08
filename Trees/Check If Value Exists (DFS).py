class Tree: 
    def __init__(self, val , left=None , right= None):
        self.val = val 
        self.right = right 
        self.left = left 

    def __str__(self): 
        return str(self.val) 

#      1
#    2   3 
#  4  5  10 


A = Tree(1)
B = Tree(2)
C = Tree(3)
D = Tree(4)
E = Tree(5)
F = Tree(10)


A.left = B
A.right = C 
B.left = D 
B.right = E  
C.left = F


# Check If Value Exists (DFS) 
# TIME: O(n) , SPACE: O(n)
def Search(node, target):
    if not node: 
        return False 
    if node.val == target: 
        return True
    return Search(node.left, target) or Search(node.right, target)

print(Search(A,  5))  
    