from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        l, r = 1, max_rate
        result = max_rate

        while l <= r:
            mid = (l + r) // 2
            total_hours = 0
            for i in piles: total_hours += ceil(i / mid)
            if total_hours <=h:
                r = mid - 1
                result = mid 
            else: l = mid + 1
        return result
            