class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        cost = [[-1]*n for _ in range(m)]
        cost[m-1][n-1] = grid[m-1][n-1]

        def dfs(x, y):
            nonlocal n
            nonlocal m
            nonlocal cost

            if x == m or y == n:
                return float('inf')
            elif cost[x][y] != -1:
                return cost[x][y]
            else:
                right, down = dfs(x,y+1), dfs(x+1,y)
                cost[x][y] = min(right, down) + grid[x][y]
            return cost[x][y]

        return dfs(0,0)
