class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        v_tot = [0] * cols
        h_tot = [0] * rows
        total = 0

        for r in range(rows):
            for c in range(cols):
                total += grid[r][c]
                v_tot[c] += grid[r][c]
                h_tot[r] += grid[r][c]
        if total % 2 == 1:
            return False
        total = total//2

        curTot = 0
        for num in v_tot:
            curTot += num
            if curTot == total:
                return True
        curTot = 0
        for num in h_tot:
            curTot += num
            if curTot == total:
                return True
        
        return False
