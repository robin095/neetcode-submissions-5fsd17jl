class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heap.append([dist, point[0], point[1]])
        heapq.heapify(heap)
        while len(res) < k:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res