class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        memo = {}
        
        def dp(d, targ):
            if d == 0:
                return 0 if targ > 0 else 1
            if (d, targ) in memo:
                return memo[(d, targ)]
            
            ret = 0
            
            for i in range(max(0, targ-k), targ):
                ret += dp(d-1, i)
            
            memo[(d, targ)] = ret
            return ret
        
        return dp(n, target) % (10**9 + 7)
