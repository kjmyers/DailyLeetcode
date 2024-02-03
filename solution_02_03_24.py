class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = [-1] * len(arr)

        def solve(i):
            if i >= len(arr):
                return 0
            
            if (dp[i] != -1):
                return dp[i]
            
            ret = 0
            curMax = 0

            for l in range(i, min(len(arr), i+k)):
                curMax = max(curMax, arr[l])
                ret = max(ret, curMax * (l - i + 1) + solve(l+1) )
            
            dp[i] = ret
            return ret
        
        return solve(0)
