class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            two_prev = 1
            prev = 2
            for i in range(3, n+1):
                two_prev, prev = prev, two_prev + prev
            
            return prev