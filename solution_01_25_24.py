class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for j in range(2)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i%2][j] = dp[(i-1)%2][j-1] + 1
                else:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])
        
        return dp[(m)%2][n]
