class Tree: 
    def __init__(self, val , left=None , right= None):
        self.val = val 
        self.right = right 
        self.left = left 


#      1
#    2     3 
#  4  5  10 


A = Tree(1)
B = Tree(2)
c = Tree(3)
D = Tree(4)
E = Tree(5)
F = Tree(10)



A.left = B    # 2
A.right = c   # 3  

B.left = D    # 4 
B.right = E    # 5  

E.left = F  # 10 




# Level Order Traversal (BFS) Time: O(n), Space: O(n)

from collections import deque
level = []
def level_order(node): 
    q = deque()
    q.append(node)
    while q: 
        node = q.popleft() 
        level.append(node.val)
        if node.left: 
            q.append(node.left)
        if node.right: 
            q.append(node.right)



level_order(A)

print(f'Level Order Traversal :- {level}')
