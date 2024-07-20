class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ret = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if rowSum[row] <= colSum[col]:
                    ret[row][col] = rowSum[row]
                else:
                    ret[row][col] = colSum[col]
                rowSum[row] -= ret[row][col]
                colSum[col] -= ret[row][col]
        
        return ret
