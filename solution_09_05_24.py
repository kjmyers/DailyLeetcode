class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        right = mean * (len(rolls) + n) - sum(rolls)
        if right < n*1 or right > n*6:
            return []
        
        ret = []
        val = right//n
        mod = right % n
        ret = [val] * n
        for i in range(mod):
            ret[i] += 1
        return ret
