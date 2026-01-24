class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        ret = 0
        for i in range(n//2):
            ret = max(ret,nums[i]+nums[n-1-i])
        
        return ret
