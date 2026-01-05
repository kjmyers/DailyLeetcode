class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ret = 0
        negCount = 0
        minVal = float('inf')

        for r in range(m):
            for c in range(n):
                if matrix[r][c] >= 0:
                    minVal = min(minVal, matrix[r][c])
                    ret += matrix[r][c]
                else:
                    minVal = min(minVal, -matrix[r][c])
                    ret += -matrix[r][c]
                    negCount += 1
        
        if negCount % 2 == 1:
            ret -= 2*minVal

        return ret
