class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def valid(val):
            if val == 0:
                return False
            remaining = n
            for q in quantities:
                remaining -= int(math.ceil(q/val))
            if remaining < 0:
                return False
            else:
                return True
        
        def bsearch(lo, hi):
            while lo < hi:
                mid = lo + (hi - lo)//2
                if valid(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        

        return bsearch(0, max(quantities))
