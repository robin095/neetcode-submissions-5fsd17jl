class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point: List[int]) -> int:
            distance = (point[0])**2 + (point[1])**2
            return distance
        
        def sort(arr, s, e):

            if e <= s:
                return

            pivot = arr[e]
            l = s

            for i in range (s, e):
                if dist(arr[i]) < dist(arr[e]):
                    temp = arr[i]
                    arr[i] = arr[l]
                    arr[l] = temp
                    l += 1

            arr[e] = arr[l]
            arr[l] = pivot

            sort(arr, s, l - 1)
            sort(arr, l + 1, e)
        
        sort(points, 0, len(points) - 1)

        return points[:k]
