class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
            if d[n] == 3:
                d.pop(n)
        
        for k in d.keys():
            return k
