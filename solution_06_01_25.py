class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        ret = 0
        for i in range(min(limit+1, n+1)):
            ret += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
            
        
        return ret
