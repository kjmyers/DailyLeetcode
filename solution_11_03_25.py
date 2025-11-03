class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        cur = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] != colors[i-1]:
                cur = 0
            
            total += min(cur, neededTime[i])
            cur = max(cur, neededTime[i])
        
        return total
