# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyNode = ListNode(0)
        current = dummyNode 
        carry = 0 
        while l1 or l2 or carry :
            
            val1 = l1.val if l1 else 0  
            val2 = l2.val if l2 else 0 
            
            # Addition 
            total = val1 + val2 + carry
            # Reminder 
            val = total % 10  
            # quotient
            carry = total // 10 
            current.next = ListNode(val)
           
            # Shift Pointer 
            current = current.next 
            l1 = l1.next if l1 else None   
            l2 = l2.next if l2 else None  

        return dummyNode.next   

        # Time Complexity - 	O(max(l1, l2))
        # Space Complexity - 	O(max(l1, l2)) 

# https://leetcode.com/problems/add-two-numbers/