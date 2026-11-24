class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            elif num > res[0]:
                heapq.heappush(res,num)
                heapq.heappop(res)
            else: continue
        
        return heapq.heappop(res)
