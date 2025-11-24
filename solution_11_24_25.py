class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        ret = []
        for num in nums:
            cur = cur << 1
            cur += num
            ret.append(cur % 5 == 0)
        
        return ret
