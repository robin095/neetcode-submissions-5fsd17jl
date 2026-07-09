class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num)
        heapq.heapify(heap)
        i = 0
        for i in range (len(heap) - k):
            res = heapq.heappop(heap)
            
        return heap[0]