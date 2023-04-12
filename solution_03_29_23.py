class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        maxSat = 0
        suffix = 0

        for i in range(len(satisfaction)-1,-1,-1):
            if suffix + satisfaction[i] <= 0:
                break
            suffix += satisfaction[i]
            maxSat += suffix
        
        return maxSat
