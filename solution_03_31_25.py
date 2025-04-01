class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        #ret = 0

        memo = {}

        n = len(questions)

        def solve(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            ans = questions[i][0] + solve(i + questions[i][1] + 1)

            skip = solve(i+1)

            memo[i] = max(ans, skip)

            return memo[i]
        
        return solve(0)
