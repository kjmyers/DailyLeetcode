class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        numIslands = 0
        
        def inRange(row, col):
            if (row < rows and row >= 0
                and col < cols and col >= 0):
                return True
        
        def DFS(row, col):
            if (inRange(row, col) and grid[row][col] == "1"
                and (row,col) not in visited):
                visited.add((row,col))
                directions = [(row+1,col),(row-1,col),
                             (row,col+1),(row,col-1)]
                for r, c in directions:
                    DFS(r,c)
            
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    
                    DFS(row, col)
                    numIslands += 1
        
        return numIslands
