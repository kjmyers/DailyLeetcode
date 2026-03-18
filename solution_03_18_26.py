class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ret = 0

        pf = [ [0] * n for _ in range(m) ]
        for r in range(m):
            for c in range(n):
                pf[r][c] = grid[r][c]
                if r > 0:
                    pf[r][c] += pf[r-1][c]
                if c > 0:
                    pf[r][c] += pf[r][c-1]
                if r > 0 and c > 0:
                    pf[r][c] -= pf[r-1][c-1]
                
                if pf[r][c] <= k:
                    ret += 1
        
        return ret
