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
c = Tree(3)
D = Tree(4)
E = Tree(5)
F = Tree(10)



A.left = B    # 2
A.right = c   # 3  

B.left = D    # 4 
B.right = E    # 5  

E.left = F  # 10 




def in_order(node): 
    if not node: 
        return
     
    in_order(node.left)
    print(node.val)
    in_order(node.right)


in_order(A)

def pre_order(node):
    if not node: 
        return 
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)


def post_order(node):   
    if not node: 
        return 
   
    post_order(node.left)
    post_order(node.right)
    print(node.val)


post_order(A)


