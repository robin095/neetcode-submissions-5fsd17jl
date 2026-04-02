class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) //2
            if target < matrix[mid][0]: r = mid - 1
            elif target > matrix[mid][-1]: l = mid + 1
            elif matrix[mid][0] <= target <=  matrix[mid][-1]: 
                row_l, row_r = 0, len(matrix[mid]) - 1
                while row_l <= row_r:
                    row_mid = (row_l + row_r)//2
                    if target < matrix[mid][row_mid]: row_r = row_mid - 1
                    elif target > matrix[mid][row_mid]: row_l = row_mid + 1
                    else: return True
                return False
            else: return False
        return False
        