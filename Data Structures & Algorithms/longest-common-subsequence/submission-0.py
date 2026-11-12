class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(len(text2) + 1):
            for j in range(len(text1) + 1):
                if i == 0:
                    grid[i][j] = 0
                elif j == 0:
                    grid[i][j] = 0
                elif text1[j-1] == text2[i-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
        