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

# Recursive In order Traversal (DFS) Time: O(n) , Space O(n)
In = []
Post = []
Pre = []

def in_order(node): 
    if not node: 
        return
     
    in_order(node.left)
    In.append(node.val)
    in_order(node.right)

in_order(A)
print(f"In Order Traversal {In} ", end ='\n'  )

# Recursive Pre order Traversal (DFS) Time: O(n) , Space O(n)
def pre_order(node):
    if not node: 
        return 
    Pre.append(node.val)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)
print(f"Pre Order Traversal {Pre}", end ='\n'  )



# Recursive Post order Traversal (DFS) Time: O(n) , Space O(n)
def post_order(node):   
    if not node: 
        return 
   
    post_order(node.left)
    post_order(node.right)
    Post.append(node.val)

post_order(A)
print(f"Post Order Traversal {Post} ", end ='\n'  )
