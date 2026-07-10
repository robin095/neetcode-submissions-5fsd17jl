class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for _ in s:
            if _ in map1:
                map1[_] += 1
            else: map1[_] = 1
        for _ in t:
            if _ in map2:
                map2[_] += 1
            else: map2[_] = 1
        if map1 == map2:
            return True
        return False
        