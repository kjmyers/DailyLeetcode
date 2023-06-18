class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10 ** 9 + 7
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            answer = 1

            # Check its four neighbor cells, if a neighbor cell grid[prevI][prevJ] has a
            # smaller value, we move to this cell and solve the subproblem: dfs(prevI, prevJ).
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    answer += dfs(prev_i, prev_j) % mod
            
            dp[i][j] = answer
            return answer
        
        # Iterate over all cells grid[i][j] and sum over dfs(i, j).
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
