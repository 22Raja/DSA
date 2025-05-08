# Binary Search Trees (BSTs)

#       5 
#    1      8 
# -1   3  7   9 
class SearchTree:
    def __init__(self,val,  right= None , left= None ):
        self.val =  val 
        self.right = right
        self.right = left

    def __str__(self):
        return str(self.val) 
    
A1 = SearchTree(5)
B1 = SearchTree(1)
C1 = SearchTree(8)
D1 = SearchTree(-1)
E1 = SearchTree(3)
F1 = SearchTree(7)
G1 = SearchTree(9)

A1.left ,A1.right = B1 , C1  
B1.left ,B1.right = D1 , E1
C1.left , C1.right = F1 , G1    



# Binary Search Trees (BSTs) 
# Time: O(log n) , Space: O(log n )     
def Search_bst(node,target): 
    if not node: 
        return False 
    if node.val == target:
        return True
    if target < node.val: 
        return Search_bst(node.left , target)
    else:
        return Search_bst(node.right , target)

print(Search_bst(A1, 4)) 


# Time: O(log n) , Space: O(og n)