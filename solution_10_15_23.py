class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def solve(ind, st):
            if ind < 0 or ind >= arrLen:
                return 0
            if st == 0:
                if ind == 0:
                    return 1
                return 0
            
            ans = solve(ind, st-1)
            if ind > 0:
                ans = (ans + solve(ind - 1, st - 1)) % MOD
            
            if ind < arrLen - 1:
                ans = (ans + solve(ind + 1, st - 1)) % MOD
            return ans
        
        MOD = 10 ** 9 + 7
        return solve(0,steps)
                