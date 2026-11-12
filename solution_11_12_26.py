class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        ret = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                ret = max(ret, inc)
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                ret = max(ret, dec)
                inc = 1
            else:
                dec = 1
                inc = 1
        
        return ret
