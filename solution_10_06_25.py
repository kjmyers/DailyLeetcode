class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        h = []
        highest = 0
        nr = len(grid)
        nc = len(grid[0])

        heappush(h, (grid[0][0],0,0))
        seen = set()
        seen.add((0,0))

        while h:
            cur_height, row, col = heappop(h)
            highest = max(highest, cur_height)
            if (row,col) == (nr-1,nc-1):
                return highest
            seen.add((row,col))
            
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= nr or new_col < 0 or new_col >= nc:
                    continue
                if (new_row, new_col) in seen:
                    continue
                
                heappush(h, (grid[new_row][new_col],new_row,new_col))
        
        return highest
