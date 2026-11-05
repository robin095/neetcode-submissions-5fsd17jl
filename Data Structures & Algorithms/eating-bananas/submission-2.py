class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        slowest, fastest = 1, max(piles)

        while slowest <= fastest: 
            mid_speed = (slowest + fastest) // 2


            if self.time_taken(piles, mid_speed) <= h:
                working_speed = mid_speed
                fastest = mid_speed - 1
            elif self.time_taken(piles, mid_speed) > h:
                slowest = mid_speed + 1
            
        
        return working_speed
        
        

    def time_taken(self, piles, speed):
        hours = 0
        for pile in piles: 
            if pile % speed == 0:
                hours += (pile // speed)
            else: hours += (pile // speed) + 1
        
        return hours





