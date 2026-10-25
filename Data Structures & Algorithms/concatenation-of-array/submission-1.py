class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans = ans + [nums[i]]
        return ans