class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache
        def solve(ind):
            if ind >= len(nums):
                return 0
            
            return max(solve(ind+1), solve(ind+2) + nums[ind])
        
        return solve(0)
