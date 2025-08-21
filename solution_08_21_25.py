class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        res = 0
        row = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    if mat[i][j] != 0:
                        row[i][j] = row[i][j - 1] + 1                        
               
                cur = row[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, row[k][j])
                    if cur == 0:
                        break
                    res += cur
        return res
