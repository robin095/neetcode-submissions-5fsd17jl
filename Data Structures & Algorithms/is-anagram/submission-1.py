class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dict = {}
        second_dict = {}

        for char in s:
            if char not in first_dict:
                first_dict[char] = 1
            else:
                first_dict[char] += 1
        
        for char in t:
            if char not in second_dict:
                second_dict[char] = 1
            else:
                second_dict[char] += 1
        
        if first_dict == second_dict:
            return True
        else:
            return False
