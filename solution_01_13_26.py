class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        maxy = 0
        total = 0

        # get total area in all squares, highest y
        for x, y, l in squares:
            total += l**2
            maxy = max(maxy, y+l)
        
        # Check for binary search
        def check( limit ):
            area = 0
            for x,y,l in squares:
                if y < limit:
                    area += l * min(limit - y, l)
            return area >= total/2
        
        lo, hi = 0, maxy
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi
