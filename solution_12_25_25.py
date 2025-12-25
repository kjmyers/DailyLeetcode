class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse=True)
        
        ret = 0
        for i in range(k):
            ret += happiness[i] - i if happiness[i] - i > 0 else 0
        
        return ret
