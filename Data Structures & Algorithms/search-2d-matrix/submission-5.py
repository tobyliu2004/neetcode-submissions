class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0])-1

        while l <= r:
            m = (l + r) // 2
            row = m // (len(matrix[0]))
            col = m % (len(matrix[0]))
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False