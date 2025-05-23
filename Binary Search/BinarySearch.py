# Binary Search 
class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l = 0 
        r = n - 1
        while l <= r:
            mid = l + ((r-l) // 2 )
            if nums[mid] > target:
                r = mid -1 
            elif nums[mid] < target: 
                l = mid +1

            else:
                return mid  
        return -1   

        # Time Complexity - O(log n)   We search Half the Iteration 
        # Space Complexity - O(1) 

 # https://leetcode.com/problems/binary-search/ 
