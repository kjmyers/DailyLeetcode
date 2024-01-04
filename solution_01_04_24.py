class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ret = 0
        
        for v in c.values():
            if v == 1:
                return -1
            d, r = divmod(v,3)
            if r == 0:
                ret += d
            else:
                ret += d + 1
            
        
        return ret
