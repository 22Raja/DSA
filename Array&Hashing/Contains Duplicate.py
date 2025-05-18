class Solution(object):
    def containsDuplicate(self, nums):

        
        values = set() 
        for x in nums:
            if x in values:
                return True 
            else:
                values.add(x)
        else: 
            return False
            
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Time Complexity - O(n)
        # Space Complexity - O(n) 
        

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Time Complexity - O(n log n )
        # Space Complexity - O(1) 

        