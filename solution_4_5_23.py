class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        ret = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            ret = max(ret, math.ceil(prefix / (i+1)))
        
        return ret
