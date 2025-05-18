class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t) 
        # This Sort creates New Memory

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Time Complexity - O(n * log n)  
        # Space Complexity -  O(n)



class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False

        count1 = {} 
        count2 = {}   

        for char in s: 
            count1[char]  = 1 + count1.get(char, 0)           
        for char in t: 
            count2[char]  = 1 + count2.get(char , 0) 

        return count1 == count2     
    
    # Time Complexity - O(n)  
    # Space Complexity - O(n)


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False
        
        count = [0] * 26  # Array to count a-z
        for char in range(len(s)):
            count[ord(s[char]) - ord('a' )]  +=  1     
            count[ord(t[char]) - ord('a')]   -=  1       
        for i in count:
            if i != 0 : 
                return False
        else: 
            return True


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # Time Complexity  - O(n)  
    # Space Complexity  - O(1)  
        


   

