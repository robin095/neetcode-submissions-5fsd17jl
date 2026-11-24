class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first_stone = heapq.heappop_max(stones)
            second_stone = heapq.heappop_max(stones)
            resulting_stone = first_stone - second_stone
            if resulting_stone != 0:
                heapq.heappush_max(stones, resulting_stone)
        
        if len(stones) == 0:
            return 0
        else: return stones[0]
