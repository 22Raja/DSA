def reverseList(self, head):
        current = head 
        previous = None
        while current: 
            temp = current.next  
            current.next = previous  
            previous = current
            current = temp
        return previous


# Time Complexity - O(n) 
# Space Complexity - O(1)
# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/