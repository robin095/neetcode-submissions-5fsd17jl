class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        
        for i in range (len(nums)):
            
            sub = target - nums[i]
            if sub in candidates:
                if (i < candidates[sub]):
                    return [i, candidates[sub]]
                else: return [candidates[sub], i]
            else: candidates[nums[i]] = i

                
            

