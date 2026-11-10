class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs = [0] + costs
        
        @cache
        def func(i):
            if i > n:
                return inf
            if i == n:
                return costs[n]

            return costs[i] + min(func(i+1) + 1, func(i+2) + 4, func(i+3) + 9)
        
        return func(0)
