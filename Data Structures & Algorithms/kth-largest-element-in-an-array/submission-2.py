class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        heapq.heapify(res)

        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            else:
                heapq.heappush(res,num)
                heapq.heappop(res)
        
        return heapq.heappop(res)
