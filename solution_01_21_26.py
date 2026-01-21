class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            ret = -1
            d = 1
            while (nums[i] & d) != 0:
                ret = nums[i] - d
                d = d << 1
            ans[i] = ret
        
        return ans
