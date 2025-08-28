class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        for startRow in range(n):
            curRow = []
            for col in range(n - startRow):
                curRow.append(grid[startRow+col][col])
            curRow.sort(reverse=True)
            for col in range(n - startRow):
                grid[startRow+col][col] = curRow[col]
        
        for startCol in range(1, n):
            curRow = []
            for row in range(n - startCol):
                curRow.append(grid[row][startCol+row])
            curRow.sort()
            for row in range(n - startCol):
                grid[row][startCol+row] = curRow[row]
        
        return grid
