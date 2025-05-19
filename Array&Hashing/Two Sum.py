class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n): 
            for x in range(i+1, n): 
                if nums[i] + nums[x] == target:
                    return [i ,x]     

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    # Time Complexity  -  O(n^2)
    # Space Complexity -  O(1) 



class Solution(object):
    def twoSum(self, nums, target):
        prevMap = { }
        for i, n in enumerate(nums):
            val =  target - n
            if val in prevMap: 
                return [prevMap[val] , i ]
            prevMap[n] = i    
            
        return 

 

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    # Time Complexity  -  O(n)
    # Space Complexity -  O(n) 
        

