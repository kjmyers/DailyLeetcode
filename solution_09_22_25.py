class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxF = max(c.values())
        ret = 0
        for v in c.values():
            if v == maxF:
                ret += v
        
        return ret
