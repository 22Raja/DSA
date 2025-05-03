# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # find Middle
        slow , fast = head , head.next
        while fast and fast.next: 
            slow =  slow.next
            fast  = fast.next.next 
        # Reverse second Half 
        current   = slow.next 
        previous = slow.next = None 
        while current: 
            temp = current.next 
            current.next = previous   
            previous = current
            current = temp
        # Merge two Halfs 
        first, second = head , previous    
        while second:
            temp , temp1 = first.next , second.next
            first.next = second 
            second.next = temp
            first ,second = temp , temp1        
    

# Time Complexity - O(n)
# Space Complexity - O(1)

# https://leetcode.com/problems/reorder-list/