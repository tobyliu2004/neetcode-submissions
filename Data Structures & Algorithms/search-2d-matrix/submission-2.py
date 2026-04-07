class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[m//(len(matrix[0]))][m%(len(matrix[0]))]:
                r = m - 1
            elif target > matrix[m//(len(matrix[0]))][m%(len(matrix[0]))]:
                l = m + 1
            else:
                return True
        return False
        