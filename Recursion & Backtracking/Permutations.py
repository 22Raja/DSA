class Solution(object):
    def permute(self, nums):
        n = len(nums)
        res  , sol  = [] , [ ]  
        def backtrack():
            if n == len(sol): 
                res.append(sol[:])
                return 

            for x in nums: 
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop() 
        backtrack()
        return res 
    

    

# Time complexity - O(n!)
# Space complexity - O(n)


# https://leetcode.com/problems/permutations/
