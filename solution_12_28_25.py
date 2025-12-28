class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        start = 0
        ret = 0
        lo = 0

        for i in range(m-1, -1, -1):

            hi = len(grid[i])

            while lo < hi:
                mid = (lo+hi)//2
                if 0 > grid[i][mid]:
                    hi = mid
                else:
                    lo = mid+1
            ret += n - lo
        
        return ret