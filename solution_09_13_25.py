class Solution:
    def maxFreqSum(self, s: str) -> int:
        vCount = defaultdict(int)
        cCount = defaultdict(int)
        for l in s:
            if l in 'aeiou':
                vCount[l] += 1
            else:
                cCount[l] += 1
        
        return max(vCount.values(), default=0) + max(cCount.values(), default=0)
