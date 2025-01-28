class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        dirs = ((1,0), (0,1), (-1,0), (0,-1))

        def dfs(r,c):
            seen.add((r,c))
            total = grid[r][c]
            for dr,dc in dirs:
                nextR = r+dr
                nextC = c+dc
                if 0 <= nextR < rows and 0 <= nextC < cols and grid[r][c] > 0 and (nextR,nextC) not in seen:
                    total += dfs(nextR,nextC)
            return total

        ret = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r,c) not in seen:
                    ret = max(ret, dfs(r,c))
        
        return ret
