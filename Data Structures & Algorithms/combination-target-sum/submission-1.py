class Solution:
    def combinationSum(self, nums: List[int], t: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(t, i):
            if t < 0 or i >= len(nums):
                return
            if t == 0:
                res.append(subset.copy())
                return
            t -= nums[i]
            subset.append(nums[i])
            dfs(t,i)
            t += nums[i]
            subset.pop()
            dfs(t, i+1)
            
        dfs(t, 0)
        return res