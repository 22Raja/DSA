class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        dict_list = defaultdict(list)
        for value in strs:
            dict_list[''.join(sorted(value))].append(value)
        return dict_list.values() 
    # Time Complexity - O(n * k log k )
    # Space Complexity - O(n * k)    


class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        dict_list = defaultdict(list)
        for value in strs:
            values = [0] * 26
            for char in value: 
                values[ord(char) - ord('a')] += 1 
            dict_list[tuple(values)].append(value)  
        return dict_list.values() 
    
    # Time Complexity - O(n * k)
    # Space Complexity - O(n * k)    


        











