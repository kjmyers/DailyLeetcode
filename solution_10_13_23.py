class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        oneBack = 0
        twoBack = 0
        
        for i in range(len(cost)):
            cur = cost[i] + min(oneBack, twoBack)
            twoBack = oneBack
            oneBack = cur
        return min(oneBack, twoBack)
