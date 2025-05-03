# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# With Dummy Node.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode(0,head)
        slow = dummyNode
        fast = head   
        # Move fast pointer n steps ahead
        while n > 0 and fast:
            fast = fast.next 
            n -= 1 
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next 
        # Remove the nth node from the end

        slow.next = slow.next.next

        return dummyNode.next 
    
# Time complexity - O(n)
# space complexity - O(1)


# Without Dummy Node.
 def removeNthFromEnd(self, head, n):
        if not head: 
            return None 
        length = 0 
        current = head 
        while current: 
            length += 1 
            current = current.next
        # Removing the first node when n th is equal length

        if n == length:
            start_node = head.next
            head.next = None 
            return start_node 
        #Find the node before the one to delete
        before_node = head  
        for _ in range(length-n-1): 
            before_node = before_node.next

        # Remove the nth node from the end
        delete_node = before_node.next 
        Another_node = delete_node.next 
        before_node.next = Another_node

        return head
     
#Time Complexity: O(n)
#Space Complexity: O(1)

#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
