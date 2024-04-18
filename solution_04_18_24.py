class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(ii,jj):
            if not (0 <= ii < len(grid)) or not (0 <= jj < len(grid[0])) or grid[ii][jj] == 0:
                return 1
            
            seen.add((ii,jj))

            ret = 0
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                if (ii+di, jj+dj) not in seen:
                    ret += dfs(ii+di, jj+dj)
            
            return ret


        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
