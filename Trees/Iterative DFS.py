class Tree: 
    def __init__(self, val , left=None , right= None):
        self.val = val 
        self.right = right 
        self.left = left 

    def __str__(self): 
        return str(self.val) 

#      1
#    2     3 
#  4  5  10 


A = Tree(1)
B = Tree(2)
C = Tree(3)
D = Tree(4)
E = Tree(5)
F = Tree(10)


A.left = B    # 2
A.right = C   # 3  

B.left = D    # 4 
B.right = E    # 5  

C.left = F  # 10 

# Iterative Pre order Traversal (DFS) Time: O(n) , Space O(n)

def pre_order_iterative(node):
    stk = [node]
    while stk:
        none = stk.pop() 
        if node.right:
            stk.append(node.right)

        if node.left:
            stk.append(node.left)
        print(none)


pre_order_iterative(A)


# Iterative Post order Traversal (DFS) Time: O(n) , Space O(n)

def post_order_iterative(node):
    stk = [node]
    while stk:
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)
        none = stk.pop() 
        print(none)

post_order_iterative(A)

# Iterative In order Traversal (DFS) Time: O(n) , Space O(n)


def In_order_iterative(node):
    stk = [node]
    while stk:
        if node.left:
            stk.append(node.left)
        none = stk.pop() 
        if node.right:
            stk.append(node.right)
        print(none)

In_order_iterative(A)





# Check if Value Exists (DFS) Time: O(n)