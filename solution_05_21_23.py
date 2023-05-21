class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        n = len(grid)
        first_x, first_y = -1, -1
        # Find any land cell, and we treat it as a cell of island A.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break

        def dfs(x,y):
            grid[x][y] = 2
            q.append((x,y))
            for cx, cy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= cx < n and 0 <= cy < n and grid[cx][cy] == 1:
                    dfs(cx,cy)
            
        q = []
        dfs(first_x, first_y)
        distance = 0
        while q:
            new_bfs = []
            for x, y in q:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1

            # Once we finish one round without finding land cells of island B, we will
            # start the next round on all water cells that are 1 cell further away from
            # island A and increment the distance by 1.
            q = new_bfs
            distance += 1
