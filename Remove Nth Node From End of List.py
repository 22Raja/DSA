# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode(0,head)
        l = dummyNode
        r = head   

        while n > 0 and  r :
            r = r.next 
            n -= 1 
        while r:
            l = l.next
            r = r.next 

        l.next = l.next.next

        return dummyNode.next 
    
# Time complexity - O(n)
# space complexity - O(1)



#https://leetcode.com/problems/remove-nth-node-from-end-of-list/