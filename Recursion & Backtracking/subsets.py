class Solution(object):
    def subsets(self, nums):
        N = len(nums) 
        res , sol = [] , [] 

        def backtrack(i): 
            # Base case 
            if i == N:
                res.append(sol[:])
                return
            
            # If we don't pick nums[i]
            backtrack(i + 1)
            
            # Pick nums[i] 
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop() 

        backtrack(0)
        return res  



# Time complexity - O(2 ^ n)
# Space complexity - O(n)


# https://leetcode.com/problems/subsets/
