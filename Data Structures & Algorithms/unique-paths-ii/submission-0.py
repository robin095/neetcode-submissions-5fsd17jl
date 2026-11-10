class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        row = [0] * n
        i = 0

        while i < n and grid[0][i] == 0:
            row[i] = 1
            i += 1

        for p in range(1, m):
            for q in range(0, n):
                if q == 0:
                    if row[q] == 0 or grid[p][q] == 1:
                        row[q] = 0
                elif grid[p][q] == 1:
                    row[q] = 0
                else: row[q] = row[q] + row[q-1]

        return row[n-1]        

        