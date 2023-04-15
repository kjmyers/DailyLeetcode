class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for i in range(n + 1)]

        for i in range(1,n+1):
            for coins in range(k+1):
                curSum = 0

                for curCoins in range(min(len(piles[i - 1]), coins) + 1):
                    if curCoins > 0:
                        curSum += piles[i-1][curCoins - 1]
                    dp[i][coins] = max(dp[i][coins], dp[i - 1][coins - curCoins] + curSum)
        
        return dp[n][k]
