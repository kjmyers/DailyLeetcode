class Solution:
    def knightDialer(self, n: int) -> int:
        d = {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
            0: [4,6]
        }
        MOD = 10**9 + 7
        #ret = (ret+1) % MOD

        @cache
        def solve(num, remain):
            if remain == 1:
                return 1
            
            ret = 0
            for nxt in d[num]:
                ret = (ret+solve(nxt,remain-1)) % MOD
            return ret

        ans = 0
        for i in range(10):
            ans += solve(i,n)
        
        return ans % MOD
