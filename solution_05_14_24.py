class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ret = 0

        def backtrack(i,j):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == 0:
                return 0

            max_gold = 0
            original_val = grid[i][j]
            grid[i][j] = 0

            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                max_gold = max(max_gold, backtrack(i+di, j+dj))
            grid[i][j] = original_val
            return max_gold + original_val

        for row in range(m):
            for col in range(n):
                ret = max(ret, backtrack(row, col))
        return ret
