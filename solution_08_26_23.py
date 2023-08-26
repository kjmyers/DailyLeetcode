class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        memo = [0] * n

        def solve(i):
            if memo[i] != 0:
                return memo[i]
            memo[i] = 1
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    memo[i] = max(memo[i], 1 + solve(j))
            return memo[i]

        ans = 0
        for i in range(n):
            ans = max(ans, solve(i))
        return ans
