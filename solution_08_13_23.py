class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = { -1 : True }

        def solve(i):
            if i in dp:
                return dp[i]
            
            ret = False
            
            if i > 0 and nums[i] == nums[i-1]:
                ret |= solve(i-2)
            
            if i > 1 and nums[i] == nums[i-1] == nums[i-2] and solve(i-3):
                ret |= solve(i-3)
            
            if i > 1 and nums[i] == (nums[i-1] + 1) == (nums[i-2] + 2):
                ret |= solve(i-3)
            
            dp[i] = ret
            return ret
        
        return solve(len(nums)-1)
