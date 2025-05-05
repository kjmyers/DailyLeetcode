class Solution:
    def numTilings(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * (n+1)
        part = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        part[1] = 0
        part[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + 2 * part[i-1]
            part[i] = part[i-1] + dp[i-2]
        
        return dp[-1] % (pow(10,9) + 7)
