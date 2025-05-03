def hasCycle(self, head):
    current = head 
    value = set() 
    while current:
        if current in value: 
            return True   
        value.add(current)
        current = current.next

    return False

# Time Complexity - O(n) 
# Space Complexity - O(n)


def hasCycle(self, head):
        slow , fast = head , head  
        while slow and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast: 
                return True 
        return False 
# Floyd’s algorithm 
# Time Complexity - O(n) 
# Space Complexity - O(1) 


# https://leetcode.com/problems/linked-list-cycle/