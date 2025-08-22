class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = float('inf')
        bottom = -1
        left = float('inf')
        right = -1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    top = min(top, row)
                    bottom = max(bottom, row)
                    left = min(left, col)
                    right = max(right, col)
        return (bottom - top + 1) * (right - left + 1)
