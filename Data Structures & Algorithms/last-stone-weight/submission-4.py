class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heap.append(-stones[i])
            
        heapq.heapify(heap)
        while len(heap) > 1:
            stone_1 = heapq.heappop(heap)
            stone_2 = heapq.heappop(heap)
            sub = stone_1 - stone_2
            if sub != 0:
                heapq.heappush(heap, -abs(sub))
        heapq.heappush(heap, 0)
        return abs(heap[0])
        
      
