class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter >= max:
                    max = counter
            else:
                counter = 0
        return max
        