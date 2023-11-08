class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        m = max(abs(sx-fx),abs(sy-fy))
        if m == 0 and t == 1:
            return False
        else:
            return m <= t
