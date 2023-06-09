class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        ret = 0
        start = 0

        for i in range(len(nums)):
            zero += int(nums[i] == 0)

            while zero > 1:
                zero -= int(nums[start] == 0)
                start += 1
            
            ret = max(ret, i - start)
        
        return ret
