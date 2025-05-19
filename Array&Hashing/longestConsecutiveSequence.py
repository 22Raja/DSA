class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current_streak = 1
        for n in range(1, len(nums)): 
            # Too Avoid Duplicates  
            if nums[n] == nums[n-1]:
                continue
            if nums[n] == nums[n-1] + 1 :
                current_streak +=1 
            else:
               longest =  max(longest, current_streak)
               current_streak = 1

        return max(longest, current_streak)
    #Time Complexity -  O(n log n) 
    #Space Complexity - O(1)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in numSet:
            # Check if it's the start of a sequence
            if (n - 1) not in numSet: 
                length = 0 
                while (n + length) in numSet:
                    length += 1 
                longest = max(length, longest)

        return longest
   #Time Complexity -  O(n) 
   #Space Complexity - O(n)
