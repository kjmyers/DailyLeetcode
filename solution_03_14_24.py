class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def solve(g):
            left = 0
            psum = 0
            ret = 0

            for right in range(len(nums)):
                psum += nums[right]
                while left <= right and psum > g:
                    psum -= nums[left]
                    left += 1
                
                ret += right - left + 1
            
            return ret
        
        return solve(goal) - solve(goal-1)
