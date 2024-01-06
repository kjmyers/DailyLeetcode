class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        startTime = [jobs[i][0] for i in range(n)]
        memo={}
        
        def dp(i):
            if i == n:
                return 0
            
            if i in memo: return memo[i]
            
            ans = dp(i + 1) 

            j = bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])
            
            memo[i] = ans
            return ans
        
        return dp(0)
