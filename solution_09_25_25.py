class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        d = {}
        def dp(r,c):
            if (r,c) in d:
                return d[r,c]
            ret = triangle[r][c]
            if r < n-1:
                minPath = float('inf')
                for newc in range(c, c+2):
                    if 0 <= newc <= r+1:
                        minPath = min(minPath, dp(r+1, newc))
                ret += minPath
            d[r,c] = ret
            return d[r,c]
        
        return dp(0,0)
