class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tot = 0
        ret = 0
        for g in gain:
            tot += g
            ret = max(ret, tot)
        
        return ret
