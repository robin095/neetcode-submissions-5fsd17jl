class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return (((point[0])**2 + (point[1])**2)**0.5)
        
        def quickSort(points, s, e):
            if e - s + 1 <= 1:
                return points
            
            pivot = points[e]
            left = s
            for i in range(s, e):
                if dist(points[i]) < dist(pivot):
                    temp = points[i]
                    points[i] = points[left]
                    points[left] = temp
                    left += 1
                
            points[e] = points[left]
            points[left] = pivot

            quickSort(points, s, left - 1)
            quickSort(points, left + 1, e)
        
        quickSort(points, 0, len(points)-1)
        return points[:k]

