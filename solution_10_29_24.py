class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for col in range(n-2,-1,-1):
            for row in range(m):
                if grid[row][col] < grid[row][col+1]:
                    dp[row][col] = 1 + dp[row][col+1]
                if row - 1 >= 0 and grid[row][col] < grid[row-1][col+1]:
                    dp[row][col] = max(dp[row][col], 1 + dp[row-1][col+1])
                if row + 1 < m and grid[row][col] < grid[row+1][col+1]:
                    dp[row][col] = max(dp[row][col], 1 + dp[row+1][col+1])
        
        ret = 0
        for i in range(m):
            ret = max(ret,dp[i][0])


        return ret
