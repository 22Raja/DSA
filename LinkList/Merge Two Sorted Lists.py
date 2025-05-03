# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        d = ListNode()
        c = d
        while list1 and list2 : 
            if list1.val < list2.val: 
                c.next = list1  
                c = list1 
                list1 = list1.next

            else: 
                c.next = list2 
                c = list2 
                list2 = list2.next 
        
        c.next = list1 if list1 else list2 
             
        
        return d.next  
        
# Time Complexity - O(List1 + List2).  
# Space Complexity - O(1) Only for Dummy Node.  
# https://leetcode.com/problems/merge-two-sorted-lists/description/