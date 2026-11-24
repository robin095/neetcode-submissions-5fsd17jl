class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [x * -1 for x in nums]
        heapq.heapify(neg_nums)
        i = 0
        while i < k:
            res = heapq.heappop(neg_nums)
            i += 1
        return -res
        