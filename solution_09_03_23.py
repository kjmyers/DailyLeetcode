class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cost = [0] * n
        cost[0] = 1
        
        for i in range(m):
            for j in range(1,n):
                cost[j] += cost[j-1]
        return cost[n-1]
