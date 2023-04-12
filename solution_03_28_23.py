from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)

        @lru_cache(None)
        def dfs(day):

            if day > 365:
                return 0
            
            elif day in dayset:
                return min( dfs(day+1) + costs[0], dfs(day+7) + costs[1], dfs(day+30) + costs[2])
            
            else:
                return dfs(day+1)
        
        return dfs(1)
