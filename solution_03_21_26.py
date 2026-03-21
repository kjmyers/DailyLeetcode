class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        upper_x = x
        lower_x = x+k-1
        
        while upper_x < lower_x:
            for cur_y in range(y,y+k):
                # Swap top and bottom elements
                tmp = grid[upper_x][cur_y]
                grid[upper_x][cur_y] = grid[lower_x][cur_y]
                grid[lower_x][cur_y] = tmp
            upper_x += 1
            lower_x -= 1
        
        return grid
