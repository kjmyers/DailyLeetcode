class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ret = 0

        pf = [ [[0,0] for _ in range(n)] for _ in range(m) ]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "X":
                    pf[r][c][0] += 1
                elif grid[r][c] == "Y":
                    pf[r][c][1] += 1
                
                if r > 0:
                    pf[r][c][0] += pf[r-1][c][0]
                    pf[r][c][1] += pf[r-1][c][1]
                if c > 0:
                    pf[r][c][0] += pf[r][c-1][0]
                    pf[r][c][1] += pf[r][c-1][1]
                if r > 0 and c > 0:
                    pf[r][c][0] -= pf[r-1][c-1][0]
                    pf[r][c][1] -= pf[r-1][c-1][1]
                
                if pf[r][c][0] > 0 and pf[r][c][0] == pf[r][c][1]:
                    ret += 1
        
        return ret
