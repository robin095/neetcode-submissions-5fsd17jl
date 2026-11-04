class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, t, i = 0, len(nums) - 1, 0

        while i < len(nums):
            if i > t:
                break

            elif nums[i] == 0:
                temp = nums[z]
                nums[z] = 0
                nums[i] = temp
                z += 1
                i += 1

            elif nums[i] == 2:
                temp = nums[t]
                nums[t] = 2
                nums[i] = temp
                t -= 1
            
            else:
                i += 1


