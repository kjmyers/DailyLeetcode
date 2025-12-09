class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        fnext = defaultdict(int)
        for n in nums:
            fnext[n] += 1
        
        fprev = defaultdict(int)
        ret = 0
        for num in nums:
            fnext[num] -= 1
            ret = (ret + fnext[num*2] * fprev[num*2]) % (10**9 + 7)
            fprev[num] += 1
        
        return ret
