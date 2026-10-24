class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i==len(nums)-1:
                nums[i]=-1
                return nums
            max=nums[i+1]
            for j in range(i+1, len(nums)):
                if nums[j]>max:
                    max=nums[j]
            nums[i]=max
