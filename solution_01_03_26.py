class Solution:
    def numOfWays(self, n: int) -> int:
        color3 = 6
        color2 = 6
        MOD = (10**9) + 7
        for i in range(2, n+1):
            temp = color3
            color3 = (2*color3 + 2 * color2) % MOD
            color2 = (2*temp + 3 * color2) % MOD
        
        return (color3+color2) % MOD
