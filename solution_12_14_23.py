class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        rowOnes = [0] * n
        colOnes = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
        
        ret = [ [0] * m for _ in range(n) ]

        print(rowOnes)
        print(colOnes)
        
        for i in range(n):
            for j in range(m):
                ret[i][j] = rowOnes[i] + colOnes[j] - (n - rowOnes[i]) - (m - colOnes[j])
        
        return ret
