class Solution(object):
    def isPalindrome(self, s):
        new_char = []
        for ch in s: 
            if ch.isalnum():
                new_char.append(ch.lower())
        return new_char == new_char[::-1]  

        """
        :type s: str
        :rtype: bool
        """
    # Time Complexity -  O(n)
    # Space Complexity - O(n)


class Solution(object):
    def isPalindrome(self, s):
        l , r = 0 , len(s) - 1 
        while l < r : 
            while l < r and not self.alphanum(s[l]):  
                l +=1 

            while r > l and not self.alphanum(s[r]):  
                r -= 1 
            if s[l].lower() != s[r].lower(): 
                return False 
            l += 1 
            r -= 1
        return True  

    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
         ord('0') <= ord(c) <=  ord('9')  or  
        ord('a') <= ord(c) <= ord('z')) 



        """
        :type s: str
        :rtype: bool
        """
     # Time Complexity - O(n)
    # Space Complexity - O(1)
        