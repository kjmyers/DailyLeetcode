class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        q = deque()
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q.append((0,0,1))
        seen = set()

        while q:
            curRow, curCol, curDist = q.popleft()
            if curRow == n-1 and curCol == n-1:
                return curDist
            for addRow, addCol in ((-1,0),(0,1),(1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)):
                newRow = curRow + addRow
                newCol = curCol + addCol
                
                if (0 <= newRow < n and 
                    0 <= newCol < n and 
                    grid[newRow][newCol] == 0 and 
                    (newRow,newCol) not in seen):
                    
                    seen.add((newRow,newCol))
                    q.append((newRow, newCol, curDist+1))


        return -1
