class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        i = 0
        for num in nums:
            dictionary[num] = i
            i += 1
        for j in range(len(nums)):
            if target - nums[j] in dictionary and j != dictionary[target - nums[j]]:
                return [j, dictionary[target-nums[j]]]
            
        