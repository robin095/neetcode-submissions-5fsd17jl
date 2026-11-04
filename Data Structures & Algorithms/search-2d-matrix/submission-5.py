class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][len(matrix[0]) - 1]:
                l = m + 1
            elif target >= matrix[m][0] and target <= matrix[m][len(matrix[0]) - 1]:
                row_left, row_right = 0, len(matrix[0]) - 1
                while row_left <= row_right:
                    row_middle = (row_left + row_right) // 2
                    if target > matrix[m][row_middle]:
                        row_left = row_middle + 1
                    elif target < matrix[m][row_middle]:
                        row_right = row_middle - 1
                    else: return True
                return False
        return False


        