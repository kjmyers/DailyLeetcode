class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        ret = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(i,j):
            q = deque([(i,j)])
            seen.add((i,j))
            isClosed = True
            total = 0

            dirs = ((0,1),(1,0),(-1,0),(0,-1))

            while q:
                x,y = q.popleft()
                total += 1
                for d in dirs:
                    r = x + d[0]
                    c = y + d[1]
                    if r < 0 or r >= m or c < 0 or c >= n:
                        isClosed = False
                    elif grid[r][c] == 1 and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))
            if isClosed:
                return total
            else:
                return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in seen:
                    ret += bfs(i,j)
                    print(ret)
                        
                        

        return ret
